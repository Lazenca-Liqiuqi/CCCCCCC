# Codex CLI 技术手册

更新时间：2026-03-01 16:12


## codex

```bash
codex [OPTIONS] [PROMPT]
codex [OPTIONS] <COMMAND> [ARGS]
```

说明：Codex CLI 主入口；未指定子命令时启动交互式会话。

### Arguments

- `[PROMPT]`：可选初始提示词。

### Options

#### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。
- `-p, --profile <CONFIG_PROFILE>`：指定 `config.toml` 中的配置档作为默认参数集合。

#### 模型类

- `-m, --model <MODEL>`：指定本次运行使用的模型。
- `--oss`：切换到本地开源模型提供方（等价于 `-c model_provider=oss`），并校验本地服务可用性。
- `--local-provider <OSS_PROVIDER>`：指定本地 OSS 提供方（`lmstudio` 或 `ollama`）。
- `-i, --image <FILE>...`：附加一张或多张图片输入。

#### 沙箱与安全类

- `-s, --sandbox <SANDBOX_MODE>`：设置命令执行沙箱策略：`read-only`、`workspace-write`、`danger-full-access`。
- `-a, --ask-for-approval <APPROVAL_POLICY>`：设置命令执行审批策略：`untrusted`、`on-failure`（已弃用）、`on-request`、`never`。
- `--full-auto`：启用低摩擦自动执行预设；不同命令下会展开为对应的自动审批/沙箱组合。
- `--dangerously-bypass-approvals-and-sandbox`：跳过所有确认并关闭沙箱直接执行；仅建议在外部已隔离环境使用（极高风险）。

#### 目录与权限类

- `-C, --cd <DIR>`：将代理工作根目录切换到指定目录。
- `--add-dir <DIR>`：为当前会话追加额外可写目录（与主工作区并列）。

#### 输出与格式类

- `--search`：启用实时网页搜索工具（模型可直接调用 `web_search`）。
- `--no-alt-screen`：关闭备用屏缓冲，改为内联模式并保留终端滚动历史。

#### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

### codex exec

```bash
codex exec [OPTIONS] [PROMPT] [COMMAND]
```

说明：以非交互模式执行一次任务并退出。

#### Arguments

- `[PROMPT]`：初始指令；若为 `-` 则从 stdin 读取。

#### Options

##### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。
- `-p, --profile <CONFIG_PROFILE>`：指定 `config.toml` 中的配置档作为默认参数集合。

##### 模型类

- `-m, --model <MODEL>`：指定本次运行使用的模型。
- `--oss`：切换到本地开源模型提供方（等价于 `-c model_provider=oss`），并校验本地服务可用性。
- `--local-provider <OSS_PROVIDER>`：指定本地 OSS 提供方（`lmstudio` 或 `ollama`）。
- `-i, --image <FILE>...`：附加一张或多张图片输入。

##### 沙箱与安全类

- `-s, --sandbox <SANDBOX_MODE>`：设置命令执行沙箱策略：`read-only`、`workspace-write`、`danger-full-access`。
- `--full-auto`：启用低摩擦自动执行预设；不同命令下会展开为对应的自动审批/沙箱组合。
- `--dangerously-bypass-approvals-and-sandbox`：跳过所有确认并关闭沙箱直接执行；仅建议在外部已隔离环境使用（极高风险）。

##### 目录与权限类

- `-C, --cd <DIR>`：将代理工作根目录切换到指定目录。
- `--skip-git-repo-check`：允许在非 Git 仓库目录执行命令。
- `--add-dir <DIR>`：为当前会话追加额外可写目录（与主工作区并列）。
- `--ephemeral`：以临时模式运行，不在本地持久化会话文件。

##### 输出与格式类

- `--output-schema <FILE>`：指定最终响应结构的 JSON Schema 文件路径。
- `--color <COLOR>`：设置输出颜色策略：`always`、`never`、`auto`。
- `--progress-cursor`：在 exec 模式强制使用光标式进度更新。
- `--json`：使用 JSON（或 JSONL）输出，便于脚本消费。
- `-o, --output-last-message <FILE>`：将最后一条助手消息写入指定文件。

##### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex exec resume

```bash
codex exec resume [OPTIONS] [SESSION_ID] [PROMPT]
```

说明：按会话 ID（或最近会话）恢复一次 exec 会话。

##### Arguments

- `[SESSION_ID]`：会话 UUID 或线程名；省略时可配合 `--last`。
- `[PROMPT]`：恢复后发送提示词；`-` 表示从 stdin 读取。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。
- `--last`：直接使用最近一次会话，不进入会话选择器。
- `--all`：显示全部历史会话，关闭当前目录过滤（部分命令会同时展示 CWD 列）。

