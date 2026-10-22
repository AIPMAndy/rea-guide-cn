from pathlib import Path
import importlib.util,json,hashlib,tempfile,unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('rea_evidence',ROOT/'tools/validate_evidence.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
class EvidenceTests(unittest.TestCase):
 def setUp(self):self.source=ROOT/'examples/mini-app/evidence-manifest.json';self.good=json.loads(self.source.read_text())
 def test_good_tlocal(self):self.assertEqual(module.validate(self.good),[])
 def test_changed_digest_rejected(self):
  x={**self.good,'sha256':'0'*64};self.assertIn('SHA256 does not match source',module.validate(x))
 def test_path_traversal_rejected(self):
  x={**self.good,'source':'../other/file'};self.assertIn('Unsafe source path',module.validate(x))
 def test_fake_rea_evidence_rejected(self):
  x={**self.good,'status':'T-REA'};self.assertIn('T-REA requires runtime evidence fields',module.validate(x))
 def test_secret_rejected(self):
  x={**self.good,'result':'Authorization: Bearer fakeToken123'};self.assertTrue(any('Possible credential' in v for v in module.validate(x)))
if __name__=='__main__':unittest.main()
