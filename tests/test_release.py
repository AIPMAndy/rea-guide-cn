from pathlib import Path
from html.parser import HTMLParser
import unittest, json, re
ROOT=Path(__file__).resolve().parents[1]
class SiteParser(HTMLParser):
 def __init__(self):super().__init__();self.ids=set();self.links=[];self.external_js=[]
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  if 'id' in d:self.ids.add(d['id'])
  for key in ('href','src'):
   if key in d:self.links.append(d[key])
  if tag=='script' and d.get('src','').startswith(('http:','https:')): self.external_js.append(d['src'])
class Release(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.html=(ROOT/'index.html').read_text()
  cls.js=(ROOT/'assets/site.js').read_text()
  cls.parser=SiteParser();cls.parser.feed(cls.html)
  cls.data=json.loads((ROOT/'data/content.json').read_text())
 def test_counts(self):
  d=self.data
  self.assertEqual([len(d[x]) for x in ['chapters','prompts','cases','tasks','checks']],[38,64,12,30,12])
  self.assertEqual(len({x['id'] for x in d['chapters']}),38)
  self.assertEqual(len({x['id'] for x in d['prompts']}),64)
 def test_files(self):
  for name in ['README.md','START-HERE.md','LICENSE','LICENSE-DOCS.md','.nojekyll','index.html','assets/site.css','assets/site.js','assets/social-preview.svg','assets/favicon.svg','data/content.json','docs/SAFETY.md','docs/SOURCES.md','docs/AUDIT.md','docs/INSTALL-MAC.md','.github/workflows/pages.yml','examples/mini-app/test.mjs']:
   with self.subTest(file=name):self.assertTrue((ROOT/name).is_file(),name)
 def test_chapters_exist(self):
  for c in self.data['chapters']:
   p=ROOT/c['url']
   with self.subTest(chapter=c['id']):
    self.assertTrue(p.is_file(),str(p))
    text=p.read_text()
    self.assertGreater(len(text),750)
    for x in ['验收清单','红队审核','AIPMAndy','metaver.vip','非 REA 官方']:
     self.assertIn(x,text)
 def test_local_links(self):
  for link in self.parser.links:
   if link.startswith(('http:','https:','mailto:','tel:')):continue
   if link.startswith('#'):
    self.assertIn(link[1:],self.parser.ids,link)
   else:self.assertTrue((ROOT/link.split('#',1)[0]).is_file(),link)
 def test_no_remote_scripts_or_unsafe_insert(self):
  self.assertEqual(self.parser.external_js,[])
  self.assertNotIn('innerHTML',self.js)
  self.assertIn('textContent',self.js)
  self.assertIn('localStorage',self.js)
 def test_contact(self):
  self.assertIn('AIPMAndy',self.html)
  self.assertGreaterEqual(self.html.count('data-wechat'),3)
  self.assertIn('metaver.vip',self.html)
 def test_versions(self):
  self.assertEqual(self.data['version'],'5.0.0')
  self.assertIn('Node 22.19+', (ROOT/'docs/INSTALL-MAC.md').read_text())
  self.assertIn('morluto/rea', (ROOT/'docs/SOURCES.md').read_text())
 def test_permission_scope(self):
  for p in self.data['prompts']:
   self.assertIn('授权',p['body'])
   self.assertIn('证据',p['body'])
 def test_no_private_samples(self):
  self.assertTrue((ROOT/'examples/mini-app/src/order.js').is_file())
  self.assertNotIn('Authorization: Bearer',(ROOT/'examples/mini-app/src/order.js').read_text())
 def test_actions(self):
  wf=(ROOT/'.github/workflows/pages.yml').read_text()
  for phrase in ('unittest','actions/deploy-pages@v4','node examples/mini-app/test.mjs'):
   self.assertIn(phrase,wf)
if __name__=='__main__':unittest.main()
