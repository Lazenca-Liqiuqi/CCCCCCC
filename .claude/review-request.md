# 翻译审查请求 - ID 07

时间：2026-01-26

## 项目基本信息

**项目名称**: Claude Code 中文指南合集 - Engineering 文章翻译
**项目阶段**: 持续翻译期
**当前进度**: 16/19 篇文章已完成（84%）

## 项目状态与进展

### 本次工作内容

**任务**: Task #13 - 翻译 ID 07: Multi-Agent Research System

**文章信息**:
- **标题**: How we built our multi-agent research system
- **中文标题**: 我们如何构建多智能体研究系统
- **发布日期**: 2025-06-13
- **原文 URL**: https://www.anthropic.com/engineering/multi-agent-research-system
- **文件路径**: `anthropic-engineering-articles/markdown/07-multi-agent-research-system.md`

### 文章结构分析

**主要内容章节**:
1. **引言** - 多智能体系统概述与 Research 功能介绍
2. **Benefits of a multi-agent system** | 多智能体系统的优势
   - 研究工作的不可预测性
   - 子智能体的压缩作用
   - 多智能体系统的性能优势
   - Token 使用与性能关系
   - 经济可行性与适用场景

3. **Architecture overview for Research** | Research 架构概览
   - 编排者-工作者模式
   - 动态多步搜索 vs 静态 RAG
   - 完整工作流程图

4. **Prompt engineering and evaluations for research agents** | 研究智能体的提示工程与评估
   - 8 个核心原则：
     1. Think like your agents（像你的智能体一样思考）
     2. Teach the orchestrator how to delegate（教导编排者如何委派）
     3. Scale effort to query complexity（根据查询复杂性调整工作量）
     4. Tool design and selection are critical（工具设计和选择至关重要）
     5. Let agents improve themselves（让智能体自我改进）
     6. Start wide, then narrow down（先宽泛，后深入）
     7. Guide the thinking process（指导思考过程）
     8. Parallel tool calling transforms speed and performance（并行工具调用转变速度和性能）

5. **Effective evaluation of agents** | 智能体的有效评估
   - 多智能体系统的评估挑战
   - 立即开始小样本评估
   - LLM 作为评估者
   - 人类评估的重要性
   - 涌现行为与协作框架

6. **Production reliability and engineering challenges** | 生产可靠性与工程挑战
   - 智能体的有状态性与错误复合
   - 调试的新方法
   - 部署的协调挑战
   - 同步执行的瓶颈

7. **Conclusion** | 结论
   - 原型到生产的差距
   - 多智能体系统的价值
   - Clio 嵌入图展示用例

8. **Acknowledgements** | 致谢

9. **Appendix** | 附录
   - 终态评估
   - 长期对话管理
   - 文件系统输出最小化"传话游戏"

### 交付物统计

| 项目 | 内容 |
|------|------|
| **文件路径** | `anthropic-engineering-articles/markdown/07-multi-agent-research-system.md` |
| **文件大小** | ~540 行 |
| **图片数量** | 3 张 |
| **图片格式** | 原始 www-cdn.anthropic.com URL |
| **关键术语** | ~45 个 |
| **外部链接** | 1 个 |

## 关键术语表

| 英文术语 | 中文翻译 |
|----------|----------|
| Multi-agent system | 多智能体系统 |
| Agent | 智能体 |
| Subagent | 子智能体 |
| Orchestrator-worker pattern | 编排者-工作者模式 |
| Lead agent | 主导智能体 |
| Open-ended problems | 开放式问题 |
| Path-dependent | 路径依赖 |
| Context window | 上下文窗口 |
| Separation of concerns | 关注点分离 |
| Breadth-first queries | 广度优先查询 |
| Token usage | Token 使用 |
| Retrieval Augmented Generation (RAG) | 检索增强生成（RAG） |
| Static retrieval | 静态检索 |
| Dynamic search | 动态搜索 |
| Prompt engineering | 提示工程 |
| Tool design | 工具设计 |
| Emergent behaviors | 涌现行为 |
| Evaluation | 评估 |
| LLM-as-judge | LLM 作为评估者 |
| Stateful | 有状态的 |
| Rainbow deployments | 彩虹部署 |
| Synchronous execution | 同步执行 |
| Asynchronous execution | 异步执行 |
| Extended thinking mode | 扩展思考模式 |
| Interleaved thinking | 交错思考 |
| Tool calls | 工具调用 |
| Checkpoints | 检查点 |
| Deterministic safeguards | 确定性保障 |
| Production tracing | 生产跟踪 |
| End-state evaluation | 终态评估 |
| Long-horizon conversation | 长期对话 |
| Context management | 上下文管理 |
| Game of telephone | 传话游戏 |
| Artifact systems | 工件系统 |
| Handoffs | 交接 |
| MCP (Model Context Protocol) | 模型上下文协议（MCP） |
| Clio embedding plot | Clio 嵌入图 |
| BrowseComp evaluation | BrowseComp 评估 |
| SEO-optimized content farms | SEO 优化的内容农场 |

