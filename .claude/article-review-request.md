# Engineering 文章内容完整性审查请求

## 任务说明

请审查以下6篇已抓取的 Anthropic Engineering Blog 文章，验证本地文件内容是否与网页上的原始文章完全一致。

## 审查范围

### 新抓取的6篇文章

| 序号 | 文件名 | 标题 | 网页URL |
|------|--------|------|---------|
| 1 | `03-swe-bench-verified-claude-3.5-sonnet.md` | Introducing SWE Bench Verified | https://www.anthropic.com/research/swe-bench-sonnet |
| 2 | `05-think-tool-complex-situations.md` | Think tool: Helping Claude navigate complex situations | https://www.anthropic.com/engineering/claude-think-tool |
| 3 | `07-desktop-extensions-mcp-server-installation.md` | Desktop extensions: MCP server installation | https://www.anthropic.com/engineering/desktop-extensions |
| 4 | `12-writing-effective-tools-for-agents.md` | Writing Effective Tools for Agents | https://www.anthropic.com/engineering/writing-tools-for-agents |
| 5 | `14-beyond-permission-prompts.md` | Beyond Permission Prompts | https://claude.com/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous |
| 6 | `16-advanced-tool-use-on-claude-developer-platform.md` | Advanced Tool Use | https://www.anthropic.com/engineering/advanced-tool-use |

## 审查要素

请逐篇检查以下内容元素是否完整、准确：

### 1. 文字内容
- [ ] 标题完整无缺
- [ ] 正文段落完整，无遗漏
- [ ] 无多余或错误的内容
- [ ] 格式排版正确（标题层级、段落换行）

### 2. 图片内容
- [ ] 所有图片都已保留（图片URL或markdown图片语法）
- [ ] 图片alt文本完整
- [ ] 图片数量与网页一致

### 3. 代码块
- [ ] 所有代码块都已保留
- [ ] 代码语法高亮标记正确（如```python, ```javascript）
- [ ] 代码内容完整无截断
- [ ] 代码缩进和格式正确

### 4. 链接
- [ ] 所有外部链接都已保留
- [ ] 内部锚点链接完整
- [ ] 链接URL正确无误

### 5. 特殊格式元素
- [ ] 引用块（blockquote）格式正确
- [ ] 列表（有序/无序）格式完整
- [ ] 表格结构正确
- [ ] 加粗、斜体等markdown格式正确

### 6. 文章元数据
- [ ] 发布日期
- [ ] 作者信息
- [ ] 文章标签/分类

## 审查方法

1. **访问原始网页**：使用提供的URL访问每篇文章的原始网页
2. **对比本地文件**：读取 `anthropic-engineering-articles/` 目录下对应的 `.md` 文件
3. **逐项验证**：按照上述审查要素清单进行逐项对比
4. **记录差异**：如发现任何差异或不一致，请详细记录

## 输出要求

请为每篇文章提供审查报告，格式如下：

```markdown
## [序号] [文件名]

### 审查结果
✅ 通过 / ⚠️ 存在问题

### 详细检查
- 文字内容：[通过/存在问题]
- 图片内容：[数量/状态]
- 代码块：[数量/状态]
- 链接：[状态]
- 特殊格式：[状态]

### 发现的问题（如有）
[如有差异或问题，请详细说明]

### 建议
[如需修正，请给出具体建议]
```

## 审查目标

确保本地抓取的文章内容：
1. **完整性**：无内容遗漏
2. **准确性**：与原始网页一致
3. **可用性**：格式正确，可用于后续翻译工作

---

**注意**：这是为后续翻译工作准备的质量控制步骤，请确保审查的准确性。
