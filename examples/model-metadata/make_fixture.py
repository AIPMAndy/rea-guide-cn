"""Create a synthetic safetensors-format header for teaching only. No model data or private bytes."""
import json,struct,pathlib
ROOT=pathlib.Path(__file__).resolve().parent
HEADER={"synthetic_tensor":{"dtype":"F32","shape":[1],"data_offsets":[0,4]},"__metadata__":{"source":"rea-guide-owned-synthetic"}}
payload=json.dumps(HEADER,ensure_ascii=False,separators=(',',':')).encode('utf8')
(ROOT/'synthetic.safetensors').write_bytes(struct.pack('<Q',len(payload))+payload+struct.pack('<f',1.25))
print('Created synthetic.safetensors (one float; not a trained model)')
