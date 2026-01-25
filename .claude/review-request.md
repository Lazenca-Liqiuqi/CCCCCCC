# 翻译格式审查请求 - ID 09

## 项目基本信息

**项目名称**: Claude Code 中文指南合集 - Engineering 文章翻译
**文章**: 09-writing-tools-for-agents.md
**标题**: Writing effective tools for AI agents—using AI agents
**主题**: 为AI智能体编写有效工具——使用AI智能体
**翻译日期**: 2026-01-25

## 项目结构与状态

### 目录结构
```
anthropic-engineering-articles/
└── markdown/
    ├── 19-AI-resistant-technical-evaluations.md
    ├── 18-demystifying-evals-for-ai-agents.md
    ├── 17-advanced-tool-use.md
    ├── 16-effective-harnesses-for-long-running-agents.md
    ├── 15-code-execution-with-mcp.md
    ├── 14-claude-code-sandboxing.md
    ├── 13-agent-skills.md
    ├── 12-agent-sdk.md
    ├── 11-effective-context-engineering-for-ai-agents.md
    ├── 10-a-postmortem-of-three-recent-issues.md
    └── 09-writing-tools-for-agents.md (本次翻译)
```

### 项目状态
- **已完成翻译**: 11/19 篇文章（58%）
- **格式规范**: `.claude/rules/translation-format.md`
- **上一次审查**: ID 10 评分 88/100（修复后预期 98-100/100）

## 用户的原始需求

翻译 Anthropic Engineering 文章 ID 09，遵循项目的翻译格式规范，创建中英文双语对照版本。

## 本次工作内容与交付物

### 工作内容
1. 获取原文：https://www.anthropic.com/engineering/writing-tools-for-agents
2. 全文翻译，包含以下章节：
   - 引言：使用 MCP 协议为 LLM 智能体配备工具
   - What is a tool?：工具的本质（确定性系统与非确定性智能体之间的契约）
   - How to write tools：如何编写工具
     - Building a prototype（构建原型）
     - Running an evaluation（运行评估）
       - Generating evaluation tasks（生成评估任务）
       - Running the evaluation（运行评估）
       - Analyzing results（分析结果）
     - Collaborating with agents（与智能体协作）
   - Principles for writing effective tools：编写有效工具的原则
     - Choosing the right tools for agents（为智能体选择正确的工具）
     - Namespacing your tools（为工具添加命名空间）
     - Returning meaningful context from your tools（从工具返回有意义的上下文）
     - Optimizing tool responses for token efficiency（优化工具响应以提高标记效率）
     - Prompt-engineering your tool descriptions（对工具描述进行提示工程）
   - Looking ahead：展望未来
   - Acknowledgements：致谢
   - Footnotes：脚注（1个）

### 交付物
- **文件**: `anthropic-engineering-articles/markdown/09-writing-tools-for-agents.md`
- **行数**: ~550 行
- **图片**: 8 张（已转换为原始 www-cdn.anthropic.com URL）
- **链接**: 文档、API、SWE-bench、开发者指南等资源链接

## 需要审查的目标文件与范围

### 目标文件
```
anthropic-engineering-articles/markdown/09-writing-tools-for-agents.md
```

### 审查范围
全文翻译格式与质量审查

## 审查要点

### 1. 标题格式审查

- [ ] **主标题格式**: `# English Title | 中文标题`
- [ ] **二级标题格式**: `## English Subtitle | 中文副标题`
- [ ] **三级标题格式**: `### English Section | 中文章节`
- [ ] **四级标题格式**: `#### English Subsection | 中文小节`

**检查项**:
- 所有级别标题是否使用 `|` 分隔符
- 中英文顺序是否正确（英文在前，中文在后）
- 标题层级是否正确（#、##、###、####）

### 2. 正文段落格式审查

- [ ] **换行格式**: 正文段落使用换行分隔，**不使用** `|` 分隔符
- [ ] **空行要求**: 英文段落和中文段落之间**必须有空行**
- [ ] **纯英文段落**: 英文段落中**禁止出现中文字符**（如中文标点、中英混杂等）
- [ ] **纯中文段落**: 中文段落翻译完整，无遗漏

**检查项**:
- 每对英中文段落之间是否有空行
- 英文段落是否纯英文（无中文字符）
- 中文段落是否完整翻译原文内容

### 3. 有序列表格式审查

- [ ] **英文行格式**: `1. English item with description.`
- [ ] **中文行格式**: 无序号，直接文本
- [ ] **交错排列**: 英文项后紧跟中文译文

**检查项**:
- 英文行是否保留序号（`1.` `2.`）
- 中文行是否删除序号
- 列表项是否按"英文项→中文译文"交错排列
- 列表项翻译是否完整

### 4. 无序列表格式审查

- [ ] 保持原有的列表符号（`-`）
- [ ] 中英文对照完整
- [ ] 英文项后紧跟中文译文

**检查项**:
- 列表符号是否正确
- 每个列表项是否有中英文对照
- 是否按交错格式排列

### 5. 图片格式审查

- [ ] **原始 URL**: 使用 `https://www-cdn.anthropic.com/images/...`
- [ ] **禁止格式**: 禁止使用代理 URL（`_next/image?url=...`）
- [ ] **图片说明**: 添加中文图片说明

