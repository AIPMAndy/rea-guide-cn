# REA 自带合法实验样本：Mini App

这是专门编写的 JavaScript 教学样例，源码完全公开，没有账号、真实客户、第三方私有程序或网络连接。

## 1. 运行本地行为基线

```bash
cd examples/mini-app
node test.mjs
```

预期结果：`5 self-owned fixture tests passed`。这一步只验证 **我们自己的 JS 程序**，不意味着 REA 已经运行。

## 2. 通过 REA 对源码目录做静态调查

先确认你安装并配置了 REA；回项目根目录，使用**绝对路径**：

```bash
npx -y rea-agents@latest analyze-javascript-application /absolute/path/to/rea-guide-cn/examples/mini-app --json
```

该命令及参数来自 REA 上游 README。别把示例路径字面复制进终端；按实际目录替换。

## 3. 应该调查什么

- `src/index.js` 导出 `summarizeOrder`。
- `src/order.js` 调用 `clampQuantity` / `discountRate` / `roundCurrency`。
- 会员且订单小计大于等于 100 才有 10% 折扣。
- 输入的负数单价和非整数数量会抛出异常。

将 **REA 静态分析实际结果** 与这张已知真值表对照；缺少的信息标注“工具未检出”。

## 4. 对抗式审核

首先，模块依赖不等于某一次运行的函数调用；其次，程序里不存在 Electron IPC 也属于合理结果。最后，本例不能推断任何第三方商业程序也有相同规则。
