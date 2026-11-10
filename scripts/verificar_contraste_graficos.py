exec(open('scripts/capturar_layout.py',encoding='utf-8-sig').read().split('with sync_playwright()')[0])
import json
def luminance(rgb):
 vals=[float(v)/255 for v in rgb[rgb.index('(')+1:rgb.index(')')].split(',')[:3]];vals=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in vals];return sum(v*w for v,w in zip(vals,[.2126,.7152,.0722]))
def contrast(a,b):
 x,y=luminance(a),luminance(b);return (max(x,y)+.05)/(min(x,y)+.05)
with sync_playwright() as p:
 b=p.chromium.launch();page=b.new_page(viewport={'width':1440,'height':1000})
 for theme in ['dark','light']:
  page.emulate_media(color_scheme=theme);page.goto(f'http://127.0.0.1:{server.server_port}/simulacao.html');page.wait_for_timeout(300)
  colors=page.locator('.dif').evaluate_all('(els)=>els.map(e=>[getComputedStyle(e).color,getComputedStyle(e).backgroundColor])')
  assert all(contrast(fg,bg)>=4.5 for fg,bg in colors),f'{theme}: difficulty contrast fails'
  assert page.locator('#final').evaluate('(e)=>getComputedStyle(e).backgroundColor===getComputedStyle(e.closest("section")).backgroundColor'),f'{theme}: chart detached from surface'
  assert page.locator('#final svg').get_attribute('role')=='img'
  assert page.locator('#curva svg').get_attribute('aria-label')
  for graph in ['final','curva']:
   panel=page.locator('#'+graph).evaluate('(e)=>getComputedStyle(e).backgroundColor')
   for fg in page.locator('#'+graph+' text').evaluate_all('(es)=>es.map(e=>getComputedStyle(e).fill)'):
    assert contrast(fg,panel)>=4.5,(theme,graph,fg,panel)
  print('PASS',theme,'difficulty and chart labels >=4.5, integrated surface, accessible chart descriptions')
 # Live OS theme change must update SVG color without reload.
 page.emulate_media(color_scheme='light');before=page.locator('#final text').first.evaluate('(e)=>getComputedStyle(e).fill');page.emulate_media(color_scheme='dark');after=page.locator('#final text').first.evaluate('(e)=>getComputedStyle(e).fill');assert before!=after
 print('PASS live theme change')
 for theme in ['light','dark']:
  page.emulate_media(color_scheme=theme);page.goto(f'http://127.0.0.1:{server.server_port}/horarios.html');page.wait_for_timeout(200)
  colors=page.locator('.celula:not(.vazia)').evaluate_all('(es)=>es.map(e=>[getComputedStyle(e).color,getComputedStyle(e).backgroundColor])')
  assert all(contrast(fg,bg)>=4.5 for fg,bg in colors),theme
  print('PASS',theme,'schedule heatmap contrast >=4.5')

 b.close()
server.shutdown()
