# Codex

## 项目基本信息

- 项目全称：Claude Code & Codex Chinese Commentary Collection
- 仓库简称：CCCCCCC
- 项目定位：整理、翻译并维护 Claude Code 与 Codex 相关中文注释资料
- 当前重点：维护已完成迁移的记忆体系，并继续补充 `codex相关/` 内容

## 目录结构

- `claude-code相关/`：Claude Code 更新日志与 Anthropic Engineering 文章译文
- `claude-code相关/anthropic-engineering-articles/AGENTS.md`：该子目录的局部记忆文件
- `codex相关/`：Codex 相关资料与后续新增内容
- `.claude/commands/`：保留的辅助命令模板
- `.claude/rules/translation-format.md`：现有翻译排版规范
- `.claude/review-request.md`：审查请求模板
- `README.md`：面向读者的项目总览，应与本文件、`CHANGELOG.md`、`LAST_RUN.md` 保持一致
- `CHANGELOG.md`：版本与重要变更记录
- `LAST_RUN.md`：上一次工作的总结

## 技术栈与技术路线

- 文档主格式：Markdown
- 工作方式：以目录迁移、项目记忆维护、双语文档整理为主
- 记忆体系：根目录使用 `AGENTS.md` 与 `LAST_RUN.md`，子目录按需使用局部 `AGENTS.md`
- 现有辅助规范暂时保留在 `.claude/` 下，后续如有必要再继续迁移命名

## 当前状态

- 远端 `main` 已同步到本地
- 旧资料目录已迁移到 `claude-code相关/` 与 `codex相关/`
- 旧的 Claude 记忆入口已退役，改为 Codex 默认加载的记忆文件
- 本轮修改只迁移项目记忆组件，不改动译文正文主题

## 计划

- 检查 `README.md`、`CHANGELOG.md` 与 `LAST_RUN.md` 是否持续保持一致
- 继续补充 `codex相关/` 的资料内容与目录说明
- 视后续工作量决定是否将 `.claude/` 下辅助模板继续重命名

## 资源

- 根项目记忆：`AGENTS.md`
- 会话续接摘要：`LAST_RUN.md`
- 子目录记忆：`claude-code相关/anthropic-engineering-articles/AGENTS.md`
- 翻译规范：`.claude/rules/translation-format.md`
- 审查模板：`.claude/review-request.md`
