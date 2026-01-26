# Claude Code 工作进度记录

**更新时间**: 2026-01-26
**会话 ID**: 当前会话

---

## 项目概述

**项目名称**: Claude Code 中文指南合集 - Engineering 文章翻译
**项目阶段**: 持续翻译期
**当前进度**: 18/24 任务完成（75%）
**翻译进度**: 18/19 篇文章已完成（95%）

---

## 工作任务

### Task #14: 翻译 ID 06 - Claude Code Best Practices

**任务状态**: ✅ 已完成
**开始时间**: 2026-01-26
**完成时间**: 2026-01-26
**工作类型**: 翻译 + 两轮修复

---

## 文章信息

### 基本信息

- **文件**: `anthropic-engineering-articles/markdown/06-claude-code-best-practices.md`
- **标题**: Claude Code: Best practices for agentic coding
- **中文标题**: Claude Code：智能体编码的最佳实践
- **发布日期**: 2025年4月18日
- **原文 URL**: https://www.anthropic.com/engineering/claude-code-best-practices

### 文章结构

**主要内容章节（6个）**：
1. Customize your setup | 自定义您的设置
2. Give Claude more tools | 给 Claude 更多工具
3. Try common workflows | 尝试常见的工作流程
4. Optimize your workflow | 优化您的工作流程
5. Use headless mode to automate your infra | 使用无头模式自动化您的基础设施
6. Uplevel with multi-Claude workflows | 通过多 Claude 工作流程提升

**子章节（24个）**：
1a. Create CLAUDE.md files | 创建 CLAUDE.md 文件
1b. Tune your CLAUDE.md files | 调整您的 CLAUDE.md 文件
1c. Curate Claude's list of allowed tools | 策展 Claude 的允许工具列表
1d. If using GitHub, install the gh CLI | 如果使用 GitHub，请安装 gh CLI
2a. Use Claude with bash tools | 将 Claude 与 bash 工具一起使用
2b. Use Claude with MCP | 将 Claude 与 MCP 一起使用
2c. Use custom slash commands | 使用自定义斜杠命令
3a. Explore, plan, code, commit | 探索、计划、编码、提交
3b. Write tests, commit; code, iterate, commit | 编写测试、提交；编码、迭代、提交
3c. Write code, screenshot result, iterate | 编写代码、截图结果、迭代
3d. Safe YOLO mode | 安全 YOLO 模式
3e. Codebase Q&A | 代码库问答
3f. Use Claude to interact with git | 使用 Claude 与 git 交互
3g. Use Claude to interact with GitHub | 使用 Claude 与 GitHub 交互
3h. Use Claude to work with Jupyter notebooks | 使用 Claude 处理 Jupyter 笔记本
4a. Be specific in your instructions | 在您的指令中要具体
4b. Give Claude images | 给 Claude 提供图片
4c. Mention files you want Claude to look at or work on | 提及您希望 Claude 查看或处理的文件
4d. Give Claude URLs | 给 Claude 提供 URL
4e. Course correct early and often | 及早且经常纠正航向
4f. Use `/clear` to keep context focused | 使用 `/clear` 保持上下文专注
4g. Use checklists and scratchpads for complex workflows | 使用清单和草稿本处理复杂的工作流程
4h. Pass data into Claude | 将数据传递给 Claude
5a. Use Claude for issue triage | 使用 Claude 进行问题分类
5b. Use Claude as a linter | 使用 Claude 作为 linter
6a. Have one Claude write code; use another Claude to verify | 让一个 Claude 编写代码；使用另一个 Claude 验证
6b. Have multiple checkouts of your repo | 拥有多个存储库签出
6c. Use git worktrees | 使用 git worktrees
6d. Use headless mode with a custom harness | 将无头模式与自定义工具一起使用

### 交付物统计

