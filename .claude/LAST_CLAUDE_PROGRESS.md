## 项目概况

本项目是 Anthropic Engineering Blog 文章的中文翻译项目，创建中英文双语对照版本。项目包含 19 篇技术文章，涵盖 AI 评估、工具使用、智能体开发、沙箱安全等主题。

## 工作任务

### Task #6: 翻译 ID 14 - Claude Code Sandboxing

翻译 Anthropic Engineering 文章 "Making Claude Code more secure and autonomous with sandboxing"，这是项目的第 6 篇翻译任务。

## 工作内容

### 1. 文章获取与分析

- **原文 URL**: https://www.anthropic.com/engineering/claude-code-sandboxing
- **发布日期**: 2025-10-20
- **文章主题**: Claude Code 沙箱安全特性
- **核心概念**: 文件系统隔离、网络隔离、沙箱 bash 工具、网页版 Claude Code

### 2. 翻译执行

全文约 800 词，翻译为 ~200 行中英文双语对照内容，包含：

- **引言**: Claude Code 的权限模型和安全风险
- **Sandboxing 概述**: 更安全、更自主的方法
- **两个核心隔离机制**: 文件系统隔离、网络隔离
- **沙箱 bash 工具**: 无需权限提示的安全 bash 执行
- **网页版 Claude Code**: 在云端安全运行
- **入门指南**: 如何使用这些工具
- **致谢**: 文章作者和贡献者

### 3. Codex 审查协作

创建 `.claude/review-request.md` 请求 Codex 审查，收到评分 **81/100**（有条件通过）。

**审查结果**:
- 技术维度: 43/50
- 战略维度: 38/50

**发现的问题**:
1. 有序列表中文行仍保留序号（未按交错格式排列）
2. 标题层级不一致（`###` 应改为 `##`）
3. 部分资源引用缺少可点击链接

### 4. 问题修复

根据 Codex 审查报告，完成以下修复：

1. **有序列表格式修复**（3处）:
   - 两个核心隔离机制列表（行 35-42）
   - 沙箱强制执行列表（行 63-70）
   - 入门指南列表（行 115-120）
   - 修复方式: 中文行删除序号，英文→中文交错排列

2. **标题层级修复**:
   - 行 11: `### Keeping users secure...` → `## Keeping users secure...`

3. **链接补齐**（2处）:
   - 行 87: "open sourced this feature" → `[open sourced this feature](https://github.com/anthropics/claude-code)`
   - 行 127: "launch blog post" → `[launch blog post](https://www.anthropic.com/engineering/claude-code-sandboxing)`

## 交付物

### 翻译文件
- `anthropic-engineering-articles/markdown/14-claude-code-sandboxing.md`
  - 行数: ~200 行
  - 图片: 2 张（已转换为原始 www-cdn.anthropic.com URL）
  - 链接: docs、claude.com/code、GitHub 仓库、博客文章

### 审查文件
- `.claude/review-request.md` - Codex 审查请求
- `.claude/review-report.md` - Codex 审查报告

## 状态变动

### 翻译进度
- **之前**: 5/19 篇文章已完成（26%）
- **现在**: 6/19 篇文章已完成（32%）
- **新增**: ID 14 - Claude Code Sandboxing

### 已完成文章列表
1. ID 19: AI Resistant Evaluations
2. ID 18: Demystifying Evals for AI Agents
3. ID 17: Advanced Tool Use
4. ID 16: Effective Harnesses for Long-Running Agents
5. ID 15: Code Execution with MCP
6. ID 14: Claude Code Sandboxing ⬅️ 新增

### 剩余待翻译
- 13 篇文章待翻译（ID 13-02，跳过 ID 01）

## 工具

### 主要工具
- **WebReader**: 获取原文内容
- **Write**: 创建翻译文件
- **Edit**: 修复格式问题
- **Skill**: 调用 Codex协作、项目记忆 skill

### 技术栈
- Markdown 格式
- 中英文双语对照
- Git 版本控制

### 遵循规范
- `.claude/rules/translation-format.md` - 翻译格式规范
- Codex 审查协作机制

## 下一步计划

按照翻译计划继续翻译剩余 13 篇文章：
- Task #7: ID 13 - Agent Skills
- Task #8: ID 12 - Agent SDK
- ...（继续至 ID 02，跳过 ID 01）
