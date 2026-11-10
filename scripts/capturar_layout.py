from pathlib import Path
import threading,http.server,sys
from playwright.sync_api import sync_playwright
sys.stdout.reconfigure(encoding='utf-8')
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Quiet);threading.Thread(target=server.serve_forever,daemon=True).start()
out=Path('docs/previews/layout');out.mkdir(parents=True,exist_ok=True)
phase=sys.argv[1] if len(sys.argv)>1 else 'before'
with sync_playwright() as p:
 browser=p.chromium.launch(); page=browser.new_page();errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 for name in ['simulacao','horarios','ultima-rodada','classicos']:
  for w,theme in [(1440,'light'),(375,'light')]+([] if phase=='before' else [(1440,'dark'),(375,'dark')]):
   page.set_viewport_size({'width':w,'height':1100});page.emulate_media(color_scheme=theme);page.goto(f'http://127.0.0.1:{server.server_port}/{name}.html');page.wait_for_timeout(600)
   page.screenshot(path=str(out/f'{phase}-{name}-{w}-{theme}.png'))
   print(name,w,theme,'width',page.evaluate('document.documentElement.scrollWidth'),'tables',page.locator('tbody tr').count())
  if phase!='before':
   print('Small controls',page.locator('button:visible,select:visible').evaluate_all('(els)=>els.filter(e=>e.getBoundingClientRect().height<44).length'))
 print('Errors',errors);browser.close()
server.shutdown()
