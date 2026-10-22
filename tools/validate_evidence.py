"""Validate a JSON evidence manifest for source traceability. No REA execution.

Usage: python3 tools/validate_evidence.py path/to/manifest.json
The manifest refers only to files under the allowed root; paths outside are rejected.
"""
import hashlib,json,pathlib,sys,re
ROOT=pathlib.Path(__file__).resolve().parents[1]
REQUIRED={'id','kind','source','sha256','result','status'}
ALLOWED={'T-local','T-REA','O','E','U'}

def validate(obj,root=ROOT):
 if not isinstance(obj,dict):return ['Root is not an object']
 missing=REQUIRED-obj.keys();errors=[f'Missing: {sorted(missing)}'] if missing else []
 if obj.get('status') not in ALLOWED:errors.append('Invalid evidence status')
 if obj.get('status')=='T-REA' and not all(obj.get(k) for k in ('rea_version','command','exit_code','observed_at','limitations')):
  errors.append('T-REA requires runtime evidence fields')
 if not isinstance(obj.get('source'),str):errors.append('Missing source path');return errors
 # Source is a single local file. A URL without a local artifact cannot claim T-local.
 src=obj['source']
 if pathlib.PurePath(src).is_absolute() or '..' in pathlib.PurePath(src).parts or src.startswith(('http://','https://')):errors.append('Unsafe source path');return errors
 target=(root/src).resolve()
 if not target.is_relative_to(root.resolve()) or not target.is_file():errors.append('Source file not found');return errors
 digest=hashlib.sha256(target.read_bytes()).hexdigest()
 if obj.get('sha256')!=digest:errors.append('SHA256 does not match source')
 if not str(obj.get('result','')).strip():errors.append('Result must state a concrete observable fact')
 for key,value in obj.items():
  if isinstance(value,str) and re.search(r'(?i)(?:sk-[a-z0-9]{24,}|authorization:\s*bearer\s+\w+|-----begin private key-----)',value):
   errors.append('Possible credential in '+key)
 return errors

def main():
 if len(sys.argv)!=2:raise SystemExit('Usage: validate_evidence.py manifest.json')
 x=json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
 errs=validate(x)
 if errs:
  print('ERROR: '+'; '.join(errs),file=sys.stderr)
  raise SystemExit(1)
 print('Evidence manifest validated. This does not independently establish that REA ran.')
if __name__=='__main__':main()
