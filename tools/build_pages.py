"""Build source-linked, safe, static chapter readers from locally-owned Markdown.

Dependencies for MAINTAINERS only: pip install mistune beautifulsoup4
Committed HTML output requires neither Python dependencies nor JS at viewer runtime.
"""
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit, quote
import json, re, html, os, datetime
import mistune
from bs4 import BeautifulSoup
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'pages'
D=json.loads((ROOT/'data/content.json').read_text())
CHAPTER_PATHS={x['url']:x for x in D['chapters']}
# Including source documentation and templates avoids links that render as raw Markdown on Pages.
mds=[p for p in ROOT.rglob('*.md') if not any(x in p.parts for x in ('node_modules','pages','.git','__pycache__'))]
source={p.relative_to(ROOT).as_posix():p for p in mds}
renderer=mistune.create_markdown(escape=True,plugins=['table','task_lists','strikethrough'])
nav=D['chapters']

def article_link(src:Path,href:str):
    parts=urlsplit(href)
    if parts.scheme or parts.netloc or href.startswith('#'):
        return href
    dest=(src.parent/parts.path).resolve()
    try:key=dest.relative_to(ROOT.resolve()).as_posix()
    except ValueError:return href
    if key in source:
        target=OUT/(key[:-3]+'.html')
    elif key and dest.is_file():
        target=dest
    else:
        return href
    return os.path.relpath(target, (OUT/src.relative_to(ROOT)).parent).replace('\\','/')+(('#'+parts.fragment) if parts.fragment else '')

def clean(md_path:Path):
    document=BeautifulSoup(renderer(md_path.read_text(encoding='utf-8')),'html.parser')
    for tag in document.find_all(['script','iframe','object','embed']):tag.decompose()
    for a in document.find_all('a'):
        href=a.get('href','')
        if href.lower().startswith(('javascript:','data:','vbscript:')):a.attrs.pop('href',None);continue
        a['href']=article_link(md_path,href)
        if a['href'].startswith(('http://','https://')):a['rel']='noopener noreferrer';a['target']='_blank'
    for img in document.find_all('img'):
        src=img.get('src','')
        if src.lower().startswith(('javascript:','data:','vbscript:')):img.attrs.pop('src',None)
        elif src and not src.startswith(('https://','http://')):
            img['src']=article_link(md_path,src)
    # No generated arbitrary event handlers or uncontrolled CSS.
    for tag in document.find_all(True):
        for k in list(tag.attrs):
            if k.lower().startswith('on'):tag.attrs.pop(k,None)
    headings={}
    for h in document.find_all(re.compile(r'^h[1-6]$')):
        base=re.sub(r'[^a-z0-9\u4e00-\u9fa5-]+','-',h.get_text(' ',strip=True).lower()).strip('-') or 'section'
        headings[base]=headings.get(base,0)+1
        h['id']=base if headings[base]==1 else f'{base}-{headings[base]}'
    return str(document)

def build():
    for key,path in source.items():
        out=OUT/(key[:-3]+'.html');out.parent.mkdir(parents=True,exist_ok=True)
        depth=len(out.relative_to(OUT).parts)-1
        prefix='../'*(depth+1)
        title=CHAPTER_PATHS[key]['title'] if key in CHAPTER_PATHS else path.stem.replace('-',' ')
        prev_next=''
        if key in CHAPTER_PATHS:
            index=D['chapters'].index(CHAPTER_PATHS[key])
            prev=nav[index-1] if index else None
            nxt=nav[index+1] if index+1<len(nav) else None
            def path_to(n):return os.path.relpath(OUT/(n['url'][:-3]+'.html'),out.parent).replace('\\','/')
            prev_next='<div class="reader-next">'+(f'<a href="{html.escape(path_to(prev))}">← 上一章：{html.escape(prev["title"])}</a>' if prev else '<span>第一章</span>')+(f'<a href="{html.escape(path_to(nxt))}">下一章：{html.escape(nxt["title"])} →</a>' if nxt else '<span>最后一章</span>')+'</div>'
        side=''.join(f'<a {"aria-current=page class=active" if n["url"]==key else ""} href="{html.escape(os.path.relpath(OUT/(n["url"][:-3]+".html"),out.parent).replace(os.sep,"/"))}">{html.escape(n["id"])}　{html.escape(n["title"])}</a>' for n in nav)
        body=clean(path)
        page=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(title)}｜REA 逆向万物保姆级攻略</title><meta name="description" content="REA 逆向工程开源中文教程，逐步操作、证据链、反证和安全验收。"><link rel="icon" href="{prefix}assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="{prefix}assets/site.css"><link rel="stylesheet" href="{prefix}assets/reader.css"></head><body>
