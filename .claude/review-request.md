# 翻译格式审查请求 - ID 14

## 项目基本信息

**项目名称**: Claude Code 中文指南合集 - Engineering 文章翻译
**文章**: 14-claude-code-sandboxing.md
**标题**: Making Claude Code more secure and autonomous with sandboxing
**主题**: Claude Code 沙箱安全特性
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
    └── 14-claude-code-sandboxing.md (本次翻译)
```

### 项目状态
- **已完成翻译**: 6/19 篇文章（32%）
- **格式规范**: `.claude/rules/translation-format.md`
- **上一次审查**: ID 15 评分 93/100（技术维度满分）

## 用户的原始需求

翻译 Anthropic Engineering 文章 ID 14，遵循项目的翻译格式规范，创建中英文双语对照版本。

## 本次工作内容与交付物

### 工作内容
1. 获取原文：https://www.anthropic.com/engineering/claude-code-sandboxing
2. 全文翻译，包含以下章节：
   - 引言：Claude Code 的权限模型和风险
   - Sandboxing 概述
   - 两个核心隔离机制（文件系统隔离、网络隔离）
   - 沙箱 bash 工具
   - 网页版 Claude Code
   - 入门指南
   - 致谢

### 交付物
- **文件**: `anthropic-engineering-articles/markdown/14-claude-code-sandboxing.md`
- **行数**: ~200 行
- **图片**: 2 张（已转换为原始 www-cdn.anthropic.com URL）
- **链接**: 添加了 docs、claude.com/code 等资源链接

## 需要审查的目标文件与范围

### 目标文件
```
anthropic-engineering-articles/markdown/14-claude-code-sandboxing.md
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

**检查项**:
- 英文行是否保留序号（`1.` `2.`）
- 中文行是否删除序号
- 列表项翻译是否完整

### 4. 无序列表格式审查

- [ ] 保持原有的列表符号（`-`）
- [ ] 中英文对照完整

**检查项**:
- 列表符号是否正确
- 每个列表项是否有中英文对照

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
  - 文档 (documentation, docs)
  - 官网 (claude.com/code, anthropic.com)
  - 快速入门 (quickstart)
  - API 参考
  - GitHub 仓库

**检查项**:
- 链接是否可点击
- 提到的资源是否都有链接
- 链接格式是否正确

### 7. 代码块格式审查

- [ ] 保持原样，不翻译代码
- [ ] 代码注释可以添加中文翻译

**检查项**:
- 代码是否保持原样
- 命令示例（如 `/sandbox`）是否保持原样

### 8. 表格格式审查

- [ ] 表格包含中英文对照
- [ ] 使用"英文 | 中文"的双语格式

**检查项**:
- 表头是否有中英文对照
- 表格内容是否有中英文对照

### 9. 术语一致性审查

- [ ] 专业术语翻译一致
- [ ] 参考术语表

**关键术语**:
- Sandboxing → 沙箱/沙箱化
- Filesystem isolation → 文件系统隔离
- Network isolation → 网络隔离
- Permission prompts → 权限提示/权限请求
- Prompt injection → 提示注入
- Approval fatigue → 审批疲劳
- Autonomous → 自主/自动化
- Bubblewrap → Bubblewrap (Linux沙箱工具)
- Seatbelt → Seatbelt (macOS沙箱工具)
- Unix domain socket → Unix域套接字
- Scoped credential → 作用域凭证

### 10. 完整性审查

- [ ] 文章内容完整，无遗漏段落
- [ ] 所有图片都已翻译说明
- [ ] 所有章节都已翻译

## 评分标准

### 技术维度 (50分)

| 检查项 | 分值 | 评分标准 |
|--------|------|----------|
| 标题格式正确性 | 10分 | 所有标题使用 `|` 分隔符，层级正确 |
| 正文格式正确性 | 20分 | 换行格式，空行分隔，无中文字符混杂 |
| 列表格式正确性 | 10分 | 有序列表中文行无序号，无序列表格式正确 |
| 代码块格式正确性 | 5分 | 代码保持原样，命令示例正确 |
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
**任务ID**: #6
**文件**: 14-claude-code-sandboxing.md

请开始审查！
