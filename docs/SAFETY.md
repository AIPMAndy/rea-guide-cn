# 安全与合法使用约束

**授权第一**：REA 适合软件保存、互操作、合法研究、软件自查与教育。只逆向自有、开源或已明确得到授权的对象。

禁止把本教程用于：未经授权访问账户、破解商业许可证、规避 DRM、批量收集私人数据、从真实环境提取密钥、窃取源码或发布第三方私有二进制。

## 红队 P0 检查

1. 安装前确认源自 `morluto/rea`、`rea.tools`、`rea-agents` npm；同名 Fork 不等于官方。
2. Setup 会修改 Agent 配置，展示 plan、备份位置和权限，再显式批准。
3. 第三方 Hopper、IDA、JEB 等工具有自己的许可证；REA 的 MIT 不自动覆盖它们。
4. 浏览器调试与动态观测可执行目标；在合法且隔离的测试环境运行。
5. HAR/PCAP/崩溃报告可能包含 token、用户信息、个人路径；脱敏后才可公开。
6. 对重建产物使用原创代码，并审查受限素材、品牌与协议，避免直接搬运商业源码。
7. 输出应区分观察、解释、推断和已复现行为。

参考：[REA 上游 Disclaimer](https://github.com/morluto/rea/blob/main/DISCLAIMER.md) 与 [REA 官方安装指南](https://github.com/morluto/rea/blob/main/docs/installation.md)。