###### 模型类

- `-m, --model <MODEL>`：指定本次运行使用的模型。
- `-i, --image <FILE>`：附加单张图片输入。

###### 沙箱与安全类

- `--full-auto`：启用低摩擦自动执行预设；不同命令下会展开为对应的自动审批/沙箱组合。
- `--dangerously-bypass-approvals-and-sandbox`：跳过所有确认并关闭沙箱直接执行；仅建议在外部已隔离环境使用（极高风险）。

###### 目录与权限类

- `--skip-git-repo-check`：允许在非 Git 仓库目录执行命令。
- `--ephemeral`：以临时模式运行，不在本地持久化会话文件。

###### 输出与格式类

- `--json`：使用 JSON（或 JSONL）输出，便于脚本消费。
- `-o, --output-last-message <FILE>`：将最后一条助手消息写入指定文件。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex exec review

```bash
codex exec review [OPTIONS] [PROMPT]
```

说明：对当前仓库执行一次非交互代码审查。

##### Arguments

- `[PROMPT]`：自定义审查说明；`-` 表示从 stdin 读取。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。
- `--uncommitted`：审查 staged、unstaged 与 untracked 变更。
- `--base <BRANCH>`：按指定基线分支进行差异审查。
- `--commit <SHA>`：仅审查指定提交引入的改动。
- `--title <TITLE>`：设置审查摘要中显示的标题。

###### 模型类

- `-m, --model <MODEL>`：指定本次运行使用的模型。

###### 沙箱与安全类

- `--full-auto`：启用低摩擦自动执行预设；不同命令下会展开为对应的自动审批/沙箱组合。
- `--dangerously-bypass-approvals-and-sandbox`：跳过所有确认并关闭沙箱直接执行；仅建议在外部已隔离环境使用（极高风险）。

###### 目录与权限类

- `--skip-git-repo-check`：允许在非 Git 仓库目录执行命令。
- `--ephemeral`：以临时模式运行，不在本地持久化会话文件。

###### 输出与格式类

- `--json`：使用 JSON（或 JSONL）输出，便于脚本消费。
- `-o, --output-last-message <FILE>`：将最后一条助手消息写入指定文件。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex exec help

```bash
codex exec help
```

说明：显示 `codex exec` 的帮助信息。


### codex review

```bash
codex review [OPTIONS] [PROMPT]
```

说明：以顶层入口执行一次非交互代码审查。

#### Arguments

- `[PROMPT]`：自定义审查说明；`-` 表示从 stdin 读取。

#### Options

##### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。
- `--uncommitted`：审查 staged、unstaged 与 untracked 变更。
- `--base <BRANCH>`：按指定基线分支进行差异审查。
- `--commit <SHA>`：仅审查指定提交引入的改动。
- `--title <TITLE>`：设置审查摘要中显示的标题。

##### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

### codex login

```bash
codex login [OPTIONS] [COMMAND]
```

说明：管理登录认证流程。

#### Options

##### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

##### 沙箱与安全类

- `--with-api-key`：从 stdin 读取 API Key 完成登录。
- `--device-auth`：使用设备授权流程进行登录。

##### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex login status

```bash
codex login status [OPTIONS]
```

说明：显示当前登录状态。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex login help

```bash
codex login help
```

说明：显示 `codex login` 子命令帮助。


### codex logout

```bash
codex logout [OPTIONS]
```

说明：移除本地存储的认证凭据。

#### Options

##### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

##### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

### codex mcp

```bash
codex mcp [OPTIONS] <COMMAND>
```

说明：管理 Codex 外部 MCP 服务器配置。

#### Options

##### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

##### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex mcp list

```bash
codex mcp list [OPTIONS]
```

说明：列出已配置的 MCP 服务器。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

###### 输出与格式类

- `--json`：使用 JSON（或 JSONL）输出，便于脚本消费。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex mcp get

```bash
codex mcp get [OPTIONS] <NAME>
```

说明：查看指定 MCP 服务器配置详情。

##### Arguments

- `<NAME>`：要显示的 MCP 服务器名称。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

###### 输出与格式类

- `--json`：使用 JSON（或 JSONL）输出，便于脚本消费。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex mcp add

```bash
codex mcp add [OPTIONS] <NAME> (--url <URL> | -- <COMMAND>...)
```

说明：新增一个 MCP 服务器配置。

##### Arguments

