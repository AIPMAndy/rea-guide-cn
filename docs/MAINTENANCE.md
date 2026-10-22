# 项目维护与上游变更协议

**核心原则：文件数量不等于内容质量；每条动态能力必须有官方来源、发行版版本、复现状态和更新日期。**

## 每月定期核查

1. 阅读 `morluto/rea` 的最新 README、Release Notes 和 npm 包发行说明，记录发布时间和功能发布通道。
2. 核对 Node、系统支持、provider、`rea --help` 是否变化；未在安装版本中出现的能力不标可用。
3. 对有代码或参数变化的章节发布测试记录，保留旧版兼容信息；不要仅把 `latest` 替换成某个猜测版本。
4. 更新 `data/content.json`、`docs/CAPABILITIES.md`、`docs/SOURCES.md`、对应章节；随后重建 `pages/`。
5. CI 检查数量、站内路径、安全声明、原创样例、证据等级；再检查 GitHub Pages 的真实 URL。
6. 对 P0 安全问题优先处理：第三方权益、未授权数据处理、误报“逆向成功”、冒名官方。

## 数量以数据源为准

- `data/content.json` 是目录、提示词、案例与官方能力矩阵的唯一数据源。
- `tools/build_pages.py` 将 Markdown 预生成 HTML：输出由本项目维护、不会在访问时运行任何第三方依赖。
- CI 只执行本仓库原创测试，不尝试下载安装 REA 或运行未经授权程序。
- 所有线上未实测字段仍使用 O、E、U；只有真正的运行 Evidence 才能升级 T-REA。

## 发布条件

- GitHub repo 公开可读、LICENSE、文档许可与致谢完整。
- Actions `validate` / `deploy` 均成功；官网 HTTP 直接访问可用。
- 浏览器实际打开首页、章节链接、案例入口、搜索、移动端布局、微信复制。
- 完成之前不能说网站已经上线。

作者 AI 酋长 Andy · 微信 AIPMAndy · https://metaver.vip/
