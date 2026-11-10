exec(open('scripts/capturar_layout.py',encoding='utf-8-sig').read().split('with sync_playwright()')[0])
with sync_playwright() as p:
 b=p.chromium.launch();page=b.new_page(viewport={'width':375,'height':900});errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 base=f'http://127.0.0.1:{server.server_port}/'
 page.goto(base+'classicos.html');page.wait_for_timeout(400)
 page.locator('button[data-j="10"]').click();assert page.locator('button[data-j="10"]').get_attribute('aria-pressed')=='true'
 assert page.locator('[data-draw="rk"] tr').count()==16
 page.locator('#fg-sel').select_option(index=2);assert page.locator('[data-draw="d-vs"]').inner_text().strip()!='—'
 print('PASS classic filters and selector')
 page.goto(base+'horarios.html');page.wait_for_timeout(300)
 cell=page.locator('.celula:not(.vazia)').first;cell.click();assert page.locator('.celula.sel').count()>0;print('PASS schedule grid selection')
 page.goto(base+'ultima-rodada.html');page.locator('#b3').click();assert page.locator('#b3').get_attribute('aria-pressed')=='true';print('PASS relegation comparison')
 page.goto(base+'simulacao.html');page.wait_for_timeout(200);th=page.locator('#tab44 th').first;th.click();print('PASS sortable table click')
 for name in ['simulacao','horarios','ultima-rodada','classicos']:
  page.set_viewport_size({'width':720,'height':900});page.goto(base+name+'.html');page.evaluate("document.documentElement.style.zoom='2'");page.wait_for_timeout(200)
  assert page.evaluate('document.documentElement.scrollWidth <= innerWidth'),name
  print('PASS 200% zoom',name)
 assert not errors,errors
 b.close()
server.shutdown()