<a class="skip" href="#content">跳到正文</a>
<header class="topbar"><div class="wrap nav"><a class="brand" href="{prefix}index.html#chapters"><span class="brand-icon">R<span>✦</span></span><span>REA <strong>FIELD GUIDE</strong><small>完整中文阅读版 · V5</small></span></a><nav class="desktopnav"><a href="{prefix}index.html">网站首页</a><a href="{prefix}index.html#prompts">64 条指令</a><a href="{prefix}index.html#coverage">官方能力</a><a href="{prefix}pages/docs/SAFETY.html">安全</a></nav><div class="navcontact"><button type="button" data-wechat>微信 AIPMAndy</button><a href="https://metaver.vip/" target="_blank" rel="noopener noreferrer">作者官网 ↗</a></div></div></header>
<div class="reading-banner"><div class="wrap"><span>REA FIELD NOTES / READABLE EDITION</span><h1>{html.escape(title)}</h1><p>完整内容可读 · 保留上游来源 · 明确标记未实测能力</p></div></div>
<div class="wrap reading-grid"><aside class="reader-sidebar"><strong>38 章完整目录</strong><nav aria-label="章节目录">{side}</nav></aside><main id="content" class="reading-main"><div class="reading-top"><a href="{prefix}index.html#chapters">← 返回目录</a><a href="https://github.com/AIPMAndy/rea-guide-cn/blob/main/{quote(key)}" target="_blank" rel="noopener noreferrer">查看 Markdown 原文 ↗</a></div><div class="prose">{body}</div>{prev_next}<div class="reading-cta"><div><strong>AI 酋长 Andy</strong><p>免费开源教程，可持续提交实测与反证。微信：AIPMAndy</p></div><div><button type="button" data-wechat>复制微信号</button><a href="https://metaver.vip/" target="_blank" rel="noopener noreferrer">我的官网 ↗</a></div></div></main></div>
<div class="mobile-cta"><button type="button" data-wechat>微信 AIPMAndy · 复制</button><a href="https://metaver.vip/">作者官网 ↗</a></div><div class="toast" id="toast" role="status" aria-live="polite"></div><script src="{prefix}assets/contact.js" defer></script></body></html>'''
        # Existing source links in Markdown assume root-relative positions; BeautifulSoup above rewrites .md links.
        page=page.replace(f'href="{prefix}pages/docs/SAFETY.html"',f'href="{os.path.relpath(OUT/"docs/SAFETY.html",out.parent).replace(os.sep,"/" )}"')
        out.write_text(page,encoding='utf-8')
    # Sitemap includes browsable tutorial pages, not unverified external sites.
    urls=['https://aipmandy.github.io/rea-guide-cn/']+[f'https://aipmandy.github.io/rea-guide-cn/pages/{key[:-3]}.html' for key in sorted(source)]
    xml='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{html.escape(url)}</loc><lastmod>2026-10-21</lastmod></url>\n' for url in urls)+'</urlset>\n'
    (ROOT/'sitemap.xml').write_text(xml)
    print(f'Built {len(source)} human-readable HTML pages.')

if __name__=='__main__':build()
