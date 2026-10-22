# REA V5 发布与排障

> 2026-10-22：独立公共 GitHub 仓库 `AIPMAndy/rea-guide-cn` 已完成 177 文件发布，源码检查通过。GitHub Pages 仍待管理员启用。

## 状态

- 开源仓库：https://github.com/AIPMAndy/rea-guide-cn
- `main` 分支的源码及 72 个静态阅读页均已提交。
- 工作流 `.github/workflows/pages.yml` 包含内容完整性、Node 原创案例、合成模型、Evidence 验证与 Pages 部署。
- 最近一次 `validate` 检测为 success；`deploy` 由于 Pages 没有启用，卡在 `configure-pages`。

## 启用 Pages

1. 打开 https://github.com/AIPMAndy/rea-guide-cn/settings/pages
2. 在 Build and deployment / Source 选择 **GitHub Actions** 并保存。
3. 打开 https://github.com/AIPMAndy/rea-guide-cn/actions ，重运行失败部署或触发 `pages.yml`。
4. 确认 `validate` 和 `deploy` 都是 success。
5. 访问 https://aipmandy.github.io/rea-guide-cn/ ，测试首页、全文阅读、站内资源、移动端排版与微信复制。

如出现 `Create Pages site failed: Resource not accessible by integration`，原因是 GitHub Actions token 没有管理员创建 Pages 站点的权限。请先在仓库 Pages 设置中由管理员启用，**不要反复修改首页代码**。

## 本地测试

```bash
python3 -m unittest discover -s tests -v
node examples/mini-app/test.mjs
python3 -m unittest discover -s examples/model-metadata -p 'test_*.py' -v
python3 tools/validate_evidence.py examples/mini-app/evidence-manifest.json
```

本项目不向上游 `morluto/rea` 推送，也不应当声称官方背书。
