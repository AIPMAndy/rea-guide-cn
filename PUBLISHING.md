# 把 rea-guide-cn 发布到 GitHub 和 Pages

> 预定的独立开源仓库：`AIPMAndy/rea-guide-cn`，目前在 GitHub 创建之前不应当作已上线地址。

## 第一步：创建空仓库

打开 https://github.com/new ，Owner 选择 `AIPMAndy`，Repository name 输入 `rea-guide-cn`，选择 Public。建议不要勾选自动 README、.gitignore 或 License（本项目已经有）。

## 第二步：推送全部文件

解压 `rea-guide-cn-release-v5.zip` 后，在包含 README.md 的根目录打开终端：

```bash
git init -b main
git add .
git commit -m "feat: publish REA Chinese field guide v5"
git remote add origin https://github.com/AIPMAndy/rea-guide-cn.git
git push -u origin main
```

以上需要你具备目标仓库的写入权限，可能通过 GitHub 凭证或 SSH 完成。**若同名仓库后来已有其他代码，先比较并处理冲突，禁止强制覆盖。**

## 第三步：启用网站

仓库 Settings → Pages → Build and deployment → Source 选择 GitHub Actions。工作流 `.github/workflows/pages.yml` 会先运行校验，再将项目部署到 Pages。

发布完成地址应为 `https://aipmandy.github.io/rea-guide-cn/`；只有 GitHub `deploy` 状态 success 且实际页面可访问，才能在公开内容中声称“官网上线”。

## 第四步：对外展示前复核

- 桌面、iOS/Android：正文布局、复制、全文阅读页、官方能力筛选与进度勾选。
- `https://metaver.vip/` 与微信 `AIPMAndy` 入口正确。
- 所有研究案例都明确区分“官方资料”与“个人实际复现”。
- README 的双协议、上游 REA 地址与 Node 版本前提无误。
