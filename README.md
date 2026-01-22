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

### 已完成内容

- **16 篇 Anthropic 工程文章获取**：全部完成

- **16 篇文章内容修复**：全部完成
  - 文章01-04：添加26个链接
  - 文章05-08：添加2个链接+2个小节+2个作者信息+2张SVG图片+修复1个拼写错误
  - 文章09-12：添加11个链接+2个小节+3张SVG图片
  - 文章13-16：添加27个链接+4张图片+3个日期+1个标题

- **HTML到Markdown转换工具**：开发完成
  - 创建 `html_to_md.py` 转换脚本
  - 测试文章01转换成功（20,933字符）

- **CHANGELOG 双语对照**：已更新至 2.1.12 版本

### 待进行内容

- **HTML与Markdown内容比对**：使用转换工具批量验证16篇文章内容一致性
- **翻译16篇文章**：使用 Codex 协作翻译
- 持续跟进 Claude Code 新版本更新
- 补充更多 Anthropic 工程文章翻译

## TODO

1. **HTML与Markdown内容比对**：使用转换脚本批量转换HTML文件，与现有Markdown进行逐篇比对
2. **优化转换脚本**：修复有序列表编号、图片URL编码等问题
3. **翻译16篇文章**：使用 Codex 协作翻译所有文章
4. **质量检查**：执行自动化检查、术语一致性验证、人工审校
5. **Git提交**：完成所有修复和翻译的版本控制

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