- `<NAME>`：MCP 服务器配置名称。
- `[COMMAND]...`：启动 MCP 服务器命令；使用 `--url` 时为 HTTP 服务器模式。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。
- `--env <KEY=VALUE>`：为 stdio 模式 MCP 服务器注入环境变量。
- `--url <URL>`：将 MCP 服务器配置为可流式 HTTP 端点。
- `--bearer-token-env-var <ENV_VAR>`：指定环境变量名，从中读取 HTTP Bearer Token。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex mcp remove

```bash
codex mcp remove [OPTIONS] <NAME>
```

说明：删除指定 MCP 服务器配置。

##### Arguments

- `<NAME>`：要移除的 MCP 服务器配置名称。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex mcp login

```bash
codex mcp login [OPTIONS] <NAME>
```

说明：对指定 MCP 服务器执行 OAuth 登录。

##### Arguments

- `<NAME>`：要进行 OAuth 认证的 MCP 服务器名称。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。
- `--scopes <SCOPE,SCOPE>`：登录 MCP 时请求的 OAuth scopes（逗号分隔）。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex mcp logout

```bash
codex mcp logout [OPTIONS] <NAME>
```

说明：注销指定 MCP 服务器认证。

##### Arguments

- `<NAME>`：要注销认证的 MCP 服务器名称。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex mcp help

```bash
codex mcp help
```

说明：显示 `codex mcp` 子命令帮助。


### codex mcp-server

```bash
codex mcp-server [OPTIONS]
```

说明：以 stdio 方式将 Codex 启动为 MCP 服务器。

#### Options

##### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

##### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

### codex app-server

```bash
codex app-server [OPTIONS] [COMMAND]
```

说明：运行 app-server 或相关工具（实验特性）。

#### Options

##### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

##### 输出与格式类

- `--listen <URL>`：设置 app-server 传输端点，支持 `stdio://` 或 `ws://IP:PORT`。

##### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。
- `--analytics-default-enabled`：将 app-server 的 analytics 默认值设为启用（用户仍可在 config.toml 显式关闭）。

#### codex app-server generate-ts

```bash
codex app-server generate-ts [OPTIONS] --out <DIR>
```

说明：生成 app-server 协议的 TypeScript 绑定（实验特性）。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。
- `-o, --out <DIR>`：指定生成文件输出目录。
- `-p, --prettier <PRETTIER_BIN>`：指定 Prettier 可执行文件路径（用于格式化生成结果）。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。
- `--experimental`：在生成结果中包含实验方法和字段。

#### codex app-server generate-json-schema

```bash
codex app-server generate-json-schema [OPTIONS] --out <DIR>
```

说明：生成 app-server 协议的 JSON Schema（实验特性）。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。
- `-o, --out <DIR>`：指定生成文件输出目录。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。
- `--experimental`：在生成结果中包含实验方法和字段。

#### codex app-server help

```bash
codex app-server help
```

说明：显示 `codex app-server` 子命令帮助。


### codex completion

```bash
codex completion [OPTIONS] [SHELL]
```

说明：生成指定 shell 的补全脚本。

#### Arguments

- `[SHELL]`：要生成补全脚本的 Shell，默认 `bash`。可选值：`bash`、`elvish`、`fish`、`powershell`、`zsh`。

#### Options

##### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

##### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

### codex sandbox

```bash
codex sandbox [OPTIONS] <COMMAND>
```

说明：在 Codex 提供的沙箱环境中运行命令。

#### Options

##### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

##### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex sandbox macos

```bash
codex sandbox macos [OPTIONS] [COMMAND]...
```

说明：在 macOS Seatbelt 沙箱中执行命令。

##### Arguments

- `[COMMAND]...`：在 Seatbelt 沙箱中执行的完整命令参数。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

###### 沙箱与安全类

- `--full-auto`：启用低摩擦自动执行预设；不同命令下会展开为对应的自动审批/沙箱组合。
- `--log-denials`：命令运行期间采集并输出沙箱拒绝日志（macOS）。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex sandbox linux

```bash
codex sandbox linux [OPTIONS] [COMMAND]...
```

说明：在 Linux Landlock+seccomp 沙箱中执行命令。

##### Arguments

- `[COMMAND]...`：在 Landlock 沙箱中执行的完整命令参数。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

###### 沙箱与安全类

- `--full-auto`：启用低摩擦自动执行预设；不同命令下会展开为对应的自动审批/沙箱组合。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex sandbox windows

```bash
codex sandbox windows [OPTIONS] [COMMAND]...
```

说明：在 Windows 受限令牌沙箱中执行命令。

##### Arguments

- `[COMMAND]...`：在 Windows 受限令牌沙箱中执行的完整命令参数。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

###### 沙箱与安全类

