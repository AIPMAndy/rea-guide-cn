# 自有样例：safetensors 格式头部检查（不是 REA 真实运行）

这个例子只用 Python 标准库创建并检查一个小型、无真实模型权重的 **safetensors 结构示例**。与真实模型推理无关，也不保证完整实现 safetensors 规范。

```bash
python3 examples/model-metadata/make_fixture.py
python3 examples/model-metadata/inspect_header.py
python3 -m unittest discover -s examples/model-metadata -p 'test_*.py' -v
```

**验收**：应看到 synthetic_tensor，以及 8 字节长度与 JSON 元数据字段；截断文件必须报错。安装并核对 REA 的实际版本后，可选择用官方模型文件静态检查命令作第二次实验，再比对 Evidence。**本包没有声称运行过 REA 的模型文件分析。**

作者 AI 酋长 Andy · 微信 AIPMAndy · https://metaver.vip/
