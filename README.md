# CCCCCCC

> Anthropic、Claude Code 与 Codex 中文资料合集

## 项目全称

本项目全称为：**Claude Code & Codex Chinese Commentary Collection**。

为便于仓库管理与命名长度控制，仓库短名可使用简写形式，但文档与对外说明统一使用上述全称。

## 项目背景信息

CCCCCCC（Claude Code & Codex Chinese Commentary Collection）是一个整理 Anthropic、Claude Code 与 Codex 中文资料的项目。本项目为中文开发者提供高质量的 AI 辅助编程工具指南，包括：

- **Claude Code 更新日志**：双语对照版本，跟踪重要版本变化
- **Anthropic 工程文章**：帮助理解 AI 代理、上下文工程、MCP 协议等核心技术
- **Codex CLI 资料**：补充 Codex 使用说明与工作流参考

项目当前已经把“项目记忆入口”从 Claude 风格迁移到 Codex 风格，统一使用 `AGENTS.md`、`README.md`、`CHANGELOG.md` 和 `LAST_RUN.md`。

## 目录结构

```text
CCCCCCC/
├── AGENTS.md                                  # Codex 项目记忆入口
├── README.md                                  # 项目说明文档（本文件）
├── CHANGELOG.md                               # 项目更新日志
├── LAST_RUN.md                                # 上一次工作总结
├── .claude/                                   # Claude Code 辅助配置与模板
│   ├── commands/                              # 自定义命令
│   ├── rules/                                 # 翻译规则
│   │   └── translation-format.md              # 翻译格式规范
│   ├── review-request.md                      # 审查请求模板
│   └── review-report.md                       # 审查报告模板
├── claude-code相关/
│   ├── Claude Code CHANGELOG - 双语对照.md    # Claude Code 更新日志双语版
│   └── anthropic-engineering-articles/
│       ├── AGENTS.md                          # 子目录记忆入口
│       └── 01-18 系列文章                     # Anthropic Engineering 文章翻译
└── codex相关/
    └── codex_cli_help.md                      # Codex CLI 中文整理
```

## 技术栈与技术路线

### 资料整理流程

1. **术语管理**：维护 `.claude/rules/translation-format.md` 确保翻译一致性
2. **模板复用**：保留 `.claude/review-request.md` 等模板支持资料整理
3. **双语对照**：采用原文与译文对照的格式，便于理解与学习
4. **质量保证**：遵循格式规范，确保专业术语翻译的准确性
5. **项目记忆**：统一通过 `AGENTS.md` 与 `LAST_RUN.md` 维护 Codex 工作上下文

### 资料组织

- **主题分组**：`claude-code相关/` 与 `codex相关/` 分别承载不同主题资料
- **翻译沉淀**：Anthropic Engineering 文章集中保存在 `claude-code相关/anthropic-engineering-articles/`
- **辅助配置**：`.claude/` 保留翻译规则与审查模板，但不再承担项目记忆入口职责

## 当前状态

**结构迁移期**

Anthropic Engineering 文章翻译已经完成，当前重点转为资料结构整理与 Codex 记忆体系迁移。

**已完成**：
- [x] 翻译 18/18 篇文章（100%）
- [x] 文章编号统一为 01-18
- [x] 创建翻译格式规范 `.claude/rules/translation-format.md`
- [x] 建立 Codex 审查协作机制
- [x] 统一所有文章排版风格
- [x] 建立根目录 `AGENTS.md` / `LAST_RUN.md`

**项目里程碑**：
- 所有 Engineering 文章翻译完成
- 涵盖智能体、上下文检索、MCP、Agent SDK 等核心技术
- 项目记忆入口已切换为 Codex 体系

## 工作阶段

### 阶段 1: 翻译准备期
- [x] 创建项目结构
- [x] 制定翻译格式规范
- [x] 建立 Codex 审查协作机制

### 阶段 2: 翻译执行期
- [x] ID 01: Introducing Contextual Retrieval（上下文检索）
- [x] ID 02: Building Effective Agents（构建有效的智能体）
- [x] ID 03: SWE-bench Sonnet（SWE-bench 基准测试）
- [x] ID 04: The "think" tool（"think" 工具）
- [x] ID 05: Claude Code Best Practices（Claude Code 最佳实践）
- [x] ID 06: Multi-Agent Research System（多智能体研究系统）
- [x] ID 07: Desktop Extensions（桌面扩展）
- [x] ID 08: Writing Tools（写作工具）
- [x] ID 09: A Postmortem of Three Recent Issues（问题复盘）
- [x] ID 10: Effective Context Engineering for AI Agents（上下文工程）
- [x] ID 11: Building Agents with the Claude Agent SDK（Agent SDK）
- [x] ID 12: Equipping Agents for the Real World with Agent Skills（Agent 技能）
- [x] ID 13: Claude Code Sandboxing（Claude Code 沙盒）
- [x] ID 14: Code Execution with MCP（使用 MCP 执行代码）
- [x] ID 15: Effective Harnesses for Long-Running Agents（长运行智能体）
- [x] ID 16: Introducing Advanced Tool Use（高级工具使用）
- [x] ID 17: Demystifying Evals for AI Agents（评估详解）
- [x] ID 18: Designing AI Resistant Technical Evaluations（AI 抗拒性评估）

### 阶段 3: 结构迁移与维护期
- [x] 文章编号统一为 01-18
- [x] 排版风格统一（标题、粗体、双语格式）
- [x] 项目记忆入口迁移到 Codex 体系
- [ ] 持续跟进 Claude Code 新版本更新
- [ ] 根据需要补充新的 Codex 资料
- [ ] 持续清理旧路径和旧命名引用

### 注意事项
- 新翻译文章应直接遵循 `.claude/rules/translation-format.md` 规范
- 项目状态更新优先写入 `AGENTS.md` 和 `LAST_RUN.md`
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

**当前版本**：0.2.1

详见 [CHANGELOG.md](./CHANGELOG.md)

## 贡献

欢迎提交 Issue 和 Pull Request 来改进本项目。

## 许可

本项目翻译内容遵循原文许可协议。原文版权归 Anthropic 所有。
# 项目记忆组件

- 当前生效的根项目记忆文件是 `AGENTS.md`
- 当前生效的会话续接文件是 `LAST_RUN.md`
- `claude-code相关/anthropic-engineering-articles/AGENTS.md` 是子目录局部记忆文件
- `.claude/` 目录目前只保留辅助模板与翻译规则，不再作为根项目记忆入口
