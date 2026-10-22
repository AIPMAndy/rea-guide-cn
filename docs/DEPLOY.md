# 发布到独立 GitHub 仓库

目标仓库：`AIPMAndy/rea-guide-cn`。不覆盖其他仓库，不直接向 `morluto/rea` 推送任何内容。

1. 在 https://github.com/new 创建 Public 仓库，名称 `rea-guide-cn`，最好不初始化 README。
2. 将此目录作为完整项目推到 `main`；此前跑 `python3 -m unittest discover -s tests -v`、`node examples/mini-app/test.mjs` 和 `python3 -m unittest discover -s examples/model-metadata -p "test_*.py" -v`。
3. GitHub 仓库 → Settings → Pages → Source 选择 **GitHub Actions**。
4. 推送成功后打开 Actions，确认 `validate` 和 `deploy` 都是 success。
5. 只有公开站点确实可以 HTTP 打开，才对外公布 `https://aipmandy.github.io/rea-guide-cn/`。
6. 若 Pages 报 `Get Pages site failed ... Not Found`，先检查 Pages Source 配置，不要误判为 HTML 报错。

本项目同时含 `.nojekyll`，可从 GitHub Pages 的项目子路径部署相对资源。
