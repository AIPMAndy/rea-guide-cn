# REA 命令速查（来自官方 README 与安装文档）

| 目的 | 命令 | 注意 |
|---|---|---|
| 规划并接入 Agent | `npx rea-agents@latest setup` | 会展示文件改动计划，需人工批准 |
| 诊断 | `npx -y rea-agents@latest doctor --json` | 分清全局与指定 scope |
| 检查 Ghidra provider | `rea doctor --provider ghidra --json` | REA CLI 要在 PATH、provider 应已安装 |
| 静态分析 JS 项目 | `npx -y rea-agents@latest analyze-javascript-application /absolute/path --json` | 自己的或已授权目录；静态分析不运行目标代码 |
| 已全局安装时查看命令 | `rea --help` | 精确参数以当前版本为准 |
| 全局 npm 安装 | `npm install --global rea-agents` | 与 npx 版本管理方式不同 |
| 更新已全局安装的版本 | `rea update` | 不自动替你刷新每个 Agent 注册 |
| 检查 Agent 单独注册 | `rea doctor --client codex --json` | 官方支持指定 scope |

不要凭网上过时文章手动修改一堆 JSON。对 Native、Android、WASM、抓包等专项用法，阅读最新官网文档并由当前工具 `--help` 确定参数。
