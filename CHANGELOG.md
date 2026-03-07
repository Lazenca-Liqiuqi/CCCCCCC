# Changelog

本文档记录项目的重要变更。

格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，
版本号遵循 [语义化版本](https://semver.org/lang/zh-CN/)。

## Unreleased

### 变更

- **项目记忆体系迁移**：将当前工作记忆入口切换为 Codex 风格
  - 新增根目录 `AGENTS.md`
  - 新增根目录 `LAST_RUN.md`
  - 新增 `claude-code相关/anthropic-engineering-articles/AGENTS.md`
  - 停用旧的 `CLAUDE.md` / `LAST_CLAUDE_PROGRESS.md` 作为项目记忆入口

### 文档

- **README 同步**：更新为 `claude-code相关/` 与 `codex相关/` 的实际目录结构
- **记忆入口说明统一**：明确 `.claude/` 仅保留辅助配置与模板角色

## 0.2.1 2026-02-04 排版统一与项目记忆优化

### 变更

- **Engineering 文章排版统一**：统一 18 篇文章的双语对照格式规范
  - 移除 5 个文件中 17 处标题数字序号（`## 1. Title` → `## Title`）
  - 将约 360 处 `__text__` 粗体格式转换为 `**text**`（保留代码中的合法 `__` 序列）
  - 合并 10 处分两行标题为单行双语格式（使用 `|` 分隔符）
  - 影响文件：15 个（01, 07, 13 已符合规范无需修改）

- **Claude Code 更新日志同步**：同步至 2.1.25 版本
  - 更新 fetch-cc-changelog.md 命令描述
  - 新增 2.1.25-2.1.20 版本更新内容
  - 保持中英文双语对照格式

### 文档

- **项目记忆文件优化**：修复 `.claude/CLAUDE.md` 和 `README.md` 格式
  - 添加 `## 工作阶段` 章节，使用 Markdown TODO 语法（`[x]` / `[ ]`）
  - 更新目录结构，反映最新文件位置
  - 修正章节命名（`## 项目背景` → `## 项目背景信息`）
  - 统一 CHANGELOG.md 日期格式为 `YYYY-MM-DD`

- **子目录项目记忆文件**：创建 `anthropic-engineering-articles/CLAUDE.md`
  - 包含目录结构和 18 篇文章的文件信息
  - 每篇文章包含：标题、发布日期、内容概述、核心技术

### 修复

- **标题格式规范**：所有标题统一使用 `|` 分隔符的双语格式
- **粗体格式规范**：统一使用 `**text**` 而非 `__text__`

### 改进

- **格式一致性**：所有 18 篇文章遵循统一的双语对照格式规范
- **可维护性**：项目记忆文件结构更清晰，便于后续工作
- **验证通过率**：100%（带数字标题 0 处、`__` 格式 0 处、分两行标题 0 处）

---

## 0.2.0 2026-01-26 完成所有 Engineering 文章翻译

### 新增

- **翻译 18 篇 Engineering 文章**：完成全部 Anthropic Engineering 博客文章的中英文双语翻译
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

- **翻译格式规范**：创建 `.claude/rules/translation-format.md`
  - 标题格式：使用 `|` 分隔符
  - 正文格式：换行分隔，中英文独立成段
  - 列表格式：有序列表和无序列表的双语对照规范
  - 图片格式：使用原始 URL，添加中文说明
  - 链接格式：保留原始链接，Sources 区域双语对照
  - 代码块格式：注释不与代码混合
  - 常见问题清单：基于实际修复经验
  - 质量检查清单

- **Codex 审查协作机制**
  - 审查请求模板：`.claude/review-request.md`
  - 审查报告：`.claude/review-report.md`
  - 审查流程：翻译 → 审查请求 → 修复 → 通过

### 变更

- **文章编号统一**：所有文章文件从 ID 02-19 重命名为 ID 01-18
  - Git 自动识别为 rename 操作
  - 统一编号规范，便于管理

- **项目阶段更新**：从"格式规范完善期"更新为"翻译完成期"
  - 翻译进度：4/19（21%）→ 18/18（100%）
  - 所有翻译任务完成

### 文档

- **建立双语对照格式规范**：确保所有翻译文章格式一致
- **创建质量保证流程**：Codex 审查协作机制
- **完善项目记忆系统**：LAST_CLAUDE_PROGRESS.md 记录工作进度

### 改进

- **统一翻译术语**：确保专业术语翻译一致性
- **优化翻译流程**：从翻译到审查的完整工作流
- **提升文档质量**：基于格式规范和审查机制

### 技术亮点

- **RAG 优化技术**：上下文检索（Contextual Retrieval）可将检索失败率降低 67%
- **智能体系统设计**：6 种工作流模式，从简单到复杂的设计原则
- **MCP 协议**：模型上下文协议，实现工具使用标准化
- **Agent SDK**：构建智能体的完整开发框架
- **评估方法**：AI 抗拒性技术评估，确保系统可靠性

### 项目里程碑

- 🎉 **所有 18 篇 Engineering 文章翻译完成**
- 📚 **涵盖智能体、上下文检索、MCP、Agent SDK 等核心技术**
- 🔄 **建立完整的翻译和质量保证流程**
- ✅ **项目翻译工作全面完成**

---

## 0.1.0 2025-01-20 创建项目记忆系统

### 新增

- **根目录 CLAUDE.md**：项目提示词，包含项目背景、目录结构、技术栈、当前状态和 TODO
- **根目录 README.md**：项目说明文档，面向人类读者的项目介绍
- **根目录 CHANGELOG.md**：项目更新日志，记录项目版本变更历史
- **根目录 TASKS.json**：阶段性任务清单，记录项目各阶段的任务状态
- **根目录 LAST_CLAUDE_PROGRESS.md**：上一次工作进度记录，便于工作接续
- **子目录 CLAUDE.md**：anthropic-engineering-articles/ 的项目记忆

### 文档

- 建立完整的项目记忆系统，规范项目管理流程
- 明确项目结构和技术路线
- 记录当前状态和未来规划

### 改进

- 统一项目文档格式，提升可维护性
- 为后续翻译工作提供清晰的指导
## Unreleased

### Changed

- 项目记忆入口切换为根目录 `AGENTS.md` 与 `LAST_RUN.md`
- `claude-code相关/anthropic-engineering-articles/AGENTS.md` 作为子目录局部记忆文件启用
- `.claude/` 目录保留为辅助模板与规则目录，不再作为根项目记忆入口
