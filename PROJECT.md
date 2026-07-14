# MAC 管家（MAC Butler）

> 项目状态文件（Project Status）
>
> 每次开始新对话，请先阅读本文件。

---

# 当前版本

V0.1（开发中）

---

# 产品定位

MAC 管家是一款专注于 **Mac 空间管理** 的轻量级工具。

目标不是替代 CleanMyMac，而是帮助用户：

- 一键体检
- 一键清理安全项
- 空间不足提醒

坚持：

✅ 优先系统工具

✅ 优先终端

✅ 优先应用自身清理

✅ 不删除高风险目录

---

# 当前目录

```
MacButler
├── app
│   └── main.py
├── modules
│   ├── disk.sh
│   └── chrome.sh
├── reports
├── README.md
├── PROJECT.md
└── mac-health.sh
```

---

# 当前完成

## 项目

- [x] 建立项目目录
- [x] Git 初始化
- [x] First Commit
- [x] VS Code 开发环境

---

## Python

- [x] main.py
- [x] 调用 Shell 模块

---

## Shell 模块

- [x] Disk
- [x] Chrome
- [x] 飞书
- [x] 微信

---

# 当前可以运行

Terminal：

```bash
cd ~/Documents/MacButler/app
python3 main.py
```

输出：

- Disk 检查
- Chrome 检查

---

# 下一步（Sprint 2）

准备开发：

- [ ] WPS 检查

之后：

- [ ] 一键体检

再之后：

- [ ] 一键安全清理

最后：

- [ ] 菜单栏 App

---

# 开发规范

开发流程：

Terminal

↓

VS Code

↓

Terminal 测试

↓

Git Commit

---

每新增一个模块：

1. 创建 shell 模块

2. main.py 注册模块

3. 测试

4. Git Commit

---

# Git

当前状态：

- Git 已初始化

- 已完成第一次 Commit

GitHub：

用户名：

jiemei919

---

# 与 ChatGPT 协作方式

每次开始新的聊天：

请先阅读 PROJECT.md。

然后继续开发，不需要重新介绍项目。

回答要求：

- 一次只做一步
- 明确告诉我：
  - 在哪里操作（VS Code 或 Terminal）
  - 为什么这样做
  - 如何验证成功
- 不一次给很多步骤
- 优先保证项目稳定