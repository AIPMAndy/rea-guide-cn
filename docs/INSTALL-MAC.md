# Mac + Codex 保姆级安装

适用 macOS，REA 官网声明 macOS 12 或更高版本为支持环境之一；安装前以当前项目 README 对应版本为准。

## 第 1 步：只读检查

```bash
uname -a
node --version
npm --version
```

REA 上游当前 README 说明 Node 22.19+、Node 24.11+，或 Node 26+；不能将 Node 22 的任何小版本都当成达标。不满足就先升级 Node，别直接跳过检查。

## 第 2 步：显示 REA 的安装计划

```bash
npx rea-agents@latest setup
```

在选择列表里选 Codex；检查所有将改动的配置路径、额外组件和备份方案。**不要盲目全选**。REA 可以不安装 Hopper，JS 静态分析无需原生引擎。

## 第 3 步：重启 Codex 并核验

```bash
npx -y rea-agents@latest doctor --json
```

请让 Codex 显示它实际发现的 MCP 工具；如果没出现，检查配置、客户端作用域和是否真正重启。

## 第 4 步：用自己的 Mini App 试验

```bash
cd examples/mini-app
node test.mjs
```

再按 [实验说明](../examples/mini-app/README.md) 执行 REA 的 JS 静态分析。注意 `npx` 的首次运行可能联网下载安装包，需要按提示审批。

## 常见坑

- `node v22.16.0` 不满足本指南核查时 22.x 的最低补丁版本。
- 未重新启动 Codex，旧会话可能仍没有加载新 MCP。
- 配了 REA，但没有 Ghidra，Native 分析不会因此自动可用。
- 读取绝对路径里的账号/个人信息前，请检查最小授权。