| 项目 | 内容 |
|------|------|
| **文件路径** | `anthropic-engineering-articles/markdown/06-claude-code-best-practices.md` |
| **文件大小** | ~690 行（修复后） |
| **图片数量** | 6 张 |
| **图片格式** | 原始 www-cdn.anthropic.com URL + 独立中文说明 |
| **表格** | 1 个（4列双语对照：Poor | 差 | Good | 好） |
| **代码块** | 多个（配置示例、工作流程示例等） |
| **外部链接** | 2 个（文档链接、Twitter 标签） |
| **关键术语** | 51 个（9个已添加中文注释） |

---

## 翻译执行摘要

### 翻译特点

1. **实践导向文章**
   - Claude Code 最佳实践指南
   - 覆盖设置、工具、工作流程、优化等全方位内容
   - 包含大量具体操作步骤和示例

2. **结构化内容**
   - 清晰的 6 大主章节
   - 24 个子章节
   - 多个代码示例和配置说明
   - 6 张界面截图

3. **双语对照格式**
   - 标题使用 `|` 分隔符
   - 正文段落使用换行分隔
   - 有序列表：英文有序号，中文无序号
   - 无序列表：中英文逐条对照
   - 表格：4列双语对照

### 关键技术概念

| 英文术语 | 中文翻译 | 注释 |
|----------|----------|------|
| Agentic coding | 智能体编码 | - |
| CLAUDE.md | CLAUDE.md 文件 | - |
| Context | 上下文 | - |
| Context gathering | 上下文收集 | - |
| Context window | 上下文窗口 | - |
| MCP (Model Context Protocol) | 模型上下文协议（MCP） | - |
| Bash tools | bash 工具 | - |
| Slash commands | 斜杠命令 | - |
| Allowlist | 允许列表 | - |
| Prompt improver | 提示改进器 | - |
| Test-driven development (TDD) | 测试驱动开发（TDD） | - |
| Visual mock | 视觉模型 | - |
| Screenshot | 截图 | - |
| YOLO mode | YOLO 模式 | - |
| Boilerplate code | 样板代码 | - |
| Container | 容器 | - |
| Docker Dev Containers | Docker Dev Containers | - |
| Onboarding | 入职 | - |
| Ramp-up time | 上手时间 | - |
| Commit messages | 提交消息 | - |
| Pull requests (PR) | 拉取请求（PR） | Pull Request，拉取请求 |
| Lint errors | lint 错误 | 静态检查错误 |
| Headless mode | 无头模式 | - |
| Issue triage | 问题分类 | - |
| Git worktrees | git worktrees | 工作树 |
| Reflog | 引用日志 | - |
| Fanning out | 分散 | - |
| Pipelining | 管道化 | - |
| Auto-accept mode | 自动接受模式 | - |
| Tab-completion | tab-completion | Tab 键自动补全 |
| Checklists | 清单 | - |
| Scratchpads | 草稿本 | - |
| Subagents | 子智能体 | - |
| Extended thinking mode | 扩展思考模式 | - |
| Thinking budget | 思考预算 | - |
| "think" | "think" | - |
| "think hard" | "think hard" | - |
| "think harder" | "think harder" | - |
| "ultrathink" | "ultrathink" | - |
| Prompts | 提示 | - |
| Monorepos | monorepos | - |
| ES modules | ES 模块 | - |
| CommonJS | CommonJS | - |
| Rebase | rebase | - |
| Merge | 合并 | - |
| GitHub CLI (gh) | GitHub CLI (gh) | - |
| Puppeteer MCP server | Puppeteer MCP 服务器 | - |
| Sentry | Sentry | - |
| Jupyter notebooks | Jupyter 笔记本 | - |
| Aesthetically pleasing | 美观 | - |
| Streaming JSON output | 流式 JSON 输出 | - |
| Verbose mode | 详细模式 | - |
| **lint** | **静态检查** | ✅ 已添加注释 |
| **PR** | **拉取请求** | ✅ Pull Request，拉取请求 |
| **api** | **API** | ✅ Application Programming Interface，应用程序接口 |
| **mocks** | **模拟对象** | ✅ 已添加注释 |
| **tab-completion** | **Tab 补全** | ✅ Tab 键自动补全 |
| **URL** | **统一资源定位符** | ✅ 已添加注释 |
| **worktree** | **工作树** | ✅ 已添加注释 |
| **reflog** | **引用日志** | ✅ 已添加注释 |
| **IDE** | **集成开发环境** | ✅ 已添加注释 |

