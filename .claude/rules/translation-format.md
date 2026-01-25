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

表格应该包含中英文对照：

| English Header | 中文表头 |
| --- | --- |
| English cell content | 英文单元格的中文翻译 |

## 代码块格式

代码块不需要翻译，保持原样。代码注释可以添加中文翻译：

```python
# English comment
# 中文翻译
def function():
    pass
```

## 链接格式

保留原始链接，不进行翻译：

```markdown
[Link text](https://example.com)
链接文本的中文翻译。
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

## 质量检查清单

- [ ] 所有标题使用 `|` 分隔符
- [ ] 正文段落使用换行，不使用 `|`
- [ ] 有序列表中文行无序号
- [ ] 图片链接使用原始URL
- [ ] 表格包含中英文对照
- [ ] 链接保持可点击状态
- [ ] 专业术语翻译一致（参考术语表）
