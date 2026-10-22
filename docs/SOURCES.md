# 来源及证据分级｜核查于 2026-10-21

| 事实 | 来源 | 级别 | 边界 |
|---|---|---|---|
| REA 项目定位与受支持目标 | https://github.com/morluto/rea | O：上游 README | 主分支能力不必然已随 npm 发布 |
| 官网正式入口与推荐 setup 命令 | https://rea.tools/ | O：官方站 | setup 将请求用户批准 |
| 安装、最小版本、provider 和诊断 | https://github.com/morluto/rea/blob/main/docs/installation.md | O：官方安装文档 | 操作系统/版本限制依任务而异 |
| 详细工具目录与 Evidence | https://github.com/morluto/rea/blob/main/docs/cli.md | O：官方参考（请以该仓库当前实际目录核验文件位置） | 可能随新版变动 |
| Windows Calculator 百分号示例 | https://rea.tools/ | O：官网演示 | 本项目未在用户机器重跑 |
| 浏览器小恐龙速度示例 | https://rea.tools/ | O：官网演示 | 某实现特定常数，不泛化 |
| Mini App 会员折扣 | examples/mini-app/ | T-local：原创代码自带本地测试 | 与 REA 引擎实际执行是两类证据 |
| 教程中的其他研究任务 | guides/ 与 cases/ | E：教学实验方案 | 不代表已在你的设备执行 |

**O 官方 / T-local 作者当前容器本地测试 / T-REA 真实 REA 运行记录 / E 教学建议 / U 尚未验证**。

REA 持续迭代。对某个命令的精确可用性，除了官方文档，仍应以安装版本的 `--help` / `doctor` / 实际工具清单为准。不要用 GitHub Star 数量给功能质量背书。

## 2026-10-21 V5 官方能力矩阵增补

REA 官方仓库 `https://github.com/morluto/rea` 的 **What you can analyze** 表列出额外专项能力：Go/Rust 编译元数据、GPU code object、GGUF / safetensors、IL2CPP、Godot PCK、WASM、离线 EVM、SQLite/WAL、Android / ADB / Flutter、固件、网络包与日志、PyInstaller、运行时进程捕获等。完整分类和差异见 [CAPABILITIES.md](CAPABILITIES.md)。

- **来源类型 O（官方）**：https://github.com/morluto/rea#what-you-can-analyze
- **安装和辅助工具依赖 O**：https://github.com/morluto/rea/blob/main/docs/installation.md
- **CLI 与 Evidence 合约 O**：https://github.com/morluto/rea/blob/main/docs/cli.md
- **供应链与第三方工具法律边界 O**：https://github.com/morluto/rea/blob/main/DISCLAIMER.md
- **项目网站示例 O**：https://rea.tools/
- **自主本地验证 T-local**：[Mini App 原始测试](../examples/mini-app/test.mjs)、[合成模型头部测试](../examples/model-metadata/README.md)

**尚未采集 T-REA 真实运行证据**。原始 README 也明确提醒：某些新功能还可能未进入 npm 已发布版本；使用前应在用户机器核对已安装版本的帮助、能力列表和依赖。