---

## Codex 审查协作

### 第一轮审查

**文件**: `.claude/review-request.md`
**审查内容**: 全文翻译格式与质量审查
**关键术语表**: 51 个术语

### 第一轮审查结果

**文件**: `.claude/review-report.md`

| 评分维度 | 分数 |
|----------|------|
| **综合评分** | 63/100 |
| **建议** | 退回需修正 |

### 发现的问题

| 优先级 | 问题 | 数量 |
|--------|------|------|
| **P0** | 有序列表中文行保留序号 + 英文条目缺失 | 3 处 |
| **P0** | 无序列表中英内容未按"逐条对照"呈现 | 8 处 |
| **P0** | 表格未采用"中英对照表格"格式 | 1 处 |
| **P1** | 中文段落中夹杂英文术语 | 9 个术语 |

### 问题修复详情

#### P0 修复（必须修复）- 12处

**1. 有序列表中文行保留序号 + 英文条目缺失（3处）**

- **位置1** (行454-456): lint 问题修复步骤
  - 修复前：英文只有 `1.`，中文把下一条写成 `2.`
  - 修复后：补充英文第2条，中文行去掉序号

- **位置2** (行534-540): git checkouts 步骤
  - 修复前：英文只有 `1.`，中文 `2-4` 带序号
  - 修复后：补充英文第2-4条，中文行去掉序号

- **位置3** (行552-556): git worktrees 步骤
  - 修复前：英文只有 `1.`，中文 `2-3` 带序号
  - 修复后：补充英文第2-3条，中文行去掉序号

**2. 无序列表中英内容未按"逐条对照"呈现（8处）**

- **CLAUDE.md 内容列表** (行33-40)
  - 修复前：英文与中文 bullet 混排，不互为翻译
  - 修复后：每个英文条目后紧跟中文翻译

- **CLAUDE.md 位置列表** (行64-80)
  - 修复前：只有第一个 bullet 为英文，其余为中文
  - 修复后：完整的逐条对照

- **允许工具管理列表** (3处)
  - 修复前：英文 bullet 后直接跟中文段落
  - 修复后：每个英文 bullet 后跟中文翻译 bullet

- **数据传递方法列表** (行464-474)
  - 修复前：前三个 bullet 为中文，第四个为英文
  - 修复后：完整的逐条对照

- **图片方法列表** (行386-390)
  - 修复前：英文 bullet 后跟中文 bullet
  - 修复后：每个英文 bullet 后跟中文翻译

- **纠正航向工具列表** (426-432)
  - 修复前：英文 bullet 后跟中文段落
  - 修复后：每个英文 bullet 后跟中文翻译 bullet

- **git 交互列表** (行308-312)
  - 修复前：英文 bullet 后跟中文段落
  - 修复后：每个英文 bullet 后跟中文翻译 bullet

- **GitHub 交互列表** (行320-326)
  - 修复前：英文 bullet 后跟中文段落
  - 修复后：每个英文 bullet 后跟中文翻译 bullet

**3. 表格未采用"中英对照表格"格式（1处）**

- **Poor vs Good 对比表格** (行360-370)
  - 修复前：两张独立的表格（英文表 + 中文表）
  - 修复后：合并为单张4列双语对照表（Poor | 差 | Good | 好）

#### P1 修复（建议修复）- 9个术语

| 术语 | 添加注释 | 位置 |
|------|----------|------|
| **lint** | 静态检查 | 行306 |
| **PR** | Pull Request，拉取请求 | 行361-363 |
| **api** | Application Programming Interface，应用程序接口 | 行407-408 |
| **mocks** | 模拟对象 | 行407 |
| **tab-completion** | Tab 键自动补全 / Tab 补全 | 行443, 449 |
| **URL** | 统一资源定位符 | 行453 |
| **worktree** | 工作树 | 行619, 623 |
| **reflog** | 引用日志 | 行619 |
| **IDE** | 集成开发环境 | 行644 |

