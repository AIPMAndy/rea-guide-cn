"""Offline header inspection demo, NOT a REA runner or a full safetensors validator."""
import json,struct,pathlib,sys
p=pathlib.Path(sys.argv[1] if len(sys.argv)>1 else pathlib.Path(__file__).with_name('synthetic.safetensors'))
with p.open('rb') as f:
 size=p.stat().st_size
 if size<8:raise ValueError('missing 8-byte length')
 header_length=struct.unpack('<Q',f.read(8))[0]
 if not 0<header_length<=min(size-8,1024*1024):raise ValueError('invalid header length')
 header=json.loads(f.read(header_length))
 if not isinstance(header,dict):raise ValueError('invalid object')
 print(json.dumps({'header_size':header_length,'keys':list(header),'file_size':size},ensure_ascii=False,indent=2))
