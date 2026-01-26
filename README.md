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
│   ├── rules/                                 # 项目规则
│   │   └── translation-format.md              # 翻译格式规范
│   └── review-request.md                      # 审查请求模板
├── anthropic-engineering-articles/            # Anthropic 工程文章翻译（独立 Git 仓库）
│   ├── 01-contextual-retrieval.md             # 上下文检索技术
│   ├── 02-building-effective-agents.md        # 构建有效智能体
│   ├── 03-swe-bench-sonnet.md                 # SWE-bench 基准测试
│   ├── 04-claude-think-tool.md                # "think" 工具
│   ├── 05-claude-code-best-practices.md       # Claude Code 最佳实践
│   ├── 06-multi-agent-research-system.md      # 多智能体研究系统
│   ├── 07-desktop-extensions.md               # 桌面扩展
│   ├── 08-writing-tools-for-agents.md         # 写作工具
│   ├── 09-a-postmortem-of-three-recent-issues.md  # 问题复盘
│   ├── 10-effective-context-engineering-for-ai-agents.md  # 上下文工程
│   ├── 11-agent-sdk.md                        # Agent SDK
│   ├── 12-agent-skills.md                     # Agent 技能
│   ├── 13-claude-code-sandboxing.md           # Claude Code 沙盒
│   ├── 14-code-execution-with-mcp.md          # 使用 MCP 执行代码
│   ├── 15-effective-harnesses-for-long-running-agents.md  # 长运行智能体
│   ├── 16-advanced-tool-use.md                # 高级工具使用
│   ├── 17-demystifying-evals-for-ai-agents.md # 评估详解
│   └── 18-AI-resistant-technical-evaluations.md  # AI 抗拒性评估
├── Claude Code CHANGELOG - 双语对照.md        # Claude Code 更新日志双语版
├── CLAUDE.md                                  # 项目提示词
├── README.md                                  # 项目说明文档（本文件）
├── CHANGELOG.md                               # 项目更新日志
├── TASKS.json                                 # 阶段性任务清单
└── LAST_CLAUDE_PROGRESS.md                    # 上一次工作进度记录
```

### 目录说明

- **`.claude/`**：Claude Code 工作配置，包含规则、翻译模板和审查请求
- **`anthropic-engineering-articles/`**：Anthropic 官方工程博客文章的中文翻译
- **`Claude Code CHANGELOG - 双语对照.md`**：Claude Code 官方更新日志的双语对照版本
- **项目记忆文件**：`CLAUDE.md`、`README.md`、`CHANGELOG.md`、`TASKS.json`、`LAST_CLAUDE_PROGRESS.md`

## 技术栈与技术路线

### 翻译工作流程

1. **术语管理**：维护 `.claude/rules/translation-format.md` 确保翻译一致性
2. **翻译模板**：使用 `.claude/review-request.md` 规范翻译请求
3. **双语对照**：采用原文与译文对照的格式，便于理解与学习
4. **质量保证**：遵循格式规范，确保专业术语翻译的准确性
5. **Codex 审查**：建立审查协作机制，保证翻译质量

### 版本控制

- **独立仓库**：`anthropic-engineering-articles/` 为独立 Git 仓库
- **版本跟踪**：每个翻译文章独立提交，便于版本管理与回溯
- **更新跟进**：通过自定义命令持续跟进 Claude Code 新版本

## 当前状态

**翻译完成期** 🎉

项目已完成所有 18 篇 Anthropic Engineering 文章的翻译工作，文章编号统一为 ID 01-18。

### 已完成内容

- **翻译 18/18 篇章**（100%）✅
  - ID 01: Introducing Contextual Retrieval（上下文检索）
  - ID 02: Building Effective Agents（构建有效的智能体）
  - ID 03: SWE-bench Sonnet（SWE-bench 基准测试）
  - ID 04: The "think" tool（"think" 工具）
  - ID 05: Claude Code Best Practices（Claude Code 最佳实践）
  - ID 06: Multi-Agent Research System（多智能体研究系统）
  - ID 07: Desktop Extensions（桌面扩展）
  - ID 08: Writing Tools（写作工具）
  - ID 09: A Postmortem of Three Recent Issues（问题复盘）
  - ID 10: Effective Context Engineering for AI Agents（上下文工程）
  - ID 11: Building Agents with the Claude Agent SDK（Agent SDK）
  - ID 12: Equipping Agents for the Real World with Agent Skills（Agent 技能）
  - ID 13: Claude Code Sandboxing（Claude Code 沙盒）
  - ID 14: Code Execution with MCP（使用 MCP 执行代码）
  - ID 15: Effective Harnesses for Long-Running Agents（长运行智能体）
  - ID 16: Introducing Advanced Tool Use（高级工具使用）
  - ID 17: Demystifying Evals for AI Agents（评估详解）
  - ID 18: Designing AI Resistant Technical Evaluations（AI 抗拒性评估）

- **文件编号统一**
  - 所有文章文件重编号为 01-18
  - Git 已识别为 rename 操作

- **创建翻译格式规范**
  - 文件：`.claude/rules/translation-format.md`
  - 包含：标题、正文、列表、图片、表格、代码块、链接等格式规范
  - 基于实际修复经验的常见问题清单
  - 质量检查清单

- **建立 Codex 审查协作机制**
  - 审查请求模板：`.claude/review-request.md`
  - 审查报告：`.claude/review-report.md`

### 项目里程碑

- 🎉 **所有 Engineering 文章翻译完成！**
- 📚 涵盖智能体、上下文检索、MCP、Agent SDK 等核心技术
- 🔄 文章编号统一规范

### 未来计划

- 持续跟进 Claude Code 新版本更新
- 根据需要翻译新的 Engineering 文章
- 完善项目文档和总结

## TODO

### 翻译任务
- ✅ 所有 18 篇 Engineering 文章翻译完成
- 🔄 持续跟进 Claude Code 新版本更新
- 📊 根据需要翻译新文章

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

**当前版本**：0.2.0

详见 [CHANGELOG.md](./CHANGELOG.md)

## 贡献

欢迎提交 Issue 和 Pull Request 来改进本项目！

## 许可

本项目翻译内容遵循原文许可协议。原文版权归 Anthropic 所有。
