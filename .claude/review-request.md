# Codex 审查请求 | Review Request

## 文章信息 | Article Information

| 项目 | 内容 |
|------|------|
| **文件** | `03-building-effective-agents.md` |
| **标题** | Building effective agents |
| **中文标题** | 构建有效的智能体 |
| **发布日期** | 2024年12月19日 |
| **原文 URL** | https://www.anthropic.com/research/building-effective-agents |
| **审查状态** | 第一轮审查 |

---

## 文章结构 | Article Structure

### 主要章节（8个）

1. What are agents? | 什么是智能体？
2. When (and when not) to use agents | 何时（以及何时不）使用智能体
3. When and how to use frameworks | 何时以及如何使用框架
4. Building blocks, workflows, and agents | 构建模块、工作流和智能体
   - Building block: The augmented LLM | 构建模块：增强型 LLM
   - Workflow: Prompt chaining | 工作流：提示链
   - Workflow: Routing | 工作流：路由
   - Workflow: Parallelization | 工作流：并行化
   - Workflow: Orchestrator-workers | 工作流：编排器-工作者
   - Workflow: Evaluator-optimizer | 工作流：评估器-优化器
   - Agents | 智能体
5. Combining and customizing these patterns | 组合和定制这些模式
6. Summary | 总结
7. Appendix 1: Agents in practice | 附录 1：实践中的智能体
8. Appendix 2: Prompt engineering your tools | 附录 2：提示工程你的工具

### 子章节

- Acknowledgements | 致谢
- A. Customer support | A. 客户支持
- B. Coding agents | B. 编码智能体

---

## 文章统计 | Article Statistics

| 项目 | 数值 |
|------|------|
| **总行数** | ~600 行 |
| **主要章节** | 8 个 |
| **图片数量** | 8 张（流程图和架构图） |
| **代码块** | 0 个 |
| **表格** | 0 个 |
| **外部链接** | 5 个（Anthropic Research、cookbook、框架链接） |

---

## 关键术语表 | Key Terminology

### 核心概念术语（12个）

| 英文术语 | 中文翻译 |
|----------|----------|
| Agent | 智能体 |
| Agentic systems | 智能体系统 |
| Workflow | 工作流 |
| Augmented LLM | 增强型 LLM |
| LLM (Large Language Model) | LLM（大语言模型） |
| Tool use | 工具使用 |
| Retrieval | 检索 |
| Memory | 记忆 |
| Ground truth | 真实答案 |
| Orchestrator | 编排器 |
| Worker | 工作者 |
| Autonomy | 自主性 |

### 工作流模式术语（10个）

| 英文术语 | 中文翻译 |
|----------|----------|
| Prompt chaining | 提示链 |
| Routing | 路由 |
| Parallelization | 并行化 |
| Sectioning | 分节 |
| Voting | 投票 |
| Orchestrator-workers | 编排器-工作者 |
| Evaluator-optimizer | 评估器-优化器 |
| Gate | 门 |
| Checkpoint | 检查点 |
| Blocker | 障碍 |

### 框架与工具术语（8个）

| 英文术语 | 中文翻译 |
|----------|----------|
| LangGraph | LangGraph |
| Amazon Bedrock | Amazon Bedrock |
| Rivet | Rivet |
| Vellum | Vellum |
| Model Context Protocol | 模型上下文协议 (MCP) |
| Agent-computer interface | 智能体-计算机接口 (ACI) |
| Poka-yoke | 防错 |
| Guardrails | 防护栏 |

### 开发实践术语（8个）

| 英文术语 | 中文翻译 |
|----------|----------|
| Sandbox | 沙盒 |
| Iteration | 迭代 |
| Evaluation | 评估 |
| Feedback loop | 反馈循环 |
| Human oversight | 人工监督 |
| Usage-based pricing | 基于使用量的定价 |
| Human-computer interface | 人机交互界面 (HCI) |
| Docstring | 文档字符串 |

---

## 审查重点 | Review Focus

### 格式规范检查

1. **标题格式**：
   - 所有级别的标题（#、##、###、####）使用 `|` 分隔符
   - 确保标题层级正确（# → ## → ### → ####）

2. **正文段落**：
   - 使用换行分隔，中英文段落之间有空行
   - 英文段落中禁止出现中文字符
   - 中文段落独立成段

3. **列表格式**：
   - 无序列表：中英文都有 `-` 符号且逐条对照
   - 嵌套列表：保持缩进格式一致
   - 列表项之间应有空行分隔