- `--full-auto`：启用低摩擦自动执行预设；不同命令下会展开为对应的自动审批/沙箱组合。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex sandbox help

```bash
codex sandbox help
```

说明：显示 `codex sandbox` 子命令帮助。


### codex debug

```bash
codex debug [OPTIONS] <COMMAND>
```

说明：调试相关工具集合。

#### Options

##### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

##### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex debug app-server

```bash
codex debug app-server [OPTIONS] <COMMAND>
```

说明：用于 app-server 的调试工具入口。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

##### codex debug app-server send-message-v2

```bash
codex debug app-server send-message-v2 [OPTIONS] <USER_MESSAGE>
```

说明：向调试中的 app-server 发送一条用户消息。

###### Options

####### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

####### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

##### codex debug app-server help

```bash
codex debug app-server help
```

说明：显示 `codex debug app-server` 子命令帮助。

#### codex debug help

```bash
codex debug help
```

说明：显示 `codex debug` 子命令帮助。


### codex apply

```bash
codex apply [OPTIONS] <TASK_ID>
```

说明：将 Codex 任务生成的 diff 以 `git apply` 应用到本地工作树。

#### Options

##### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

##### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

### codex resume

```bash
codex resume [OPTIONS] [SESSION_ID] [PROMPT]
```

说明：恢复历史交互会话（可直接续接最近会话）。

#### Arguments

- `[SESSION_ID]`：会话 UUID 或线程名；省略时可配合 `--last`。
- `[PROMPT]`：可选初始提示词。

#### Options

##### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。
- `-p, --profile <CONFIG_PROFILE>`：指定 `config.toml` 中的配置档作为默认参数集合。
- `--last`：直接使用最近一次会话，不进入会话选择器。
- `--all`：显示全部历史会话，关闭当前目录过滤（部分命令会同时展示 CWD 列）。

##### 模型类

- `-i, --image <FILE>...`：附加一张或多张图片输入。
- `-m, --model <MODEL>`：指定本次运行使用的模型。
- `--oss`：切换到本地开源模型提供方（等价于 `-c model_provider=oss`），并校验本地服务可用性。
- `--local-provider <OSS_PROVIDER>`：指定本地 OSS 提供方（`lmstudio` 或 `ollama`）。

##### 沙箱与安全类

- `-s, --sandbox <SANDBOX_MODE>`：设置命令执行沙箱策略：`read-only`、`workspace-write`、`danger-full-access`。
- `-a, --ask-for-approval <APPROVAL_POLICY>`：设置命令执行审批策略：`untrusted`、`on-failure`（已弃用）、`on-request`、`never`。
- `--full-auto`：启用低摩擦自动执行预设；不同命令下会展开为对应的自动审批/沙箱组合。
- `--dangerously-bypass-approvals-and-sandbox`：跳过所有确认并关闭沙箱直接执行；仅建议在外部已隔离环境使用（极高风险）。

##### 目录与权限类

- `-C, --cd <DIR>`：将代理工作根目录切换到指定目录。
- `--add-dir <DIR>`：为当前会话追加额外可写目录（与主工作区并列）。

##### 输出与格式类

- `--search`：启用实时网页搜索工具（模型可直接调用 `web_search`）。
- `--no-alt-screen`：关闭备用屏缓冲，改为内联模式并保留终端滚动历史。

##### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

### codex fork

```bash
codex fork [OPTIONS] [SESSION_ID] [PROMPT]
```

说明：基于历史交互会话创建分叉会话。

#### Arguments

- `[SESSION_ID]`：会话 UUID；省略时可配合 `--last`。
- `[PROMPT]`：可选初始提示词。

#### Options

##### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。
- `-p, --profile <CONFIG_PROFILE>`：指定 `config.toml` 中的配置档作为默认参数集合。
- `--last`：直接使用最近一次会话，不进入会话选择器。
- `--all`：显示全部历史会话，关闭当前目录过滤（部分命令会同时展示 CWD 列）。

##### 模型类

- `-i, --image <FILE>...`：附加一张或多张图片输入。
- `-m, --model <MODEL>`：指定本次运行使用的模型。
- `--oss`：切换到本地开源模型提供方（等价于 `-c model_provider=oss`），并校验本地服务可用性。
- `--local-provider <OSS_PROVIDER>`：指定本地 OSS 提供方（`lmstudio` 或 `ollama`）。

##### 沙箱与安全类

