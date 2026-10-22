# 官方能力覆盖矩阵｜版本核查 2026-10-21

> 来源为 [REA 上游能力表](https://github.com/morluto/rea#what-you-can-analyze)，属于 O（官方陈述），不是 T-REA（真实执行）。请务必在本机检查 npm 发行版实际能力。

| 功能 | 专项要求或限制 | 独立教程 | 当前已实测？ |
|---|---|---|---|
| 桌面安装扫描 | 内置目录/文件头识别，内置只读功能，上游 README | [guides/25--.md](../guides/25--.md) | **否（O）** |
| Native 反编译 | Hopper / Ghidra / IDA，许可工具 + provider | [guides/10-native.md](../guides/10-native.md) | **否（O）** |
| Linux ELF 静态布局 | Linux x64 + 自带 pwntools，依官方子系统验证 | [guides/15-formats.md](../guides/15-formats.md) | **否（O）** |
| Go 构建元数据 | 静态 ELF/PE/Thin Mach-O，不需安装 Go | [guides/26-go-rust-.md](../guides/26-go-rust-.md) | **否（O）** |
| Rust 构建元数据 | cargo-auditable 嵌入信息，不是源码还原 | [guides/26-go-rust-.md](../guides/26-go-rust-.md) | **否（O）** |
| GPU Code Objects | PTX / CUBIN / ELF / PE，静态元数据，非运行 | [guides/27-gpu-code-objects.md](../guides/27-gpu-code-objects.md) | **否（O）** |
| GGUF/safetensors | 模型头部、tensor 声明，不推断模型性能 | [guides/28-gguf-safetensors.md](../guides/28-gguf-safetensors.md) | **否（O）** |
| Unity IL2CPP | global-metadata.dat 支持指定版本，不等于全部反编译 | [guides/29-il2cpp-metadata.md](../guides/29-il2cpp-metadata.md) | **否（O）** |
| Godot PCK | PCK 清单及受控提取，尊重资源版权 | [guides/30-godot-pck.md](../guides/30-godot-pck.md) | **否（O）** |
| WASM | 用户提供 WABT，版本约束核查 | [guides/31-wasm-artifact.md](../guides/31-wasm-artifact.md) | **否（O）** |
| 离线 EVM 字节码 | Linux x64 本地 carrier，只读、不发交易 | [guides/32-offline-evm.md](../guides/32-offline-evm.md) | **否（O）** |
| SQLite/WAL | Node 24.15+ 或 26+ 的原生 SQLite 限制，区别于通用 Node 门槛 | [guides/16-sqlite.md](../guides/16-sqlite.md) | **否（O）** |
| JavaScript/Electron | Node/npm；Linux 需 procps ps，静态模块图及 IPC | [guides/08-javascript-electron.md](../guides/08-javascript-electron.md) | **否（O）** |
| 网站观察 | Chrome 家族浏览器，动态需显式许可 | [guides/09-website.md](../guides/09-website.md) | **否（O）** |
| HAR/SAZ 网络记录 | 脱敏捕获记录，数据隐私高风险 | [guides/36-saved-captures.md](../guides/36-saved-captures.md) | **否（O）** |
| .NET | 静态元数据/CIL，不需原生反编译器 | [guides/14-dotnet.md](../guides/14-dotnet.md) | **否（O）** |
| Android APK | JDK + JADX，系统与许可依赖 | [guides/13-android.md](../guides/13-android.md) | **否（O）** |
| Android ADB | 用户提供 adb，设备权限需审批 | [guides/33-android-devices.md](../guides/33-android-devices.md) | **否（O）** |
| JEB 项目 | 用户运行并授权的 JEB MCP，受第三方许可 | [guides/13-android.md](../guides/13-android.md) | **否（O）** |
| Apktool 资源 | 用户提供 Apktool launcher，依官方版本而定 | [guides/13-android.md](../guides/13-android.md) | **否（O）** |
| Flutter APK | 静态 APK 元数据，不等于 Dart 源码 | [guides/34-flutter-metadata.md](../guides/34-flutter-metadata.md) | **否（O）** |
| 固件 | Linux Binwalk / Unblob，提取须核对许可 | [guides/35-firmware.md](../guides/35-firmware.md) | **否（O）** |
| PCAP/TShark | 用户提供 Tshark / capinfos，高度敏感的网络数据 | [guides/36-saved-captures.md](../guides/36-saved-captures.md) | **否（O）** |
| 逻辑信号 | Linux sigrok-cli + prlimit，只读记录 | [guides/36-saved-captures.md](../guides/36-saved-captures.md) | **否（O）** |
| PyInstaller | 静态 CArchive 元数据，不等于原始项目源码 | [guides/37-pyinstaller.md](../guides/37-pyinstaller.md) | **否（O）** |
| 运行时进程捕获 | Linux/macOS PTY，会执行目标，有副作用 | [guides/38-process-behavior.md](../guides/38-process-behavior.md) | **否（O）** |
| Apple bundle/资源 | plist 及签名或资源目录，导出限制依版权 | [guides/25--.md](../guides/25--.md) | **否（O）** |
| crash core | Linux x64 + 用户提供 pwntools，隐私与地址风险 | [guides/36-saved-captures.md](../guides/36-saved-captures.md) | **否（O）** |

## 上游并非所有功能都是全平台

- Linux 记录格式或插件常有专属依赖；例如部分离线 ELF/记录重放需要 Linux x64。
- SQLite 专项的 Node 要求可能比 REA 通用要求更高（上游称 Node 24.15+ 或 26+），不要直接套通用 22.19+。
- Android APK 的 JADX + 完整 JDK、WASM 的 WABT、native 的 Ghidra/Hopper/IDA 均有额外许可证和版本前提。
- 浏览器/进程/设备行为观察可能执行程序或读到私人信息，必须单独审批且隔离。
- 静态证据只是初步调查，不能推断完整功能或安全性。

作者 AI 酋长 Andy · 微信 AIPMAndy · https://metaver.vip/