**检查项**:
- 图片 URL 是否为原始 www-cdn.anthropic.com 链接
- 是否包含中文图片描述
- 图片链接是否可访问

### 6. 链接格式审查

- [ ] **保留链接**: 保持 markdown 链接格式 `[Link text](https://...)`
- [ ] **资源链接**: 为提到的资源添加链接
  - 文档 (documentation, guide, cookbook)
  - API 参考 (API reference, docs.anthropic.com)
  - 博客文章 (blog post, SWE-bench)
  - 官网 (Developer Guide)

**检查项**:
- 链接是否可点击
- 提到的资源是否都有链接
- 链接格式是否正确

### 7. 代码块格式审查

- [ ] 保持原样，不翻译代码
- [ ] 代码示例保持原样
- [ ] 命令保持原样

**检查项**:
- 代码是否保持原样
- 文件名和术语是否正确保留

### 8. 术语一致性审查

- [ ] 专业术语翻译一致
- [ ] 参考术语表

**关键术语**:
- Model Context Protocol (MCP) | 模型上下文协议（MCP）
- Tool | 工具
- Agent | 智能体
- Deterministic systems | 确定性系统
- Non-deterministic systems | 非确定性系统
- Contract | 契约
- Affordances | 可供性
- Context | 上下文
- Ergonomic | 符合人体工程学（的）
- Prototype | 原型
- Evaluation | 评估
- MCP server | MCP 服务器
- Desktop extension (DXT) | 桌面扩展（DXT）
- API call | API 调用
- Prompt | 提示
- Response | 响应
- Knowledge base | 知识库
- Microservice | 微服务
- Sandbox environment | 沙箱环境
- Stress-test | 压力测试
- Verifier | 验证器
- Ground truth | 基本事实
- System prompt | 系统提示
- Chain-of-thought (CoT) | 思维链（CoT）
- Interleaved thinking | 交错思考
- Runtime | 运行时间
- Token consumption | 标记消耗
- Workflow | 工作流程
- Consolidate | 整合/合并
- Namespacing | 命名空间
- Prefix | 前缀
- Suffix | 后缀
- Context relevance | 上下文相关性
- Technical identifier | 技术标识符
- UUID | UUID
- Hallucination | 幻觉
- Retrieval task | 检索任务
- ResponseFormat | ResponseFormat（响应格式）
- Enum | 枚举
- Verbosity | 详细程度
- Pagination | 分页
- Range selection | 范围选择
- Truncation | 截断
- Input validation | 输入验证
- Error response | 错误响应
- Traceback | 回溯
- Token-efficient | 节省标记的
- Prompt-engineering | 提示工程
- Specialized query format | 专门的查询格式
- Niche terminology | 小众术语
- Data model | 数据模型
- SWE-bench Verified | SWE-bench Verified
- State-of-the-art | 最先进的
- Open-world access | 开放世界访问
- Destructive changes | 破坏性更改

### 9. 完整性审查

- [ ] 文章内容完整，无遗漏段落
- [ ] 所有图片都已翻译说明
- [ ] 所有章节都已翻译
- [ ] 脚注（Footnotes）已翻译

## 评分标准

### 技术维度 (50分)

| 检查项 | 分值 | 评分标准 |
|--------|------|----------|
| 标题格式正确性 | 10分 | 所有标题使用 `|` 分隔符，层级正确 |
| 正文格式正确性 | 20分 | 换行格式，空行分隔，无中文字符混杂 |
| 列表格式正确性 | 10分 | 有序列表中文行无序号，交错排列正确 |
| 代码块格式正确性 | 5分 | 代码保持原样，文件名正确 |
| 图片链接正确性 | 5分 | 使用原始 URL，图片说明完整 |

### 战略维度 (50分)

| 检查项 | 分值 | 评分标准 |
|--------|------|----------|
| 需求匹配度 | 15分 | 是否满足用户的翻译需求 |
| 格式规范一致性 | 20分 | 是否遵循 `.claude/rules/translation-format.md` |
| 翻译质量 | 10分 | 术语准确，表达流畅 |
| 可维护性 | 5分 | 文件命名、目录结构是否符合规范 |

### 综合评分

- **90-100分**: 通过 - 无需修改或仅做微小调整
- **75-89分**: 有条件通过 - 需要修复部分问题
- **60-74分**: 退回 - 需要重大修改
- **60分以下**: 退回 - 需要重新翻译

## 输出要求

请输出结构化的审查报告到 `.claude/review-report.md`，包含：

1. **综合评分**: X/100
2. **技术维度评分**: X/50
   - 标题格式正确性: X/10
   - 正文格式正确性: X/20
   - 列表格式正确性: X/10
   - 代码块格式正确性: X/5
   - 图片链接正确性: X/5
3. **战略维度评分**: X/50
   - 需求匹配度: X/15
   - 格式规范一致性: X/20
   - 翻译质量: X/10
   - 可维护性: X/5
4. **建议**: 通过 / 有条件通过 / 退回
5. **关键发现**: 发现的问题清单（如有）
6. **优点**: 做得好的地方
7. **修改建议**: 需要修改的具体内容和位置

---

**审查请求生成时间**: 2026-01-25
**任务ID**: #11
**文件**: 09-writing-tools-for-agents.md

请开始审查！
