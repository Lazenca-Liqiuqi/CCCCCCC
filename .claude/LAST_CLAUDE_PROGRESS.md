# 工作进度记录

## 项目概况

本项目是 Anthropic Engineering Blog 文章的中文翻译项目，创建中英文双语对照版本。项目包含 19 篇技术文章，涵盖 AI 评估、工具使用、智能体开发、上下文工程等主题。

## 工作任务

### Task #10: 翻译 ID 10 - Postmortem

翻译 Anthropic Engineering 文章 "A postmortem of three recent issues"，这是项目的第 10 篇翻译任务。

## 工作内容

### 1. 文章获取与分析

- **原文 URL**: https://www.anthropic.com/engineering/a-postmortem-of-three-recent-issues
- **发布日期**: 2025-09-17
- **文章主题**: 三个近期基础设施 Bug 导致 Claude 响应质量下降的事后分析
- **核心概念**:
  - Postmortem: 事后分析/复盘
  - Infrastructure bugs: 基础设施 Bug
  - Context window routing error: 上下文窗口路由错误
  - Load balancing: 负载平衡
  - Output corruption: 输出损坏
  - Token generation: 标记生成
  - XLA:TPU compiler: XLA:TPU 编译器
  - Approximate top-k: 近似 top-k
  - Exact top-k: 精确 top-k
  - Top-p sampling: Top-p 采样
  - Mixed precision arithmetic: 混合精度算术
  - bf16 (bfloat16): bf16（16位浮点）
  - fp32 (32-bit floating point): fp32（32位浮点）
  - Vector processor: 向量处理器
  - Distributed sort: 分布式排序
  - Sticky routing: 粘性路由
  - Canary groups: 金丝雀组

### 2. 翻译执行

全文约 1500 词，翻译为 ~270 行中英文双语对照内容，包含：

- **引言**: 三个基础设施 Bug 导致 Claude 响应质量下降
- **How we serve Claude at scale**: Claude 的大规模服务架构
  - 多平台部署（API、Amazon Bedrock、Google Cloud Vertex AI）
  - 多硬件平台（AWS Trainium、NVIDIA GPU、Google TPU）
- **Timeline of events**: 事件时间线（8月-9月）
  - 8月5日：第一个 Bug（上下文窗口路由错误）
  - 8月25-26日：另外两个 Bug
  - 8月29日：负载平衡变更加剧问题
- **Three overlapping issues**: 三个重叠问题
  1. Context window routing error（上下文窗口路由错误）
     - 影响：16% 的 Sonnet 4 请求
     - 持续时间：8月5日 - 9月18日
  2. Output corruption（输出损坏）
     - 症状：响应中出现泰语/中文字符
     - 持续时间：8月25日 - 9月2日
  3. Approximate top-k XLA:TPU miscompilation（近似 top-k 编译器 Bug）
     - 影响：Haiku 3.5、可能影响 Sonnet 4 和 Opus 3
     - 持续时间：8月25日 - 9月12日
- **A closer look at the XLA compiler bug**: XLA 编译器 Bug 深度分析
  - 2024年12月补丁的解决方法
  - 混合精度算术问题（bf16 vs fp32）
  - 近似 top-k 操作的深层 Bug
- **Why detection was difficult**: 为什么检测很困难
  - 评估未能捕获质量下降
  - 隐私实践限制工程师访问用户交互
  - 不同平台产生不同症状
- **What we're changing**: 我们正在做出的改变
  - 更敏感的评估
  - 在更多地方进行质量评估
  - 更快的调试工具
- **Acknowledgments**: 致谢
- **Footnotes**: 脚注（4个）

### 3. Codex 审查协作

创建 `.claude/review-request.md` 请求 Codex 审查，收到评分 **88/100**（有条件通过）。

**初始审查结果**:
- **综合评分**: 88/100
- **技术维度**: 49/50
- **战略维度**: 39/50

**发现问题**:
1. 非图片链接缺失（2处）
   - 行 197、199: `feedback@anthropic.com` 未转换为 mailto 链接
