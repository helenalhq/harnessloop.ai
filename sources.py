"""Source registry for every regulatory figure quoted on the public site.

Planning rule (FA-HARNESS-WEB-005, ch. 2 and 6.2): a number may appear on the site only if it is
registered here with its official wording, link and check date. `source-tests.py` enforces this
against the built HTML, so an unregistered link or a banned figure fails the test run.

Maintenance: once a quarter, reopen each link, compare the wording, update `checked`, and commit.
The test prints the next review date; it warns when the date has passed.
"""
from datetime import date, timedelta

ECFR_113_62 = 'https://www.ecfr.gov/current/title-19/chapter-I/part-113/section-113.62'
FMC_DD = 'https://www.fmc.gov/articles/fmc-publishes-final-rule-on-detention-and-demurrage-billing-practices/'
USC_1592 = 'https://www.law.cornell.edu/uscode/text/19/1592'
CUSTOMS_128 = 'https://www.customs.gov.cn/customs/302249/302266/302267/356554/index.html'

REVIEW_DAYS = 92  # a quarter

SOURCES = (
    {
        'key': 'isf', 'label': '19 CFR § 113.62', 'issuer': {'zh': '美国海关与边境保护局', 'en': 'U.S. CBP'},
        'url': ECFR_113_62, 'checked': date(2026, 11, 25),
        'figure': {'zh': '装船前至少 24 小时申报；逾期每次违规定额赔偿金 $5,000',
                   'en': 'Filed at least 24 hours before lading; $5,000 liquidated damages per violation'},
        'note': '2026-11-26 复核未完成：eCFR 对自动访问返回跳转页，需人工打开核对。',
    },
    {
        'key': 'dd', 'label': 'FMC final rule on D&D billing', 'issuer': {'zh': '美国联邦海事委员会', 'en': 'U.S. FMC'},
        'url': FMC_DD, 'checked': date(2026, 11, 26),
        'figure': {'zh': '账单须在最后一次收费后 30 个日历日内开出；至少 30 个日历日争议窗口',
                   'en': 'Invoices within 30 calendar days from when charges were last incurred; at least 30 calendar days to dispute'},
        'quote': 'within 30 calendar days from when charges were last incurred / at least 30 calendar days to make fee mitigation, refund, or waiver requests',
    },
    {
        'key': 'usc1592', 'label': '19 U.S.C. § 1592', 'issuer': {'zh': '美国法典', 'en': 'U.S. Code'},
        'url': USC_1592, 'checked': date(2026, 11, 26),
        'figure': {'zh': '重大过失：少缴税款的 4 倍；未影响税款征收时为货值的 40%',
                   'en': 'Gross negligence: four times the lawful duties, or 40 percent of dutiable value'},
        'quote': 'four times the lawful duties, taxes, and fees / 40 percent of the dutiable value of the merchandise',
        'note': 'uscode.house.gov 与 govinfo 的条目地址本轮返回 404，暂用 Cornell LII 的美国法典全文。',
    },
    {
        'key': 'customs128', 'label': '海关总署令第 128 号', 'issuer': {'zh': '海关总署', 'en': 'GACC'},
        'url': CUSTOMS_128, 'checked': date(2026, 11, 25),
        'figure': {'zh': '第 15 日起按日征收计税价格的 0.5‰，起征点人民币 50 元', 'en': ''},
        'note': '2026-11-26 复核未完成：本机网络下该站证书链校验失败，需人工打开核对。',
    },
)

# Figures the planning document retired, and promise-style wording it forbids.
BANNED = (
    '100–400', '450 亿', '450 billion', '40–60%', '30→9', '复用率 70%', '毛利率',
    '保证合规', '免除罚款', '避免罚款', '确保通过', '零罚款',
    'guarantee', 'Guarantee', '保证通过', '100% compliance',
)
BANNED_PATTERNS = (
    r'最高可达', r'高达\s*\d', r'提升\s*\d+\s*%', r'节省\s*\d+\s*%', r'降低\s*\d+\s*%',
    r'\bup to \d+%\b', r'\b\d+% (?:faster|fewer|less|more|reduction)\b',
)

# External links that are not regulatory sources but are allowed on the site.
OTHER_EXTERNAL = {
    'https://vercel.com/legal/privacy-policy': 'hosting privacy notice linked from the privacy page',
    'https://github.com/rsi-gear/gear': 'research reference, labelled as not a partnership',
}


def next_review():
    """Earliest date on which any source is due for its quarterly check."""
    return min(s['checked'] for s in SOURCES) + timedelta(days=REVIEW_DAYS)


def allowed_urls():
    return {s['url'] for s in SOURCES} | set(OTHER_EXTERNAL)


def audit(text, today=None):
    """Return a list of problems found in a built HTML document."""
    import re
    problems = []
    for link in re.findall(r'href="(https?://[^"#]+)"', text):
        if 'harnessloop.ai' in link or link in allowed_urls():
            continue
        problems.append(f'unregistered external link: {link}')
    for phrase in BANNED:
        if phrase in text:
            problems.append(f'banned figure or promise: {phrase}')
    for pattern in BANNED_PATTERNS:
        if re.search(pattern, text):
            problems.append(f'banned pattern matched: {pattern}')
    return problems
