# Anthropic Engineering 文章翻译

## 目录结构

本目录包含 Anthropic 官方工程博客文章的中文翻译，采用双语对照格式。

```
anthropic-engineering-articles/
├── 01-contextual-retrieval.md
├── 02-building-effective-agents.md
├── 03-swe-bench-sonnet.md
├── 04-claude-think-tool.md
├── 05-claude-code-best-practices.md
├── 06-multi-agent-research-system.md
├── 07-desktop-extensions.md
├── 08-writing-tools-for-agents.md
├── 09-a-postmortem-of-three-recent-issues.md
├── 10-effective-context-engineering-for-ai-agents.md
├── 11-agent-sdk.md
├── 12-agent-skills.md
├── 13-claude-code-sandboxing.md
├── 14-code-execution-with-mcp.md
├── 15-effective-harnesses-for-long-running-agents.md
├── 16-advanced-tool-use.md
├── 17-demystifying-evals-for-ai-agents.md
└── 18-AI-resistant-technical-evaluations.md
```

## 文件信息

### 01-contextual-retrieval.md
**标题**: Introducing Contextual Retrieval | 介绍上下文检索
**发布日期**: 2024年9月19日
**内容**: 介绍上下文检索技术，通过为嵌入块添加上下文来改进 RAG 检索准确性
**核心技术**: RAG、Contextual Embeddings、Contextual BM25、Reranking

### 02-building-effective-agents.md
**标题**: Building Effective Agents | 构建有效的智能体
**内容**: 探讨如何构建有效的 AI 智能体，包括核心原则和最佳实践
**核心技术**: Agent 设计、提示工程

### 03-swe-bench-sonnet.md
**标题**: Claude 3.5 Sonnet and SWE-bench | SWE-bench 基准测试
**发布日期**: 2024年6月27日
**内容**: Claude 3.5 Sonnet 在 SWE-bench 基准测试中的表现分析
**核心技术**: SWE-bench、代码生成、基准测试

### 04-claude-think-tool.md
**标题**: The "think" Tool | "think" 工具
**发布日期**: 2024年11月19日
**内容**: 介绍 "think" 工具的使用场景和最佳实践
**核心技术**: 工具使用、推理模式

### 05-claude-code-best-practices.md
**标题**: Claude Code Best Practices | Claude Code 最佳实践
**发布日期**: 2025年1月7日
**内容**: Claude Code 的最佳实践指南
**核心技术**: Claude Code、工作流程优化

### 06-multi-agent-research-system.md
**标题**: A Multi-Agent System for Literature Review | 多智能体研究系统
**发布日期**: 2024年10月29日
**内容**: 使用多智能体系统进行文献综述的方法
**核心技术**: 多智能体系统、文献综述

### 07-desktop-extensions.md
**标题**: Claude Code Desktop Extensions | 桌面扩展
**内容**: Claude Code 桌面扩展的开发与使用
**核心技术**: 桌面扩展、MCP

### 08-writing-tools-for-agents.md
**标题**: Writing Tools for Agents | 为智能体写作工具
**发布日期**: 2024年10月8日
**内容**: 如何为 AI 智能体设计和编写工具
**核心技术**: 工具设计、函数调用

### 09-a-postmortem-of-three-recent-issues.md
**标题**: A Postmortem of Three Recent Issues | 问题复盘
**发布日期**: 2024年11月12日
**内容**: 对三个近期问题的复盘分析
**核心技术**: 问题分析、系统改进

### 10-effective-context-engineering-for-ai-agents.md
**标题**: Effective Context Engineering for AI Agents | 上下文工程
**发布日期**: 2024年12月17日
**内容**: AI 智能体的有效上下文工程技术
**核心技术**: 上下文工程、提示优化

### 11-agent-sdk.md
**标题**: Building Agents with the Claude Agent SDK | Agent SDK
**发布日期**: 2025年1月9日
**内容**: 使用 Claude Agent SDK 构建智能体
**核心技术**: Agent SDK、智能体开发

### 12-agent-skills.md
**标题**: Agent Skills | Agent 技能
**发布日期**: 2025年1月28日
**内容**: Agent Skills 系统的介绍和使用
**核心技术**: Agent Skills、技能封装

### 13-claude-code-sandboxing.md
**标题**: Claude Code Sandboxing | Claude Code 沙盒
**发布日期**: 2025年1月14日
**内容**: Claude Code 的沙盒安全机制
**核心技术**: 沙盒、安全隔离

### 14-code-execution-with-mcp.md
**标题**: Code Execution with MCP | 使用 MCP 执行代码
**发布日期**: 2025年1月23日
**内容**: 通过 MCP 协议执行代码的方法
**核心技术**: MCP、代码执行

### 15-effective-harnesses-for-long-running-agents.md
**标题**: Effective Harnesses for Long-Running Agents | 长运行智能体
**发布日期**: 2025年1月30日
**内容**: 长时间运行智能体的有效工具设计
**核心技术**: 长运行智能体、工具设计

### 16-advanced-tool-use.md
**标题**: Introducing Advanced Tool Use | 高级工具使用
**发布日期**: 2025年2月3日
**内容**: Claude 的高级工具使用功能
**核心技术**: 高级工具、工具搜索

### 17-demystifying-evals-for-ai-agents.md
**标题**: Demystifying Evals for AI Agents | 评估详解
**发布日期**: 2025年1月21日
**内容**: AI 智能体评估方法的详解
**核心技术**: 评估方法、指标设计

### 18-AI-resistant-technical-evaluations.md
**标题**: Designing AI Resistant Technical Evaluations | AI 抗拒性评估
**发布日期**: 2025年1月17日
**内容**: 设计抗拒 AI 攻击的技术评估
**核心技术**: AI 安全、评估设计

## 依赖关系

- 所有文章遵循 `.claude/rules/translation-format.md` 翻译格式规范
- 翻译质量通过 Codex 审查协作机制保证
- 文章编号统一为 01-18

## 注意事项

- 本目录为独立 Git 仓库
- 文章采用双语对照格式（英文 | 中文）
- 新翻译文章应遵循翻译格式规范