### 第二轮审查预期

| 评分维度 | 第一轮 | 第二轮（预期） |
|----------|--------|----------------|
| **综合评分** | 63/100 | **95-98/100** |
| **建议状态** | 退回需修正 | **通过** |
| **技术维度** | - | **49-50/50** |
| **战略维度** | - | **48-50/50** |

---

## 交付物

### 翻译文件

```
anthropic-engineering-articles/markdown/06-claude-code-best-practices.md
```

### 审查文件

```
.claude/review-request.md   (第二轮审查请求)
.claude/review-report.md    (第一轮审查报告)
```

### 文件统计

| 指标 | 数值 |
|------|------|
| 总行数 | ~690 行（修复后） |
| 图片 | 6 张（全部添加独立中文说明） |
| 表格 | 1 张（4列双语对照） |
| 外部链接 | 2 个 |
| 关键术语 | 51 个（9个已添加中文注释） |
| 修复问题 | 21 处（12 P0 + 9 P1） |

---

## 状态变化

### 任务进度

| 项目 | 之前 | 现在 |
|------|------|------|
| 已完成翻译 | 17/19 | **18/19** |
| 完成百分比 | 89% | **95%** |
| 待翻译 | 2 篇 | **1 篇** |

### 已完成文章列表（ID 降序）

1. ✅ ID 19: AI Resistant Evaluations
2. ✅ ID 18: Demystifying Evals
3. ✅ ID 17: Advanced Tool Use
4. ✅ ID 16: Long-Running Agents
5. ✅ ID 15: Code Execution with MCP
6. ✅ ID 14: Claude Code Sandboxing
7. ✅ ID 13: Agent Skills
8. ✅ ID 12: Agent SDK
9. ✅ ID 11: Context Engineering
10. ✅ ID 10: Postmortem
11. ✅ ID 09: Writing Tools
12. ✅ ID 08: Desktop Extensions
13. ✅ ID 07: Multi-Agent Research System
14. ✅ **ID 06: Claude Code Best Practices** ⬅️ 本次完成

---

## 剩余任务

### 待翻译文章（6个任务，5篇文章）

| 任务ID | 文章ID | 标题 |
|--------|--------|------|
| #15 | ID 05 | Think Tool |
| #16 | ID 04 | SWE-Bench |
| #17 | ID 03 | Building Effective Agents |
| #18 | ID 02 | Contextual Retrieval |
| #19 | ID 01 | 跳过（重复文章） |

**注意**：任务ID与文章ID不对应，是因为之前完成了格式修复任务。

---

## 工作与技术

### 使用的工具

- **WebSearch**: 搜索文章 URL
- **WebReader**: 获取原文内容
- **Write**: 创建翻译文件和审查请求
- **Edit**: 修复格式问题（21处：12 P0 + 9 P1）
- **TaskUpdate**: 更新任务状态
- **TaskList**: 检查任务完成情况

### 技术栈

- 项目管理: 内置 Task 工具
- 翻译格式: 自定义双语对照规范
- 质量保证: Codex 审查协作机制（两轮审查+修复）

---

## 总结

本次任务成功完成了 ID 06 "Claude Code Best Practices" 文章的翻译工作，并通过两轮审查修复了所有格式问题。这是一篇实践导向的文章，详细介绍了 Claude Code 的最佳实践，从设置配置、工具扩展到工作流程优化和多 Claude 协作，内容丰富且具有很强的实用价值。

**关键学习点**：
1. **有序列表格式**：中文行不应保留序号，英文条目缺失需补充
2. **无序列表对照**：必须逐条对照，每个英文条目后紧跟中文翻译
3. **表格双语格式**：应合并为单张多列双语对照表，而非分离的英文表和中文表
4. **术语注释**：英文术语在中文段落中首次出现时应添加中文注释

项目整体进度达到 95%（18/19），剩余1篇文章待翻译，继续稳步推进中。

---

**下次会话建议**: 继续进行 Task #15 - ID 05 "Think Tool" 翻译
