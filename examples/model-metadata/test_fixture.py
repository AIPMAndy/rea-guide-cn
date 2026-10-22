import pathlib,subprocess,sys,unittest
ROOT=pathlib.Path(__file__).resolve().parent
class SyntheticHeaderTests(unittest.TestCase):
 def test_header(self):
  subprocess.run([sys.executable,str(ROOT/'make_fixture.py')],check=True,capture_output=True)
  run=subprocess.run([sys.executable,str(ROOT/'inspect_header.py')],check=True,capture_output=True,text=True)
  self.assertIn('synthetic_tensor',run.stdout)
 def test_bad_header(self):
  from tempfile import TemporaryDirectory
  with TemporaryDirectory() as tmp:
   t=pathlib.Path(tmp)/'broken.bin';t.write_bytes(b'bad')
   run=subprocess.run([sys.executable,str(ROOT/'inspect_header.py'),str(t)],capture_output=True,text=True)
   self.assertNotEqual(run.returncode,0)
if __name__=='__main__':unittest.main()
