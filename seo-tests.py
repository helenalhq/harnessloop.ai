import json,re
from pathlib import Path
from seo import FAQ
for lang in ('zh','en'):
 base=Path('dist/en' if lang=='en' else 'dist')
 for p in [base/'index.html',*base.glob('*/index.html')]:
  if p.parent.name=='en':continue
  text=p.read_text()
  ld=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',text).group(1))
  assert len(ld['@graph'])==3
  assert 'og:image' in text and 'summary_large_image' in text
 html=(base/'faq/index.html').read_text()
 graph=json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',html).group(1))['@graph']
 assert graph[-1]['@type']=='FAQPage'
 for q,a in FAQ[lang]:
  body=html.split('<body>',1)[1]
  assert q in body and a in body
  assert any(x['name']==q and x['acceptedAnswer']['text']==a for x in graph[-1]['mainEntity'])
assert Path('dist/assets/social.png').stat().st_size>1000
assert 'location.replace' not in Path('dist/assets/language.js').read_text()
print('PASS SEO: visible FAQ matches schema, stable locales, social image and entity graph')
