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
- **术语管理**：维护 `.claude/terminology.md` 确保翻译一致性
- **版本控制**：`anthropic-engineering-articles/` 为独立 Git 仓库
- **翻译流程**：使用翻译请求模板，遵循术语表规范
- **更新跟进**：通过自定义命令持续跟进 Claude Code 新版本

## 当前状态

- **进行中**：获取Anthropic Engineering文章（7/16篇已完成）
- **已完成**：CHANGELOG 双语对照已更新至 2.1.12 版本
- **待完成**：待翻译版本 2.1.6, 2.1.5, 2.1.4, 2.1.3, 2.1.2

## TODO

### 阶段1：获取Anthropic Engineering文章

使用 WebReader 逐篇抓取16篇Anthropic Engineering文章的纯英文内容。

### 阶段2：翻译16篇文章（双语对照格式）

使用 Codex 协作翻译所有16篇文章，分批执行。

### 阶段3：质量检查和版本控制

执行自动化检查、术语一致性验证、人工审校，完成 Git 提交。

## 资源

- [Claude Code GitHub](https://github.com/anthropics/claude-code)
- [Claude Code CHANGELOG](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
- [Anthropic Engineering Blog](https://www.anthropic.com/engineering)
