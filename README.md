# Claude Code Chinese Commentary Collection

> Anthropic 与 Claude Code 中文指南合集

## 项目背景

Claude Code Chinese Commentary Collection 是一个专注于 Anthropic 技术文档中文翻译的项目。本项目为中文开发者提供高质量的 AI 辅助编程工具指南，包括：

- **Claude Code 更新日志**：双语对照版本，及时跟踪最新功能更新
- **Anthropic 工程文章**：深入理解 AI 代理、上下文工程、MCP 协议等核心技术

项目致力于降低中文开发者学习 Anthropic 技术栈的门槛，促进 AI 辅助编程的普及与应用。

## 目录结构

```
Claude Code Chinese Commentary Collection/
├── .claude/                                    # Claude Code 配置目录
│   ├── commands/                              # 自定义命令
│   ├── terminology.md                         # 翻译术语表
│   └── translate_request.md                   # 翻译请求模板
├── anthropic-engineering-articles/            # Anthropic 工程文章翻译（独立 Git 仓库）
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
├── CLAUDE.md                                  # 项目提示词
├── README.md                                  # 项目说明文档（本文件）
├── CHANGELOG.md                               # 项目更新日志
├── TASKS.json                                 # 阶段性任务清单
└── LAST_CLAUDE_PROGRESS.md                    # 上一次工作进度记录
```

### 目录说明

- **`.claude/`**：Claude Code 工作配置，包含术语表、翻译模板和自定义命令
- **`anthropic-engineering-articles/`**：Anthropic 官方工程博客文章的中文翻译
- **`Claude Code CHANGELOG - 双语对照.md`**：Claude Code 官方更新日志的双语对照版本
- **项目记忆文件**：`CLAUDE.md`、`README.md`、`CHANGELOG.md`、`TASKS.json`、`LAST_CLAUDE_PROGRESS.md`

## 技术栈与技术路线

### 翻译工作流程

1. **术语管理**：维护 `.claude/terminology.md` 确保翻译一致性
2. **翻译模板**：使用 `.claude/translate_request.md` 规范翻译请求
3. **双语对照**：采用原文与译文对照的格式，便于理解与学习
4. **质量保证**：遵循术语表，确保专业术语翻译的准确性

### 版本控制

- **独立仓库**：`anthropic-engineering-articles/` 为独立 Git 仓库
- **版本跟踪**：每个翻译文章独立提交，便于版本管理与回溯
- **更新跟进**：通过自定义命令持续跟进 Claude Code 新版本

## 当前状态

**格式规范完善期**

项目已完成4篇Engineering文章的翻译（ID 19-16），并完成了格式规范制定和已翻译文章的格式修复工作。

### 已完成内容

- **翻译 4/19 篇文章**（21%）
  - ID 19: Designing AI Resistant Technical Evaluations
  - ID 18: Demystifying Evals for AI Agents
  - ID 17: Introducing Advanced Tool Use
  - ID 16: Effective Harnesses for Long-Running Agents

- **格式修复 4/4 篇文章**（100%）
  - 修复正文段落空行问题
  - 修复标题格式（使用 `|` 分隔符）
  - 修复代码块、列表、链接、表格等问题

- **创建翻译格式规范**
  - 文件：`.claude/rules/translation-format.md`
  - 包含：标题、正文、列表、图片、表格、代码块、链接等格式规范
  - 基于实际修复经验的常见问题清单
  - 质量检查清单

- **建立 Codex 审查协作机制**
  - 审查请求模板：`.claude/review-request.md`
  - 审查报告：`.claude/review-report.md`

### 待进行内容

- **翻译剩余 15 篇文章**（ID 15-01，跳过 ID 01）
- 持续跟进 Claude Code 新版本更新

## TODO

### 翻译任务
- [ ] 翻译 ID 15: Code Execution with MCP
- [ ] 翻译 ID 14: Claude Code Sandboxing
- [ ] 翻译 ID 13: Agent Skills
- [ ] 翻译 ID 12: Agent SDK
- [ ] 翻译 ID 11: Context Engineering
- [ ] 翻译 ID 10: Postmortem
- [ ] 翻译 ID 09: Writing Tools
- [ ] 翻译 ID 08: Desktop Extensions
- [ ] 翻译 ID 07: Multi-Agent Research
- [ ] 翻译 ID 06: Claude Code Best Practices
- [ ] 翻译 ID 05: Think Tool
- [ ] 翻译 ID 04: SWE-Bench
- [ ] 翻译 ID 03: Building Effective Agents
- [ ] 翻译 ID 02: Contextual Retrieval
- [ ] 跳过 ID 01: 重复文章

### 注意事项
- 新翻译文章应直接遵循 `.claude/rules/translation-format.md` 规范
- 翻译完成后可请求 Codex 审查确保质量

## 资源

### 官方资源

- [Claude Code GitHub](https://github.com/anthropics/claude-code)
- [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- [Anthropic Engineering Blog](https://www.anthropic.com/engineering)
- [Anthropic 官方文档](https://docs.anthropic.com/)

### 相关工具

- [Claude Code CLI](https://github.com/anthropics/claude-code)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [Claude Agent SDK](https://docs.anthropic.com/en/docs/build-with-claude/agents)

## 版本

**当前版本**：0.1.0

详见 [CHANGELOG.md](./CHANGELOG.md)

## 贡献

欢迎提交 Issue 和 Pull Request 来改进本项目！

## 许可

本项目翻译内容遵循原文许可协议。原文版权归 Anthropic 所有。
