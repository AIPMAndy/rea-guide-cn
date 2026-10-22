# 参与贡献

欢迎教程更正、命令复测、跨平台安装实录和实验样例。请先读 [安全说明](docs/SAFETY.md)。

提交需要：目标自有/授权声明；操作系统/REA 版本/Node 版本；原始命令和状态；证据（脱敏）；预期与实际；是否真实 REA 运行；反证及复测步骤。

禁止上传受限二进制、未授权源码、真实 Cookie/Token、个人信息、收费分析器许可证和破解教程。

建议 PR 写成：事实变化 → 官方依据 → 对用户的影响 → 最小复现 → 自动测试。所有官方命令变更要核对上游最新正式发布，而不只看 main。

## V5 提交真实实测记录（必须满足）

提交前阅读 [证据等级](docs/PROVENANCE.md) 和 [实验基准](docs/BENCHMARK.md)。Issue/PR 应包含：目标许可与匿名化范围、REA + Node + provider 版本、完整只读命令、退出码、源文件 Hash、实际 Evidence 摘要、反证实验、系统和复测日期。**没有真实 REA 输出的内容一律标 E / O，不写 T-REA。**

修改 Markdown 后请运行 `python3 tools/build_pages.py` 更新静态网页、站点地图，再运行完整单测。维护者本地需要 `mistune` 与 `beautifulsoup4`；网页用户不需要安装 Python。

```bash
python3 -m unittest discover -s tests -v
python3 -m unittest discover -s examples/model-metadata -p 'test_*.py' -v
node examples/mini-app/test.mjs
```

公开提问时禁止粘贴访问令牌、会话 Cookie、第三方私有源码、客户文档或完整 HAR。
