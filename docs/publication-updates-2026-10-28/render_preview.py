"""Render independent review pages without modifying the live Jekyll sources."""
from pathlib import Path
import hashlib
import html
import json
import re
import sys

import yaml

sys.path.insert(0, r"C:\Users\marcu\AppData\Local\Temp\codex-publication-preview-20261028\python")
from liquid import Environment

ROOT = Path(__file__).resolve().parents[2]
PREVIEW = Path(__file__).resolve().parent
NAMES = ["publications", "news", "failure-cv", "about"]
official = "--official" in sys.argv
drafts = {
    name: ((ROOT / "_pages" if official else PREVIEW / "draft-pages") / f"{name}.md").read_text(encoding="utf-8")
    for name in NAMES
}
config = yaml.safe_load((ROOT / "_config.yml").read_text(encoding="utf-8"))
navigation = yaml.safe_load((ROOT / "_data/navigation.yml").read_text(encoding="utf-8"))["main"]
routes = {
    "/": "index.html",
    "/publications/": "publications.html",
    "/news/": "news.html",
    "/failure-cv/": "failure-cv.html",
}


def href(url):
    return routes.get(url, "https://xunzhangsean.github.io" + url)


def relative_urls(content):
    return re.sub(
        r"\{\{\s*([\"'])(.*?)\1\s*\|\s*relative_url\s*\}\}",
        lambda match: href(match[2]) if match[2] in routes else match[2],
        content,
    )


def masthead(route):
    active = ' class="is-active"' if route == "/" else ""
    links = (
        '<li class="masthead__menu-item masthead__menu-item--lg masthead__menu-home-item">'
        f'<a{active} href="index.html">Xun Zhang</a></li>'
    )
    for item in navigation:
        active = ' class="is-active"' if route == item["url"] and item["url"] != "/" else ""
        links += (
            '<li class="masthead__menu-item">'
            f'<a{active} href="{html.escape(href(item["url"]))}">'
            f'{html.escape(item["title"])}</a></li>'
        )
    return (
        '<div class="masthead"><div class="masthead__inner-wrap"><div class="masthead__menu">'
        '<nav id="site-nav" class="greedy-nav site-nav" aria-label="Primary navigation">'
        '<a class="site-brand" href="index.html"><img class="site-brand__logo" '
        'src="/images/CEE%20logo.png" '
        'alt="Cornell Duffield Engineering School of Civil and Environmental Engineering"></a>'
        '<button class="hidden" type="button" aria-label="Toggle navigation">'
        '<div class="navicon"></div></button>'
        f'<ul class="visible-links">{links}</ul><ul class="hidden-links hidden"></ul>'
        '</nav></div></div></div>'
    )


def sidebar():
    author = config["author"]
    links = "".join(
        f'<a href="{html.escape(author[key])}">{label}</a>'
        for key, label in [
            ("researchgate", "ResearchGate"),
            ("googlescholar", "Google Scholar"),
            ("linkedin", "LinkedIn"),
            ("github", "GitHub"),
        ]
        if author.get(key)
    )
    return (
        '<div class="sidebar sticky"><div itemscope itemtype="http://schema.org/Person" '
        'class="profile_box"><div class="author__avatar">'
        f'<img src="/{author["avatar"]}" alt="Xun Zhang"></div><div class="author__content">'
        '<h3 class="author__name" itemprop="name">Xun Zhang</h3>'
        f'<p class="author__bio">{html.escape(author["bio"])}</p></div>'
        f'<div class="profile-links">{links}</div></div></div>'
    )


for name, content in drafts.items():
    route = "/" if name == "about" else f"/{name}/"
    if name == "about":
        body = content[content.index("<span class='anchor'") :]
        capture = (
            "{% capture homepage_news_source %}{% include_relative news.md %}{% endcapture %}\n"
            "    {% include latest-news.html content=homepage_news_source %}"
        )
        if capture in body:
            latest = Environment().from_string(
                (ROOT / "_includes/latest-news.html").read_text(encoding="utf-8")
            ).render(**{"include": {"content": relative_urls(drafts["news"])}})
            body = body.replace(capture, latest, 1)
    else:
        body = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", content, count=1, flags=re.S)
    title = {
        "about": "About Me",
        "publications": "Publications and Conferences",
        "news": "News",
        "failure-cv": "Failure CV",
    }[name]
    kind = "home-page" if name == "about" else "sub-page"
    page = (
        '<!doctype html><html lang="en" class="js"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
        '<meta name="robots" content="noindex,nofollow">'
        f'<title>{title} · October 2026 update preview</title>'
        '<link rel="icon" href="/images/favicon-32x32.png">'
        '<link rel="stylesheet" href="preview.css"></head>'
        f'<body class="{kind}">{masthead(route)}<div id="main" role="main">'
        f'{sidebar() if name == "about" else ""}<article class="page">'
        '<div class="page__inner-wrap"><section class="page__content">'
        f'{relative_urls(body)}</section></div></article></div></body></html>'
    )
    filename = "index.html" if name == "about" else f"{name}.html"
    (PREVIEW / filename).write_text(page, encoding="utf-8", newline="\n")

manifest = {
    "previewOnly": not official,
    "sourceMode": "official" if official else "draft",
    "homepageNewsLimit": 3,
    "baselineSha256": {
        str(Path("_pages") / f"{name}.md"): hashlib.sha256(
            (ROOT / "_pages" / f"{name}.md").read_bytes()
        ).hexdigest()
        for name in NAMES
    },
    "changes": [
        "DIN accepted 27 October 2026; retain the arXiv link, without a DOI",
        "Geomorphology accepted 22 October 2026; update the final title and DOI",
        "Add the two acceptance announcements to News and the homepage news feed",
        "One additional 2026 Journal of Hydrology rejection: x1 to x2",
        "Homepage automatically renders the first three News entries",
        "Last updated: October 28, 2026",
    ],
}
previous_manifest = PREVIEW / "manifest.json"
if previous_manifest.exists():
    manifest["baselineSha256"] = json.loads(previous_manifest.read_text(encoding="utf-8")).get(
        "baselineSha256", manifest["baselineSha256"]
    )
(PREVIEW / "manifest.json").write_text(
    json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8", newline="\n"
)

original_pubs = (ROOT / "_pages/publications.md").read_text(encoding="utf-8")
marker = "    <h3>Papers in Progress</h3>"
assert drafts["publications"][drafts["publications"].index(marker) :] == original_pubs[original_pubs.index(marker) :]
original_home = (ROOT / "_pages/about.md").read_text(encoding="utf-8")
assert drafts["about"].split('  <div class="news-list">')[0] == original_home.split('  <div class="news-list">')[0]
assert drafts["publications"].count("Field characteristics and initiation mechanisms") == 1
assert "ssrn.5415435" not in drafts["publications"]
assert "Under Review" not in drafts["publications"]
print("Rendered four independent preview pages with the existing site stylesheet.")
print("Source: implemented official pages." if official else "Source: preview drafts; official pages were not changed.")
