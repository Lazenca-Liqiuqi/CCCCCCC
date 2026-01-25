# 翻译格式审查请求 - ID 16

## 项目基本信息

**项目名称**: Claude Code Chinese Commentary Collection

**项目类型**: Anthropic Engineering Blog 文章中英文双语翻译

**文章**: 16-effective-harnesses-for-long-running-agents.md
**标题**: Effective Harnesses for Long-Running Agents

## 项目状态与当前任务

**当前阶段**: 修复已翻译文章的格式问题

**任务进度**:
- ✅ ID 19: 修复完成
- ✅ ID 18: 格式正确，无需修复
- ✅ ID 17: 修复完成
- ✅ ID 16: 修复完成（待审查）

## 用户原始需求

用户指出的格式问题：
1. 图片不能显示 - 图片链接使用代理URL格式
2. 缺少链接 - 文章中缺少某些链接
3. 标题翻译太突兀 - 应该使用"原文 | 译文"格式
4. 有序列表序号翻倍 - 中文行重复了序号
5. 表格只有译文、没有原文

**重要澄清**:
- **只有标题使用 `|` 格式**
- **正文使用换行格式，不使用 `|`**
- **有序列表中文行删除序号**

## 本次工作内容

### 工作目标

修复文章 `16-effective-harnesses-for-long-running-agents.md` 的翻译格式问题，使其符合 `.claude/rules/translation-format.md` 规范。

### 已完成的修复

**问题1：正文段落缺少空行**
- 在所有英文段落和中文段落之间添加了空行
- 影响范围：全文约 50+ 处

**已验证正确的部分**:
1. 标题格式：所有标题使用 `原文 | 译文` 格式 ✓
   - `# Effective Harnesses for Long-Running Agents | 长时间运行智能体的有效工具`
   - `## The Long-Running Agent Problem | 长时间运行智能体的问题`
   - `### Feature List | 功能列表`

2. 有序列表格式：英文行有序号，中文行无序号 ✓
   ```
   1. _Run `pwd` to see the directory you're working in._
   _运行 `pwd` 查看你正在工作的目录。_
   ```

3. 图片链接：使用原始 URL（www-cdn.anthropic.com）✓

4. 表格格式：表格包含中英文对照 ✓

### 交付物

待审查的文件: `anthropic-engineering-articles/markdown/16-effective-harnesses-for-long-running-agents.md`

## 审查目标与范围

### 目标文件

`/home/pc/project/Claude Code Chinese Commentary Collection/anthropic-engineering-articles/markdown/16-effective-harnesses-for-long-running-agents.md`

### 参考规范

`/home/pc/project/Claude Code Chinese Commentary Collection/.claude/rules/translation-format.md`

## 审查要点

### 1. 标题格式审查

**检查项**:
- [ ] 所有级别的标题（#、##、###）是否使用 `原文 | 译文` 格式
- [ ] 标题中是否包含英文原文和中文翻译
- [ ] `|` 前后是否有适当的空格

**预期示例**:
```markdown
# Effective Harnesses for Long-Running Agents | 长时间运行智能体的有效工具
## The Long-Running Agent Problem | 长时间运行智能体的问题
### Feature List | 功能列表
```

### 2. 正文段落格式审查

**检查项**:
- [ ] 正文段落是否使用换行格式（**不使用** `|`）
- [ ] 英文段落和中文段落之间是否有空行
- [ ] 是否存在遗漏的 `|` 分隔符

**预期示例**:
```markdown
As AI agents become more capable, developers are increasingly asking them to take on complex tasks.

随着 AI 智能体变得更强大，开发人员越来越要求它们承担复杂任务。
```

### 3. 有序列表格式审查

**检查项**:
- [ ] 英文行是否保留序号（`1. `）
- [ ] 中文行是否删除序号
- [ ] 是否存在序号重复的情况

**预期示例**:
```markdown
1. _Run `pwd` to see the directory you're working in._
_运行 `pwd` 查看你正在工作的目录。_

2. _Read the git logs and progress files._
_阅读 git 日志和进度文件。_
```

### 4. 图片链接审查

**检查项**:
- [ ] 图片链接是否使用原始 URL（www-cdn.anthropic.com）
- [ ] 是否存在代理 URL（example.com/_next/image?url=...）
- [ ] 图片说明是否有中文翻译

**预期示例**:
```markdown
![Image 1: Screenshots...](https://www-cdn.anthropic.com/images/...)
Claude 通过 Puppeteer MCP 服务器在测试时拍摄的屏幕截图。
```

### 5. 表格格式审查

**检查项**:
- [ ] 表格是否包含中英文对照
- [ ] 表头和内容是否正确格式化

### 6. 链接完整性审查

**检查项**:
- [ ] 文中提到的文档、资源是否有链接
- [ ] 链接是否可点击且指向正确地址

### 7. 代码块格式审查

**检查项**:
- [ ] 代码块是否正确格式化
- [ ] 代码示例是否有说明

### 8. 特殊格式审查

**检查项**:
- [ ] 强调文本（粗体、斜体）是否正确
- [ ] 分隔线 `---` 前后格式是否正确

## 评分标准

### 技术维度 (50分)

| 评分项 | 分值 | 评分标准 |
|--------|------|----------|
| 标题格式正确性 | 10 | 全部正确=10，部分正确=5-9，大部分错误=0-4 |
| 正文格式正确性 | 20 | 全部正确=20，部分正确=10-19，大部分错误=0-9 |
| 列表格式正确性 | 10 | 无重复序号=10，少量问题=5-9，严重问题=0-4 |
| 链接完整性 | 5 | 链接完整=5，部分缺失=2-4，严重缺失=0-1 |
| 图片链接正确性 | 5 | 全部正确=5，部分问题=2-4，严重问题=0-1 |

### 战略维度 (50分)

| 评分项 | 分值 | 评分标准 |
|--------|------|----------|
| 需求匹配度 | 15 | 完全符合用户要求=15，基本符合=8-14，不符合=0-7 |
| 格式规范一致性 | 20 | 完全符合规范=20，基本符合=10-19，不符合=0-9 |
| 可维护性 | 10 | 便于后续翻译=10，一般=5-9，困难=0-4 |
| 风险评估 | 5 | 低风险=5，中等风险=2-4，高风险=0-1 |

### 综合评分

- **90-100分**: 通过，格式完全正确
- **75-89分**: 有条件通过，需微调
- **60-74分**: 退回，需重新修复
- **0-59分**: 严重问题，需全面返工

## 决策建议

请 Codex 根据以上审查要点进行评估，并提供：

1. **技术维度评分** (0-50分)
2. **战略维度评分** (0-50分)
3. **综合评分** (0-100分)
4. **明确建议**: 通过 / 有条件通过 / 退回 / 已正确无需修改
5. **支持论据**: 详细说明评分理由
6. **关键发现**: 指出任何问题或改进建议
7. **修改记录**: 如发现问题，列出需要修改的具体位置

## 特别说明

**ID 16 文章特点**:
- 包含有序列表（带斜体的步骤说明）
- 包含代码块和代码示例
- 包含表格（中英文对照）
- 有图片和图片说明
- 有脚注部分

**审查重点**:
- 正文空行格式
- 有序列表的斜体格式
- 表格的中英文对照
- 脚注格式

---

**审查请求生成时间**: 2026-01-25
**任务ID**: #24
**文件**: 16-effective-harnesses-for-long-running-agents.md
