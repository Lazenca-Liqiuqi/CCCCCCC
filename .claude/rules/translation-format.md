# Engineering 文章翻译格式规范

## 基本原则

中英文双语对照，保持原文内容的完整性和可读性。

## 标题格式

所有级别的标题使用 `|` 分隔符：

```markdown
# English Title | 中文标题
## English Subtitle | 中文副标题
### English Section | 中文章节
```

## 正文段落格式

使用换行分隔，**不使用** `|` 分隔符：

```markdown
English paragraph here.

中文段落在这里。
```

**重要**：
- 英文段落和中文段落之间**必须有空行**
- 英文段落中**禁止出现中文字符**（如中文标点、中英混杂等）
- 中文段落中禁止出现英文单词未翻译的情况（专有名词除外）

## 有序列表格式

英文行保留序号，中文行删除序号：

```markdown
1. First English item with description.
第一个英文项目的中文翻译。

2. Second English item with description.
第二个英文项目的中文翻译。
```

**注意**：中文行不要序号，避免重复编号。

## 无序列表格式

保持原有的列表符号：

```markdown
- English bullet point.
- 英文项目符号的中文翻译。
```

## 图片格式

使用原始图片链接，不使用代理URL：

```markdown
![Image description: Alt text](https://www-cdn.anthropic.com/images/...)
中文图片说明。
```

**禁止格式**：
```markdown
![Alt text](https://example.com/_next/image?url=...)
```

## 表格格式

表格应该包含中英文对照，使用"英文 | 中文"的双语格式：

| English Header | 中文表头 |
| --- | --- |
| English cell content | 英文单元格的中文翻译 |

**复杂表格**：对于多列表格，使用英文和中文列对照：

| English Category | 英文分类 | English Description | 英文描述 | Chinese Value | 中文值 |
| --- | --- | --- | --- | --- | --- |
| Category data | 分类数据 | Description text | 描述文本 | Value data | 数值数据 |

**禁止**：表格中只有中文或只有英文的行

## 代码块格式

代码块不需要翻译，保持原样。代码注释可以添加中文翻译：

```python
# English comment
# 中文翻译
def function():
    pass
```

**禁止格式**：
```python
# English comment | code_here  # 禁止用 | 混合注释和代码
```

## 链接格式

保留原始链接，不进行翻译：

```markdown
[Link text](https://example.com)
链接文本的中文翻译。
```

**必须添加链接的资源类型**：
- 文档 (documentation, guide, tutorial)
- 快速入门 (quickstart)
- API 参考 (API reference)
- 官网或招聘页面 (anthropic.com/careers)
- GitHub 仓库或文件
- 博客文章或技术资源

**示例**：
```markdown
You can find code examples in the [quickstart](https://docs.anthropic.com/...).
你可以在快速入门中找到代码示例。
```

## 特殊情况处理

### 长段落
超过200字的段落可以在英文和中文之间添加空行提高可读性。

### 代码示例
代码示例的说明文字使用换行格式：

```markdown
Here is an example:
这是一个示例：
```

### 引用块
引用块保持原有格式，添加中文翻译：

```markdown
> English quote text
> 英文引用的中文翻译
```

## 常见问题清单

基于实际修复经验，以下是需要特别注意的问题：

### 1. 正文格式问题
- **中英文段落之间缺少空行** - 这是最常见的系统性问题
- **英文段落中出现中文字符** - 如 "gather上下文" 应改为 "gather context"
- **使用 `|` 分隔正文** - 只有标题使用 `|`，正文必须用换行

### 2. 标题格式问题
- **步骤标题缺少 `|`** - `#### 1. English title` 应改为 `#### 1. English title | 中文标题`
- **子标题缺少 `|`** - 所有 `###` 和 `####` 标题都需要双语格式
- **中英文顺序错误** - 应该是 "英文 | 中文"

### 3. 代码块问题
- **注释和代码用 `|` 混合** - `# Comment | code` 应分离为两行
- **缺少中文注释翻译** - 注释应该有中英文对照

### 4. 列表问题
- **列表项缺少中文翻译** - 英文列表项后应该有对应的中文翻译
- **中文行重复序号** - 中文行不应该有 `1.` `2.` 等序号

### 5. 链接问题
- **纯文本引用缺少链接** - quickstart、documentation、careers 等应该有链接
- **链接不可点击** - 确保 `[]()` 格式正确

### 6. 表格问题
- **只有中文内容** - 表格应该是英文 | 中文的双语对照
- **表头只有中文** - 每列都应该有英文和中文表头

## 质量检查清单

### 基础格式
- [ ] 所有标题（#、##、###、####）使用 `|` 分隔符
- [ ] 正文段落使用换行，不使用 `|`
- [ ] 英文段落和中文段落之间有空行
- [ ] 有序列表中文行无序号

### 内容质量
- [ ] 图片链接使用原始 URL（www-cdn.anthropic.com）
- [ ] 表格包含中英文对照
- [ ] 链接保持可点击状态
- [ ] 代码块注释不与代码混合

### 完整性检查
- [ ] 文中提到的资源都有链接（文档、API、仓库等）
- [ ] 英文段落中没有中文字符
- [ ] 中文段落翻译完整，无遗漏
- [ ] 专业术语翻译一致（参考术语表）
