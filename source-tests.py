"""Data discipline (planning doc ch. 2 and 6.2): a regulatory figure ships only if it is registered.

Checks the built HTML, not the source files:
  1. every external link is a registered official source or a listed non-regulatory link;
  2. retired figures and promise-style wording are absent;
  3. each registered figure still appears where the site quotes it, so registry and copy agree.
"""
from datetime import date
from pathlib import Path
from sources import SOURCES, audit, next_review

routes = ['', 'how-it-works', 'data-factory', 'research', 'contact', 'privacy', 'faq', 'solutions', 'demo']
documents = [Path('dist/zh/index.html')]
documents += [Path('dist') / slug / 'index.html' for slug in routes if slug]
documents += [Path('dist/en') / (slug + '/' if slug else '') / 'index.html' for slug in routes]

problems = []
for path in documents:
    problems += [f'{path}: {problem}' for problem in audit(path.read_text().split('<body>', 1)[1])]

# (source key, page, language, phrase that must stay next to the source link)
QUOTES = (
    ('isf', 'home', 'zh', '装船前至少 24 小时申报'),
    ('isf', 'home', 'zh', '$5,000'),
    ('isf', 'home', 'en', 'at least 24 hours before lading'),
    ('isf', 'home', 'en', '$5,000'),
    ('isf', 'demo', 'zh', '装货港代码'),
    ('dd', 'home', 'zh', '30 个日历日'),
    ('dd', 'home', 'en', '30 calendar days'),
    ('usc1592', 'home', 'en', '4×'),
    ('usc1592', 'home', 'en', '40% of dutiable value'),
    ('customs128', 'home', 'zh', '0.5‰'),
    ('customs128', 'home', 'zh', '第 15 日起'),
    ('customs128', 'home', 'zh', '人民币 50 元'),
)
PAGES = {
    'home': {'zh': 'dist/zh/index.html', 'en': 'dist/en/index.html'},
    'demo': {'zh': 'dist/demo/index.html', 'en': 'dist/en/demo/index.html'},
}
urls = {source['key']: source['url'] for source in SOURCES}
for key, page, lang, phrase in QUOTES:
    text = Path(PAGES[page][lang]).read_text()
    if urls[key] not in text or phrase not in text:
        problems.append(f'{key}: "{phrase}" and its source link must appear together on the {lang} {page} page')

assert not problems, '\n'.join(problems)
due = next_review()
state = 'OVERDUE: reopen the official pages and update `checked` in sources.py' if due <= date.today() else 'scheduled'
print(f'PASS sources: {len(SOURCES)} registered official sources, no unregistered links or retired figures; quarterly review {state} for {due.isoformat()}')