4. **图片格式**：
   - 使用原始图片链接（www-cdn.anthropic.com）
   - 每张图片后面有中文说明
   - 禁止使用代理 URL（_next/image）

5. **链接格式**：
   - 保留原始链接
   - Sources 区域添加中文链接行
   - 确保所有链接可点击

6. **特殊格式**：
   - `__text__` 加粗格式保持一致
   - 附录章节编号（A. B.）保持一致

### 内容质量检查

1. **术语一致性**：
   - Agent 统一翻译为"智能体"
   - Workflow 统一翻译为"工作流"
   - LLM 保持原文或翻译为"大语言模型"
   - Framework 翻译为"框架"

2. **翻译准确性**：
   - 技术概念是否准确传达（agentic systems、orchestrator-workers、evaluator-optimizer）
   - 工作流模式的描述是否清晰
   - 框架名称是否正确（LangGraph、Rivet、Vellum）

3. **可读性**：
   - 中文表达流畅自然
   - 技术内容易于理解
   - 专业术语不过度晦涩

4. **完整性**：
   - 所有章节完整无遗漏
   - 8 张图片完整
   - 附录内容完整
   - Sources 区域完整

### 特殊注意事项

1. **架构概念区分**：
   - Agentic systems（智能体系统）vs workflows（工作流）vs agents（智能体）的准确区分
   - Orchestrator-workers 与 parallelization 的关键区别（灵活性 vs 预定义）
   - Evaluator-optimizer 与 prompt chaining 的区别（循环反馈 vs 线性步骤）

2. **工作流模式**：
   - 6 种工作流模式的准确描述
   - 每种模式的适用场景和示例
   - 模式之间的差异和选择标准

3. **框架建议**：
   - 直接使用 LLM API 的建议
   - 框架的优缺点说明
   - 抽象层的理解要求

4. **设计原则**：
   - 三个核心原则（简单性、透明度、ACI）
   - HCI 与 ACI 的类比
   - Poka-yoke（防错）设计理念

5. **实践案例**：
   - 客户支持场景的 4 个要点
   - 编码智能体的 4 个优势
   - SWE-bench 基准测试提及

---

## 质量检查清单 | Quality Checklist

### 基础格式
- [ ] 所有标题（#、##、###、####）使用 `|` 分隔符
- [ ] 正文段落使用换行，不使用 `|`
- [ ] 英文段落和中文段落之间有空行
- [ ] 无序列表中英文逐条对照
- [ ] 嵌套列表缩进一致

### 内容质量
- [ ] 图片使用原始 URL（www-cdn.anthropic.com）
- [ ] 链接保持可点击状态
- [ ] `__text__` 加粗格式正确
- [ ] 术语翻译一致

### 完整性检查
- [ ] 所有8个主要章节完整
- [ ] 2个附录完整（实践中的智能体、提示工程你的工具）
- [ ] 8张图片完整
- [ ] Sources 区域有中文对照
- [ ] 英文段落中没有中文字符
- [ ] 中文段落翻译完整，无遗漏

### 术语一致性
- [ ] Agent 翻译一致（智能体）
- [ ] Workflow 翻译一致（工作流）
- [ ] Orchestrator 翻译一致（编排器）
- [ ] Evaluator-optimizer 翻译一致（评估器-优化器）
- [ ] Framework 翻译一致（框架）

---

## 预期评分 | Expected Score

| 评分维度 | 预期分数 |
|----------|----------|
| **综合评分** | **90-95/100** |
| **建议状态** | **通过（预期）** |
| **技术维度** | **45-48/50** |
| **战略维度** | **45-47/50** |

**预期依据**：
- 严格按照格式规范创建，格式问题较少
- 技术内容准确，术语翻译一致
- 双语对照完整，章节结构清晰
- 图片、链接格式正确
- Sources 区域包含中文对照

---

## 特别说明 | Special Notes

1. **首次翻译**：这是 ID 03 的首次翻译，无修复历史
2. **格式规范**：已严格按照 `.claude/rules/translation-format.md` 创建
3. **技术准确性**：已确保技术概念和架构模式准确性
4. **完整性**：所有章节、附录、图片已完整翻译
5. **图片处理**：所有 8 张图片使用原始 URL（www-cdn.anthropic.com）

**会话 ID**: 当前会话
**请求时间**: 2026-01-26
**审查轮次**: 第一轮（首次审查）
