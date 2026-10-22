from pathlib import Path
from urllib.parse import unquote,urlsplit
from html.parser import HTMLParser
import json,unittest,re
ROOT=Path(__file__).resolve().parents[1]
class P(HTMLParser):
 def __init__(self):super().__init__();self.refs=[];self.ids=set();self.external_scripts=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if d.get('id'):self.ids.add(d['id'])
  for k in ('href','src'):
   if d.get(k):self.refs.append(d[k])
  if tag=='script' and d.get('src','').startswith(('https://','http://')):self.external_scripts.append(d['src'])
class V5Site(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.data=json.loads((ROOT/'data/content.json').read_text(encoding='utf-8'))
  cls.index=(ROOT/'index.html').read_text(encoding='utf-8')
 def test_counts_and_source_status(self):
  d=self.data
  self.assertEqual(d['version'],'5.0.0')
  self.assertEqual([len(d[x]) for x in ['chapters','prompts','cases','tasks','checks','capabilities']],[38,64,12,30,12,28])
  self.assertEqual(len({x['id'] for x in d['chapters']}),38)
  self.assertEqual(len({x['id'] for x in d['prompts']}),64)
  for x in d['capabilities']:
   self.assertEqual(x['evidence'],'O（上游能力说明）')
   self.assertIn('未实测',x['validated'])
 def test_home_numbers(self):
  for m in ['>38</strong>','>64</strong>','>12</strong>','38 章系统课程','64 条完整指令','12 个案例','28 类官方能力']:
   self.assertIn(m,self.index,m)
 def test_rendered_chapters(self):
  for c in self.data['chapters']:
   source=ROOT/c['url']
   target=ROOT/'pages'/c['url'].replace('.md','.html')
   self.assertTrue(source.is_file(),c['url'])
   self.assertTrue(target.is_file(),str(target))
   content=target.read_text()
   self.assertIn('微信',content)
   self.assertIn('metaver.vip',content)
   self.assertIn('验收清单',content)
   self.assertNotIn('<script>alert(',content)
 def test_rendered_links(self):
  pages=list((ROOT/'pages').rglob('*.html'))
  self.assertGreaterEqual(len(pages),70)
  for path in [ROOT/'index.html',*pages]:
   p=P();p.feed(path.read_text(encoding='utf-8'))
   self.assertFalse(p.external_scripts,path)
   for ref in p.refs:
    if ref.startswith(('#','http:','https:','mailto:','tel:','data:')):continue
    u=urlsplit(ref);link=unquote(u.path)
    full=(path.parent/link).resolve()
    self.assertTrue(full.is_file(),f'Broken link {ref} in {path}')
 def test_website_does_not_execute_untrusted_html(self):
  js=(ROOT/'assets/site.js').read_text()
  self.assertNotIn('innerHTML',js)
  self.assertIn('renderCapabilities()',js)
  self.assertIn('capability-grid',self.index)
  self.assertIn('pages/',js)
 def test_complete_provenance(self):
  for name in ['docs/BENCHMARK.md','docs/PROVENANCE.md','docs/CAPABILITIES.md','docs/AUDIT.md','tools/validate_evidence.py']:
   self.assertTrue((ROOT/name).is_file())
  self.assertIn('Node 22.16.0 真正跑 REA',(ROOT/'docs/AUDIT.md').read_text())
if __name__=='__main__':unittest.main()
