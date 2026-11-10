from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote
import re, threading, http.server, functools
from playwright.sync_api import sync_playwright
pages=['index.html','simulacao.html','horarios.html','ultima-rodada.html','classicos.html']
class Links(HTMLParser):
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ('href','src') and v and not v.startswith(('http','data:','#','mailto:')):
    assert Path(unquote(v.split('#')[0])).exists(),(self.file,v)
for name in pages:
 p=Links(); p.file=name; p.feed(Path(name).read_text(encoding='utf-8'))
for old,new in [('backup/index (1).html','horarios.html'),('backup/index (2).html','ultima-rodada.html'),('backup/index-.html','classicos.html')]:
 a=re.findall(r'<script\b.*?</script>',Path(old).read_text(encoding='utf-8'),re.S)
 b=re.findall(r'<script\b.*?</script>',Path(new).read_text(encoding='utf-8'),re.S)
 if new == "horarios.html":
  # Display code intentionally changes; the embedded dataset must remain identical.
  a=re.search(r"const DADOS\s*=.*",Path(old).read_text(encoding="utf-8"))[0]
  b=re.search(r"const DADOS\s*=.*",Path(new).read_text(encoding="utf-8"))[0]
 assert a==b,new
print('PASS: local links and original secondary analysis scripts preserved')
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*args): pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),Quiet)
threading.Thread(target=server.serve_forever,daemon=True).start()
with sync_playwright() as p:
 browser=p.chromium.launch()
 page=browser.new_page()
 errors=[]; page.on('pageerror',lambda e:errors.append(str(e)))
 for width,theme in [(1440,'light'),(375,'light'),(1440,'dark'),(375,'dark')]:
  page.set_viewport_size({'width':width,'height':1000});page.emulate_media(color_scheme=theme)
  page.goto(f'http://127.0.0.1:{server.server_port}/index.html');page.screenshot(path=f'portal-{width}-{theme}.png',full_page=True)
  assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),(width,theme)
  assert page.locator('h1').count()==1
  print('PASS: portal',width,theme,'no horizontal overflow')
 for name in pages[1:]:
  page.goto(f'http://127.0.0.1:{server.server_port}/{name}'); page.wait_for_timeout(700)
  assert page.locator('.portal-links a[aria-current="page"]').count()==1,name
  print('PASS: analysis loads and active navigation',name)
 print('Browser errors:',errors)
 assert not errors
 browser.close()
server.shutdown()

