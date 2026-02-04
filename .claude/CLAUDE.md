# Claude Code Chinese Commentary Collection

## 项目背景信息

本项目是 Anthropic 与 Claude Code 中文指南合集，专注于技术文档的翻译。项目包含 Claude Code 更新日志的双语对照版本以及 Anthropic 工程博客文章的中文翻译，旨在为中文开发者提供高质量的 AI 辅助编程工具指南。

## 目录结构

```
Claude Code Chinese Commentary Collection/
├── .claude/                                    # Claude Code 配置目录
│   ├── commands/                              # 自定义命令
│   ├── rules/                                 # 项目规则
│   │   └── translation-format.md              # 翻译格式规范
│   ├── CLAUDE.md                              # 项目提示词
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
├── README.md                                  # 项目说明文档
├── CHANGELOG.md                               # 项目更新日志
├── TASKS.json                                 # 阶段性任务清单
└── LAST_CLAUDE_PROGRESS.md                    # 上一次工作进度记录
```

## 技术栈与技术路线

- **工作方式**：中文翻译，双语对照格式
- **术语管理**：维护 `.claude/rules/translation-format.md` 格式规范
- **版本控制**：`anthropic-engineering-articles/` 为独立 Git 仓库
- **翻译流程**：使用翻译请求模板，遵循格式规范
- **质量保证**：Codex 审查协作机制
- **更新跟进**：通过自定义命令持续跟进 Claude Code 新版本

## 当前状态

**翻译完成期** 🎉

项目已完成所有 18 篇 Engineering 文章的翻译工作，文章编号统一为 ID 01-18。

**已完成**：
- [x] 翻译 18/18 篇文章（100%）
- [x] 文章编号统一为 01-18
- [x] 创建翻译格式规范 `.claude/rules/translation-format.md`
- [x] 建立 Codex 审查协作机制
- [x] 统一所有文章排版风格

**项目里程碑**：
- 🎉 所有 Engineering 文章翻译完成！
- 📚 涵盖智能体、上下文检索、MCP、Agent SDK 等核心技术
- 📐 排版格式全部统一

## 工作阶段

### 阶段 1: 翻译准备期
- [x] 创建项目结构
- [x] 制定翻译格式规范
- [x] 建立 Codex 审查协作机制

### 阶段 2: 翻译执行期
- [x] ID 01: Contextual Retrieval（上下文检索）
- [x] ID 02: Building Effective Agents（构建有效的智能体）
- [x] ID 03: SWE-bench Sonnet（SWE-bench 基准测试）
- [x] ID 04: The "think" tool（"think" 工具）
- [x] ID 05: Claude Code Best Practices（Claude Code 最佳实践）
- [x] ID 06: Multi-Agent Research System（多智能体研究系统）
- [x] ID 07: Desktop Extensions（桌面扩展）
- [x] ID 08: Writing Tools（写作工具）
- [x] ID 09: Postmortem（问题复盘）
- [x] ID 10: Context Engineering（上下文工程）
- [x] ID 11: Agent SDK（Agent SDK）
- [x] ID 12: Agent Skills（Agent 技能）
- [x] ID 13: Claude Code Sandboxing（Claude Code 沙盒）
- [x] ID 14: Code Execution with MCP（使用 MCP 执行代码）
- [x] ID 15: Long-Running Agents（长运行智能体）
- [x] ID 16: Advanced Tool Use（高级工具使用）
- [x] ID 17: Demystifying Evals（评估详解）
- [x] ID 18: AI Resistant Evaluations（AI 抗拒性评估）

### 阶段 3: 翻译完成期
- [x] 文章编号统一为 01-18
- [x] 排版风格统一（标题、粗体、双语格式）
- [ ] 持续跟进 Claude Code 新版本更新
- [ ] 根据需要翻译新的 Engineering 文章
- [ ] 完善项目文档和总结

### 注意事项
- 新翻译文章应直接遵循 `.claude/rules/translation-format.md` 规范
- 翻译完成后可请求 Codex 审查确保质量

## 资源

- [Claude Code GitHub](https://github.com/anthropics/claude-code)
- [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- [Anthropic Engineering Blog](https://www.anthropic.com/engineering)