## 审查范围

### 需要审查的文件

**主要审查目标**:
- `anthropic-engineering-articles/markdown/07-multi-agent-research-system.md`

### 审查重点

#### 格式规范检查

根据 `.claude/rules/translation-format.md` 规范，请检查：

1. **标题格式**
   - 所有级别标题（#、##、###、####）是否使用 `|` 分隔符
   - 格式：`English Title | 中文标题`

2. **正文段落格式**
   - 英文段落和中文段落之间是否有空行
   - 是否使用换行分隔（不使用 `|`）
   - 英文段落中是否没有中文字符
   - 中文段落中是否没有未翻译的英文单词（专有名词除外）

3. **有序列表格式**
   - 英文行保留序号（`1.` `2.` `3.` 等）
   - 中文行删除序号

4. **无序列表格式**
   - 英文行和中文行是否都保留 `-` 符号
   - 英文行和中文行之间是否有空行

5. **图片格式**
   - 是否使用原始 www-cdn.anthropic.com URL
   - 是否禁止使用代理 URL（`_next/image?url=...`）
   - 是否有中文图片说明

6. **链接格式**
   - 是否保留可点击的 markdown 链接
   - 链接文本是否翻译为中文

7. **代码块格式**
   - 是否保持原样，不翻译
   - 注释是否添加中文翻译（如有）

#### 内容质量检查

1. **翻译准确性**
   - 术语翻译是否一致（参考术语表）
   - 技术概念翻译是否准确
   - 是否遗漏重要信息

2. **完整性**
   - 所有章节是否都翻译
   - 图片是否都有中文说明
   - 外部链接是否保持可点击

3. **可读性**
   - 中文表达是否流畅自然
   - 专业术语是否统一

#### 特别注意事项

1. **粗体标记**
   - 文中使用 `__text__` 格式的粗体标记，需要检查中英文是否都保持一致

2. **代码/命令示例**
   - 文中可能包含工具调用示例、命令等
   - 确认这些内容保持原样，不翻译

3. **专有名词**
   - Claude、Research、Opus、Sonnet 等专有名词保持英文
   - Clio、BrowseComp 等内部名称保持英文

4. **数字和单位**
   - 90.2%、4×、15×、200,000 等保持原格式
   - Claude Opus 4、Claude Sonnet 4 等版本号保持原格式

## 审查评分标准

### 技术维度（50分）

1. **标题格式正确性**（10分）
   - 所有标题使用 `|` 分隔符
   - 中英文顺序正确

2. **正文格式正确性**（20分）
   - 空行分隔正确
   - 无 `|` 混合使用
   - 英文段落无中文字符

3. **列表格式正确性**（10分）
   - 有序列表：英文有序号，中文无序号
   - 无序列表：中英文都有 `-` 符号且有空行分隔

4. **代码块格式正确性**（5分）
   - 保持原样，不翻译
   - 无 `|` 混合

5. **图片链接正确性**（5分）
   - 使用原始 URL
   - 有中文说明

### 战略维度（50分）

1. **需求匹配度**（15分）
   - 符合双语对照规范
   - 适合中文开发者阅读

2. **格式规范一致性**（20分）
   - 遵循 translation-format.md
   - 无系统性问题

3. **翻译质量**（10分）
   - 术语翻译一致
   - 技术概念准确
   - 表达流畅自然

4. **可维护性**（5分）
   - 格式清晰统一
   - 易于后续更新

## 输出要求

请提供：

1. **综合评分**（0-100分）
   - 技术维度评分（0-50分）
   - 战略维度评分（0-50分）
   - 明确建议（通过/退回/有条件通过）

2. **问题清单**
   - 按优先级排序（高/中/低）
   - 说明具体位置（行号）
   - 描述问题和修复建议
   - 提供修复前后对比示例

3. **优点列表**
   - 做得好的地方
   - 值得保持的优点

4. **修改建议**
   - 按优先级排序
   - 提供具体修复方案

## 预期问题提示

基于以往经验，可能需要注意：

1. **无序列表格式**：中文行可能缺少 `-` 符号或空行分隔
2. **粗体标记**：`__text__` 格式在中文段落中可能遗漏
3. **数字和单位**：需要保持原格式，不翻译
4. **专有名词**：确保保持英文（Claude、Research、Opus、Sonnet 等）
5. **长段落**：需要检查空行分隔是否正确
6. **链接**：确保文中提到的资源（如 Cookbook）有可点击链接

---

**会话 ID**: 019bf489-67c1-7362-a343-d5114f763579
**请求时间**: 2026-01-26