- `-s, --sandbox <SANDBOX_MODE>`：设置命令执行沙箱策略：`read-only`、`workspace-write`、`danger-full-access`。
- `-a, --ask-for-approval <APPROVAL_POLICY>`：设置命令执行审批策略：`untrusted`、`on-failure`（已弃用）、`on-request`、`never`。
- `--full-auto`：启用低摩擦自动执行预设；不同命令下会展开为对应的自动审批/沙箱组合。
- `--dangerously-bypass-approvals-and-sandbox`：跳过所有确认并关闭沙箱直接执行；仅建议在外部已隔离环境使用（极高风险）。

##### 目录与权限类

- `-C, --cd <DIR>`：将代理工作根目录切换到指定目录。
- `--add-dir <DIR>`：为当前会话追加额外可写目录（与主工作区并列）。

##### 输出与格式类

- `--search`：启用实时网页搜索工具（模型可直接调用 `web_search`）。
- `--no-alt-screen`：关闭备用屏缓冲，改为内联模式并保留终端滚动历史。

##### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

### codex cloud

```bash
codex cloud [OPTIONS] [COMMAND]
```

说明：浏览 Codex Cloud 任务并在本地应用变更（实验特性）。

#### Options

##### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

##### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex cloud exec

```bash
codex cloud exec [OPTIONS] --env <ENV_ID> [QUERY]
```

说明：不启动 TUI，直接提交一条 Codex Cloud 任务。

##### Arguments

- `[QUERY]`：在 Codex Cloud 执行的任务提示词。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。
- `--env <ENV_ID>`：指定（或筛选）Codex Cloud 环境 ID。
- `--attempts <ATTEMPTS>`：设置云端执行尝试次数（best-of-N），默认 1。
- `--branch <BRANCH>`：指定 Codex Cloud 任务运行分支；默认使用当前分支。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex cloud status

```bash
codex cloud status [OPTIONS] <TASK_ID>
```

说明：查看指定 Codex Cloud 任务状态。

##### Arguments

- `<TASK_ID>`：待检查状态的 Codex Cloud 任务 ID。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex cloud list

```bash
codex cloud list [OPTIONS]
```

说明：列出 Codex Cloud 任务。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。
- `--env <ENV_ID>`：指定（或筛选）Codex Cloud 环境 ID。
- `--limit <N>`：限制列表返回条数（例如 cloud list 为 1-20）。
- `--cursor <CURSOR>`：使用上一页返回的游标继续分页拉取任务。

###### 输出与格式类

- `--json`：使用 JSON（或 JSONL）输出，便于脚本消费。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex cloud apply

```bash
codex cloud apply [OPTIONS] <TASK_ID>
```

说明：将指定 Codex Cloud 任务的 diff 应用到本地。

##### Arguments

- `<TASK_ID>`：要应用的 Codex Cloud 任务 ID。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。
- `--attempt <N>`：指定要查看或应用的任务尝试序号（1 起始）。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex cloud diff

```bash
codex cloud diff [OPTIONS] <TASK_ID>
```

说明：查看指定 Codex Cloud 任务的统一 diff。

##### Arguments

- `<TASK_ID>`：要查看差异的 Codex Cloud 任务 ID。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。
- `--attempt <N>`：指定要查看或应用的任务尝试序号（1 起始）。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex cloud help

```bash
codex cloud help
```

说明：显示 `codex cloud` 子命令帮助。


### codex features

```bash
codex features [OPTIONS] <COMMAND>
```

说明：查看和管理特性开关。

#### Options

##### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

##### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex features list

```bash
codex features list [OPTIONS]
```

说明：列出特性及其阶段与当前生效状态。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex features enable

```bash
codex features enable [OPTIONS] <FEATURE>
```

说明：在配置中启用指定特性。

##### Arguments

- `<FEATURE>`：要设置的特性键（例如 `unified_exec`）。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex features disable

```bash
codex features disable [OPTIONS] <FEATURE>
```

说明：在配置中禁用指定特性。

##### Arguments

- `<FEATURE>`：要设置的特性键（例如 `unified_exec`）。

##### Options

###### 配置类

- `-c, --config <key=value>`：覆盖 `~/.codex/config.toml` 配置；支持点路径，值按 TOML 解析（失败则按字符串）。

###### 特性开关类

- `--enable <FEATURE>`：启用实验特性（可重复），等价于 `-c features.<name>=true`。
- `--disable <FEATURE>`：禁用实验特性（可重复），等价于 `-c features.<name>=false`。

#### codex features help

```bash
codex features help
```

说明：显示 `codex features` 子命令帮助。


### codex help

```bash
codex help [COMMAND]...
```

说明：打印命令帮助或指定子命令帮助。

#### Arguments

- `[COMMAND]...`：输出指定子命令帮助。