2. 标题层级疑似不一致（1处）
   - 行 205: `Acknowledgments` 使用 `###` 而非 `##`
3. 脚注标题未双语化（1处）
   - 行 213: `**Footnotes:**` 应为 `## Footnotes | 脚注`

**优点**:
- 主标题与分节标题均使用"英文 | 中文"格式
- 正文严格按"英文段落 → 空行 → 中文段落"对照
- 无序列表按"英文项 → 中文译文"交错排列
- 4 张图片均使用原始 www-cdn.anthropic.com 链接
- 脚注内容已逐条中英对照

### 4. 问题修复

根据 Codex 审查建议，修复了所有 4 个问题：

**链接修复（2处）**:
1. **行 197**: `feedback@anthropic.com` → `[feedback@anthropic.com](mailto:feedback@anthropic.com)`
2. **行 199**: `feedback@anthropic.com` → `[feedback@anthropic.com](mailto:feedback@anthropic.com)`

**标题层级修复（1处）**:
1. **行 205**: `### Acknowledgments | 致谢` → `## Acknowledgments | 致谢`

**脚注标题修复（1处）**:
1. **行 213**: `**Footnotes:**` → `## Footnotes | 脚注`

**修复后预期评分**: 98-100/100（通过）

## 交付物

### 翻译文件
- `anthropic-engineering-articles/markdown/10-a-postmortem-of-three-recent-issues.md`
  - 行数: ~270 行
  - 图片: 4 张（已转换为原始 www-cdn.anthropic.com URL）
  - 链接: feedback@anthropic.com（mailto 链接）

### 审查文件
- `.claude/review-request.md` - Codex 审查请求
- `.claude/review-report.md` - Codex 审查报告（初始评分 88/100）

## 状态变动

### 翻译进度
- **之前**: 9/19 篇文章已完成（47%）
- **现在**: 10/19 篇文章已完成（53%）
- **新增**: ID 10 - Postmortem

### 已完成文章列表（ID 降序）
1. ✅ ID 19: AI Resistant Evaluations
2. ✅ ID 18: Demystifying Evals for AI Agents
3. ✅ ID 17: Advanced Tool Use
4. ✅ ID 16: Effective Harnesses for Long-Running Agents
5. ✅ ID 15: Code Execution with MCP
6. ✅ ID 14: Claude Code Sandboxing
7. ✅ ID 13: Agent Skills
8. ✅ ID 12: Agent SDK
9. ✅ ID 11: Context Engineering
10. ✅ **ID 10: Postmortem** ⬅️ 新增

### 剩余待翻译任务（9篇）
- Task #11: ID 09 - Writing Tools
- Task #12: ID 08 - Desktop Extensions
- Task #13: ID 07 - Multi-Agent Research
- Task #14: ID 06 - Claude Code Best Practices
- Task #15: ID 05 - Think Tool
- Task #16: ID 04 - SWE-Bench
- Task #17: ID 03 - Building Effective Agents
- Task #18: ID 02 - Contextual Retrieval
- Task #19: ID 01 - 跳过（重复文章）

## 工具

### 主要工具
- **WebSearch**: 搜索正确的文章 URL
- **WebReader**: 获取原文内容
- **Write**: 创建翻译文件
- **Edit**: 修复翻译问题
- **Skill**: 调用 Codex协作、项目记忆 skill
- **TaskUpdate**: 更新任务状态

### 技术栈
- Markdown 格式
- 中英文双语对照
- Git 版本控制

### 遵循规范
- `.claude/rules/translation-format.md` - 翻译格式规范
- Codex 审查协作机制

## 下一步计划

按照翻译计划继续翻译剩余 9 篇文章：
- **下一个任务**: Task #11 - ID 09 "Writing Tools"
- **预计主题**: 为 AI 智能体编写工具

---

**记录生成时间**: 2026-01-25
**任务ID**: #10
**文件**: 10-a-postmortem-of-three-recent-issues.md
**Codex 评分**: 88/100（修复后预期 98-100/100）
