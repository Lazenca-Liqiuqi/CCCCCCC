# Claude Code Chinese Commentary Collection

## 项目背景信息

本项目是 Anthropic 与 Claude Code 中文指南合集，专注于技术文档的翻译。项目包含 Claude Code 更新日志的双语对照版本以及 Anthropic 工程博客文章的中文翻译，旨在为中文开发者提供高质量的 AI 辅助编程工具指南。

## 目录结构

```
Claude Code Chinese Commentary Collection/
├── .claude/                                    # Claude Code 配置目录
│   ├── commands/                              # 自定义命令
│   │   └── fetch-cc-changelog.md              # 获取 Claude Code 更新日志
│   ├── terminology.md                         # 翻译术语表
│   └── translate_request.md                   # 翻译请求模板
├── anthropic-engineering-articles/            # Anthropic 工程文章翻译
│   ├── 01-contextual-retrieval.md             # 上下文检索技术
│   ├── 02-building-effective-agents.md        # 构建有效代理
│   ├── 04-claude-code-best-practices.md       # Claude Code 最佳实践
│   ├── 06-how-we-built-our-multi-agent-research-system.md  # 多代理研究系统
│   ├── 08-a-postmortem-of-three-recent-issues.md  # 三个问题的复盘
│   ├── 09-effective-context-engineering-for-ai-agents.md  # AI 代理上下文工程
│   ├── 10-building-agents-with-the-claude-agent-sdk.md   # 使用 Agent SDK 构建代理
│   ├── 11-equipping-agents-for-the-real-world-with-agent-skills.md  # 为现实世界装备代理技能
│   ├── 13-code-execution-with-mcp.md          # 使用 MCP 执行代码
│   └── 15-effective-harnesses-for-long-running-agents.md  # 长运行代理的有效控制
├── Claude Code CHANGELOG - 双语对照.md        # Claude Code 更新日志双语版
├── CLAUDE.md                                  # 项目提示词（本文件）
├── README.md                                  # 项目说明文档
├── CHANGELOG.md                               # 项目更新日志
├── TASKS.json                                 # 阶段性任务清单
└── LAST_CLAUDE_PROGRESS.md                    # 上一次工作进度记录
```

## 技术栈与技术路线

- **工作方式**：中文翻译，双语对照格式
- **术语管理**：维护 `.claude/terminology.md` 确保翻译一致性
- **版本控制**：`anthropic-engineering-articles/` 为独立 Git 仓库
- **翻译流程**：使用翻译请求模板，遵循术语表规范
- **更新跟进**：通过自定义命令持续跟进 Claude Code 新版本

## 当前状态

- **已完成**：10 篇 Anthropic 工程文章翻译
- **已完成**：CHANGELOG 双语对照已更新至 2.1.12 版本
- **待完成**：待翻译版本 2.1.6, 2.1.5, 2.1.4, 2.1.3, 2.1.2

## TODO

- [ ] 完成待翻译版本（2.1.6, 2.1.5, 2.1.4, 2.1.3, 2.1.2）的更新日志翻译
- [ ] 持续跟进 Claude Code 新版本的更新日志翻译
- [ ] 补充更多 Anthropic 工程文章翻译

## 资源

- [Claude Code GitHub](https://github.com/anthropics/claude-code)
- [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- [Anthropic Engineering Blog](https://www.anthropic.com/engineering)
