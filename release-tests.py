import os, subprocess, tempfile, shutil
from pathlib import Path
from xml.etree import ElementTree as ET
source=Path(__file__).parent
with tempfile.TemporaryDirectory() as tmp:
 p=Path(tmp)/'site'; shutil.copytree(source,p,ignore=shutil.ignore_patterns('.git','node_modules','__pycache__'))
 for env,expected in [({},False),({'SITE_ENV':'production'},True),({'SITE_ENV':'production','VERCEL_ENV':'preview'},False),({'VERCEL_ENV':'production'},True)]:
  clean={k:v for k,v in os.environ.items() if k not in ('SITE_ENV','VERCEL_ENV')};clean.update(env)
  subprocess.run(['python3','build.py'],cwd=p,env=clean,check=True)
  contact=(p/'dist/contact/index.html').read_text()
  assert '<form' not in contact, 'Local brief must not have native form submission fallback'
  home=(p/'dist/index.html').read_text()
  assert ('name="robots" content="index,follow"' in home)==expected, f'Wrong indexing policy: {env}'
  assert ('Disallow: /' in (p/'dist/robots.txt').read_text()) != expected
  for prefix in ('','en/'):
   for slug in ('','how-it-works/','data-factory/','contact/','research/','privacy/','faq/'):
    html=(p/f'dist/{prefix}{slug}index.html').read_text()
    assert 'rel="canonical"' in html and 'hreflang="zh-CN"' in html and 'hreflang="en"' in html
    assert 'property="og:title"' in html and 'name="twitter:card"' in html
    assert '开发预览' not in html and 'Development preview' not in html
  assert len(ET.parse(p/'dist/sitemap.xml').getroot())==14
  assert (p/'dist/404.html').exists()
print('PASS release: safe no-JS contact, four environment modes, 14 SEO routes, sitemap and 404')
