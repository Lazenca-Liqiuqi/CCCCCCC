# Claude Code Chinese Commentary Collection

## 项目背景信息

本项目是 Anthropic 与 Claude Code 中文指南合集，专注于技术文档的翻译。项目包含 Claude Code 更新日志的双语对照版本以及 Anthropic 工程博客文章的中文翻译，旨在为中文开发者提供高质量的 AI 辅助编程工具指南。

## 目录结构

```
Claude Code Chinese Commentary Collection/
├── .claude/                                    # Claude Code 配置目录
├── anthropic-engineering-articles/            # Anthropic 工程文章翻译
├── Claude Code CHANGELOG - 双语对照.md        # Claude Code 更新日志双语版
├── CLAUDE.md                                  # 项目提示词（本文件）
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

**格式规范完善期**

项目已完成4篇Engineering文章的翻译（ID 19-16），并完成了格式规范制定和已翻译文章的格式修复工作。

**已完成**：
- ✅ 翻译 4/19 篇文章（21%）
- ✅ 修复 4/4 篇文章格式
- ✅ 创建翻译格式规范 `.claude/rules/translation-format.md`
- ✅ 建立 Codex 审查协作机制

**进行中**：
- 🔄 剩余 15 篇文章待翻译（ID 15-01，跳过 ID 01）

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

- [Claude Code GitHub](https://github.com/anthropics/claude-code)
- [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- [Anthropic Engineering Blog](https://www.anthropic.com/engineering)
