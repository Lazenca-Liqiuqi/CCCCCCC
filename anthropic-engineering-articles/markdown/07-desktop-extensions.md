# Claude Desktop Extensions: One-click MCP server installation for Claude Desktop | Claude Desktop 扩展：一键安装 MCP 服务器

Claude Desktop Extensions: One-click MCP server installation for Claude Desktop

Claude Desktop 扩展：一键安装 MCP 服务器

---

When we released the Model Context Protocol (MCP) last year, we saw developers build amazing local servers that gave Claude access to everything from file systems to databases. But we kept hearing the same feedback: installation was too complex. Users needed developer tools, had to manually edit configuration files, and often got stuck on dependency issues.

去年当我们发布模型上下文协议（MCP）时，看到开发者构建了令人惊叹的本地服务器，让 Claude 能够访问从文件系统到数据库的各种资源。但我们一直听到同样的反馈：安装太复杂了。用户需要开发者工具、必须手动编辑配置文件，并且经常在依赖问题上遇到困难。

Today, we're introducing Desktop Extensions—a new packaging format that makes installing MCP servers as simple as clicking a button.

今天，我们推出了 Desktop Extensions——一种新的打包格式，让安装 MCP 服务器变得像点击按钮一样简单。

## Addressing the MCP installation problem | 解决 MCP 安装问题

Local MCP servers unlock powerful capabilities for Claude Desktop users. They can interact with local applications, access private data, and integrate with development tools—all while keeping data on the user's machine. However, the current installation process creates significant barriers:

本地 MCP 服务器为 Claude Desktop 用户解锁了强大的功能。它们可以与本地应用程序交互、访问私有数据、与开发工具集成——同时所有数据都保留在用户的机器上。然而，当前的安装过程构成了重大障碍：

- Developer tools required: Users need Node.js, Python, or other runtimes installed

- 需要开发者工具：用户需要安装 Node.js、Python 或其他运行时

- Manual configuration: Each server requires editing JSON configuration files

- 手动配置：每个服务器都需要编辑 JSON 配置文件

- Dependency management: Users must resolve package conflicts and version mismatches

- 依赖管理：用户必须解决包冲突和版本不匹配问题

- No discovery mechanism: Finding useful MCP servers requires searching GitHub

- 无发现机制：查找有用的 MCP 服务器需要搜索 GitHub

- Update complexity: Keeping servers current means manual reinstallation

- 更新复杂性：保持服务器最新意味着手动重新安装

These friction points meant that MCP servers, despite their power, remained largely inaccessible to non-technical users.

这些摩擦点意味着 MCP 服务器虽然功能强大，但仍然主要对非技术用户不可及。

## Introducing Desktop Extensions | 介绍 Desktop Extensions

Desktop Extensions (`.mcpb` files) solve these problems by bundling an entire MCP server—including all dependencies—into a single installable package. Here's what changes for users:

Desktop Extensions（`.mcpb` 文件）通过将整个 MCP 服务器——包括所有依赖项——打包到单个可安装包中来解决这些问题。以下是用户体验的变化：

**Before:**

**之前：**

```
# Install Node.js first
# 首先安装 Node.js
npm install -g @example/mcp-server
# Edit ~/.claude/claude_desktop_config.json manually
# 手动编辑 ~/.claude/claude_desktop_config.json
# Restart Claude Desktop
# 重启 Claude Desktop
# Hope it works
# 希望它能工作
```

**After:**

**之后：**

1. Download a `.mcpb` file

下载 `.mcpb` 文件

2. Double-click to open with Claude Desktop

双击用 Claude Desktop 打开

3. Click "Install"

点击"安装"

That's it. No terminal, no configuration files, no dependency conflicts.

就是这样。无需终端，无需配置文件，无需依赖冲突。

## Architecture overview | 架构概览

A Desktop Extension is a zip archive containing the local MCP server as well as a `manifest.json`, which describes everything Claude Desktop and other apps supporting desktop extensions need to know.

Desktop Extension 是一个 zip 归档文件，包含本地 MCP 服务器以及 `manifest.json`，后者描述了 Claude Desktop 和其他支持桌面扩展的应用程序需要了解的所有信息。

```
extension.mcpb (ZIP archive)
├── manifest.json         # Extension metadata and configuration
                          # 扩展元数据和配置
├── server/               # MCP server implementation
                          # MCP 服务器实现
│   └── [server files]
                          # 服务器文件
├── dependencies/         # All required packages/libraries
                          # 所有必需的包/库
└── icon.png             # Optional: Extension icon
                          # 可选：扩展图标

# Example: Node.js Extension
# 示例：Node.js 扩展
extension.mcpb
├── manifest.json         # Required: Extension metadata and configuration
                          # 必需：扩展元数据和配置
├── server/               # Server files
                          # 服务器文件
│   └── index.js          # Main entry point
                          # 主入口点
├── node_modules/         # Bundled dependencies
                          # 打包的依赖项
├── package.json          # Optional: NPM package definition
                          # 可选：NPM 包定义
└── icon.png              # Optional: Extension icon
                          # 可选：扩展图标

# Example: Python Extension
# 示例：Python 扩展
extension.mcpb (ZIP file)
├── manifest.json         # Required: Extension metadata and configuration
                          # 必需：扩展元数据和配置
├── server/               # Server files
                          # 服务器文件
│   ├── main.py           # Main entry point
                          # 主入口点
│   └── utils.py          # Additional modules
                          # 其他模块
├── lib/                  # Bundled Python packages
                          # 打包的 Python 包
├── requirements.txt      # Optional: Python dependencies list
                          # 可选：Python 依赖项列表
└── icon.png              # Optional: Extension icon
                          # 可选：扩展图标
```

The only required file in a Desktop Extension is a manifest.json. Claude Desktop handles all the complexity:

Desktop Extension 中唯一必需的文件是 manifest.json。Claude Desktop 处理所有复杂性：

- Built-in runtime: We ship Node.js with Claude Desktop, eliminating external dependencies

- 内置运行时：我们随 Claude Desktop 一起提供 Node.js，消除了外部依赖

- Automatic updates: Extensions update automatically when new versions are available

- 自动更新：当有新版本可用时，扩展会自动更新

- Secure secrets: Sensitive configuration like API keys are stored in the OS keychain

- 安全密钥：敏感配置（如 API 密钥）存储在操作系统密钥链中

The manifest contains human-readable information (like the name, description, or author), a declaration of features (tools, prompts), user configuration, and runtime requirements. Most fields are optional, so the minimal version is quite short, although in practice, we expect all three supported extension types (Node.js, Python, and classic binaries/executables) to include files:

manifest 包含人类可读的信息（如名称、描述或作者）、功能声明（工具、提示词）、用户配置和运行时要求。大多数字段是可选的，因此最小版本相当简短，尽管在实践中，我们期望所有三种支持的扩展类型（Node.js、Python 和经典二进制文件/可执行文件）都包含文件：

```json
{
  "mcpb_version": "0.1",                    // MCPB spec version this manifest conforms to
                                            // 此 manifest 遵循的 MCPB 规范版本
  "name": "my-extension",                   // Machine-readable name (used for CLI, APIs)
                                            // 机器可读名称（用于 CLI、API）
  "version": "1.0.0",                       // Semantic version of your extension
                                            // 扩展的语义版本
  "description": "A simple MCP extension",  // Brief description of what the extension does
                                            // 扩展功能的简要描述
  "author": {                               // Author information (required)
                                            // 作者信息（必需）
    "name": "Extension Author"              // Author's name (required field)
                                            // 作者姓名（必需字段）
  },
  "server": {                               // Server configuration (required)
                                            // 服务器配置（必需）
    "type": "node",                         // Server type: "node", "python", or "binary"
                                            // 服务器类型："node"、"python" 或 "binary"
    "entry_point": "server/index.js",       // Path to the main server file
                                            // 主服务器文件的路径
    "mcp_config": {                         // MCP server configuration
                                            // MCP 服务器配置
      "command": "node",                    // Command to run the server
                                            // 运行服务器的命令
      "args": [                             // Arguments passed to the command
                                            // 传递给命令的参数
        "${__dirname}/server/index.js"      // ${__dirname} is replaced with the extension's directory
                                            // ${__dirname} 替换为扩展的目录
      ]
    }
  }
}
```

There are a number of convenience options available in the manifest spec that aim to make the installation and configuration of local MCP servers easier. The server configuration object can be defined in a way that makes room both for user-defined configuration in the form of template literals as well as platform-specific overrides. Extension developers can define, in detail, what kind of configuration they want to collect from users.

manifest 规范中提供了许多便捷选项，旨在使本地 MCP 服务器的安装和配置更容易。服务器配置对象可以以一种既支持用户定义配置（以模板字面量形式）又支持平台特定覆盖的方式来定义。扩展开发者可以详细定义他们想从用户那里收集什么样的配置。

Let's take a look at a concrete example of how the manifest aids with configuration. In the manifest below, the developer declares that the user needs to supply an `api_key`. Claude will not enable the extension until the user has supplied that value, keep it automatically in the operating system's secret vault, and transparently replace the `${user_config.api_key}` with the user-supplied value when launching the server. Similarly, `${__dirname}` will be replaced with the full path to the extension's unpacked directory.

让我们看一个具体的例子，说明 manifest 如何帮助配置。在下面的 manifest 中，开发者声明用户需要提供 `api_key`。Claude 在用户提供该值之前不会启用扩展，会自动将其保存在操作系统的密钥库中，并在启动服务器时透明地将 `${user_config.api_key}` 替换为用户提供的值。类似地，`${__dirname}` 将被替换为扩展解压目录的完整路径。

```json
{
  "mcpb_version": "0.1",
  "name": "my-extension",
  "version": "1.0.0",
  "description": "A simple MCP extension",
  "author": {
    "name": "Extension Author"
  },
  "server": {
    "type": "node",
    "entry_point": "server/index.js",
    "mcp_config": {
      "command": "node",
      "args": ["${__dirname}/server/index.js"],
      "env": {
        "API_KEY": "${user_config.api_key}"
      }
    }
  },
  "user_config": {
    "api_key": {
      "type": "string",
      "title": "API Key",
      "description": "Your API key for authentication",
      "sensitive": true,
      "required": true
    }
  }
}
```

A full `manifest.json` with most of the optional fields might look like this:

包含大多数可选字段的完整 `manifest.json` 可能如下所示：

```json
{
  "mcpb_version": "0.1",
  "name": "My MCP Extension",
  "display_name": "My Awesome MCP Extension",
  "version": "1.0.0",
  "description": "A brief description of what this extension does",
  "long_description": "A detailed description that can include multiple paragraphs explaining the extension's functionality, use cases, and features. It supports basic markdown.",
  "author": {
    "name": "Your Name",
    "email": "yourname@example.com",
    "url": "https://your-website.com"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/your-username/my-mcp-extension"
  },
  "homepage": "https://example.com/my-extension",
  "documentation": "https://docs.example.com/my-extension",
  "support": "https://github.com/your-username/my-mcp-extension/issues",
  "icon": "icon.png",
  "screenshots": [
    "assets/screenshots/screenshot1.png",
    "assets/screenshots/screenshot2.png"
  ],
  "server": {
    "type": "node",
    "entry_point": "server/index.js",
    "mcp_config": {
      "command": "node",
      "args": ["${__dirname}/server/index.js"],
      "env": {
        "ALLOWED_DIRECTORIES": "${user_config.allowed_directories}"
      }
    }
  },
  "tools": [
    {
      "name": "search_files",
      "description": "Search for files in a directory"
    }
  ],
  "prompts": [
    {
      "name": "poetry",
      "description": "Have the LLM write poetry",
      "arguments": ["topic"],
      "text": "Write a creative poem about the following topic: ${arguments.topic}"
    }
  ],
  "tools_generated": true,
  "keywords": ["api", "automation", "productivity"],
  "license": "MIT",
  "compatibility": {
    "claude_desktop": ">=1.0.0",
    "platforms": ["darwin", "win32", "linux"],
    "runtimes": {
      "node": ">=16.0.0"
    }
  },
  "user_config": {
    "allowed_directories": {
      "type": "directory",
      "title": "Allowed Directories",
      "description": "Directories the server can access",
      "multiple": true,
      "required": true,
      "default": ["${HOME}/Desktop"]
    },
    "api_key": {
      "type": "string",
      "title": "API Key",
      "description": "Your API key for authentication",
      "sensitive": true,
      "required": false
    },
    "max_file_size": {
      "type": "number",
      "title": "Maximum File Size (MB)",
      "description": "Maximum file size to process",
      "default": 10,
      "min": 1,
      "max": 100
    }
  }
}
```

To see an extension and manifest, please refer to the examples in the MCPB repository.

要查看扩展和 manifest 示例，请参考 MCPB 仓库中的示例。

The full specification for all required and optional fields in the `manifest.json` can be found as part of our open-source toolchain.

`manifest.json` 中所有必需和可选字段的完整规范可以在我们的开源工具链中找到。

## Building your first extension | 构建你的第一个扩展

Let's walk through packaging an existing MCP server as a Desktop Extension. We'll use a simple file system server as an example.

让我们逐步将现有的 MCP 服务器打包为 Desktop Extension。我们将使用一个简单的文件系统服务器作为示例。

### Step 1: Create the manifest | 步骤 1：创建 manifest

First, initialize a manifest for your server:

首先，为你的服务器初始化 manifest：

```
npx @anthropic-ai/mcpb init
```

This interactive tool asks about your server and generates a complete manifest.json. If you want to speed-run your way to the most basic manifest.json, you can run the command with a --yes parameter.

这个交互式工具会询问关于你服务器的问题并生成完整的 manifest.json。如果你想快速获得最基本的 manifest.json，可以使用 --yes 参数运行命令。

### Step 2: Handle user configuration | 步骤 2：处理用户配置

If your server needs user input (like API keys or allowed directories), declare it in the manifest:

如果你的服务器需要用户输入（如 API 密钥或允许的目录），在 manifest 中声明：

```json
"user_config": {
  "allowed_directories": {
    "type": "directory",
    "title": "Allowed Directories",
    "description": "Directories the server can access",
    "multiple": true,
    "required": true,
    "default": ["${HOME}/Documents"]
  }
}
```

Claude Desktop will:

Claude Desktop 将会：

- Display a user-friendly configuration UI

- 显示用户友好的配置界面

- Validate inputs before enabling the extension

- 在启用扩展之前验证输入

- Securely store sensitive values

- 安全地存储敏感值

- Pass configuration to your server either as arguments or environment variables, depending on developer configuration

- 根据开发者配置，将配置作为参数或环境变量传递给你的服务器

In the example below, we're passing the user configuration as an environment variable, but it could also be an argument.

在下面的示例中，我们将用户配置作为环境变量传递，但它也可以作为参数传递。

```json
"server": {
   "type": "node",
   "entry_point": "server/index.js",
   "mcp_config": {
   "command": "node",
   "args": ["${__dirname}/server/index.js"],
   "env": {
      "ALLOWED_DIRECTORIES": "${user_config.allowed_directories}"
   }
   }
}
```

### Step 3: Package the extension | 步骤 3：打包扩展

Bundle everything into a `.mcpb` file:

将所有内容打包到 `.mcpb` 文件中：

```
npx @anthropic-ai/mcpb pack
```

This command:

此命令：

1. Validates your manifest

验证你的 manifest

2. Generates the `.mcpb` archive

生成 `.mcpb` 归档文件

### Step 4: Test locally | 步骤 4：本地测试

Drag your `.mcpb` file into Claude Desktop's Settings window. You'll see:

将你的 `.mcpb` 文件拖到 Claude Desktop 的设置窗口中。你会看到：

- Human-readable information about your extension

- 关于你的扩展的人类可读信息

- Required permissions and configuration

- 所需的权限和配置

- A simple "Install" button

- 一个简单的"安装"按钮

## Advanced features | 高级功能

### Cross-platform support | 跨平台支持

Extensions can adapt to different operating systems:

扩展可以适应不同的操作系统：

```json
"server": {
  "type": "node",
  "entry_point": "server/index.js",
  "mcp_config": {
    "command": "node",
    "args": ["${__dirname}/server/index.js"],
    "platforms": {
      "win32": {
        "command": "node.exe",
        "env": {
          "TEMP_DIR": "${TEMP}"
        }
      },
      "darwin": {
        "env": {
          "TEMP_DIR": "${TMPDIR}"
        }
      }
    }
  }
}
```

### Dynamic configuration | 动态配置

Use template literals for runtime values:

使用模板字面量表示运行时值：

- `${__dirname}`: Extension's installation directory

- `${__dirname}`：扩展的安装目录

- `${user_config.key}`: User-provided configuration

- `${user_config.key}`：用户提供的配置

- `${HOME}, ${TEMP}`: System environment variables

- `${HOME}, ${TEMP}`：系统环境变量

### Feature declaration | 功能声明

Help users understand capabilities upfront:

帮助用户提前了解功能：

```json
"tools": [
  {
    "name": "read_file",
    "description": "Read contents of a file"
  }
],
"prompts": [
  {
    "name": "code_review",
    "description": "Review code for best practices",
    "arguments": ["file_path"]
  }
]
```

## The extension directory | 扩展目录

We're launching with a curated directory of extensions built into Claude Desktop. Users can browse, search, and install with one click—no searching GitHub or vetting code.

我们推出了内置在 Claude Desktop 中的精心策划的扩展目录。用户可以浏览、搜索并一键安装——无需搜索 GitHub 或审查代码。

While we expect both the Desktop Extension specification and the implementation in Claude for macOS and Windows to evolve over time, we look forward to seeing the many ways in which extensions can be used to expand the capabilities of Claude in creative ways.

虽然我们期望 Desktop Extension 规范和 Claude 在 macOS 和 Windows 中的实现都会随时间演进，但我们期待看到扩展以多种创造性方式扩展 Claude 的能力。

To submit your extension:

要提交你的扩展：

1. Ensure it follows the guidelines found in the submission form

确保它遵循提交表单中的指南

2. Test across Windows and macOS

在 Windows 和 macOS 上测试

3. Submit your extension

提交你的扩展

4. Our team reviews for quality and security

我们的团队审查质量和安全性

## Building an open ecosystem | 构建开放生态系统

We are committed to the open ecosystem around MCP servers and believe that its ability to be universally adopted by multiple applications and services has benefitted the community. In line with this commitment, we're open-sourcing the Desktop Extension specification, toolchain, and the schemas and key functions used by Claude for macOS and Windows to implement its own support of Desktop Extensions. It is our hope that the MCPB format doesn't just make local MCP servers more portable for Claude, but other AI desktop applications, too.

我们致力于围绕 MCP 服务器构建开放生态系统，并相信它被多个应用程序和服务普遍采用的能力已经惠及了社区。与这一承诺一致，我们正在开源 Desktop Extension 规范、工具链，以及 Claude 在 macOS 和 Windows 上实现自身 Desktop Extensions 支持所使用的模式和关键函数。我们希望 MCPB 格式不仅使本地 MCP 服务器对 Claude 更具可移植性，对其他 AI 桌面应用程序也是如此。

We're open-sourcing:

我们要开源：

- The complete MCPB specification

- 完整的 MCPB 规范

- Packaging and validation tools

- 打包和验证工具

- Reference implementation code

- 参考实现代码

- TypeScript types and schemas

- TypeScript 类型和模式

This means:

这意味着：

- For MCP server developers: Package once, run anywhere that supports MCPB

- 对于 MCP 服务器开发者：打包一次，在任何支持 MCPB 的地方运行

- For app developers: Add extension support without building from scratch

- 对于应用程序开发者：无需从头开始构建即可添加扩展支持

- For users: Consistent experience across all MCP-enabled applications

- 对于用户：在所有支持 MCP 的应用程序中获得一致的体验

The specification and toolchain is on purpose versioned as 0.1, as we are looking forward to working with the greater community on evolving and changing the format. We look forward to hearing from you.

规范和工具链故意版本定为 0.1，因为我们期待与更广泛的社区合作来演进和改变这种格式。我们期待听到你的声音。

## Security and enterprise considerations | 安全和企业考虑

We understand that extensions introduce new security considerations, particularly for enterprises. We've built in several safeguards with the preview release of Desktop Extensions:

我们理解扩展带来了新的安全考虑，特别是对于企业。我们在 Desktop Extensions 的预览版本中内置了多项保障措施：

### For users | 对于用户

- Sensitive data stays in the OS keychain

- 敏感数据保留在操作系统密钥链中

- Automatic updates

- 自动更新

- Ability to audit what extensions are installed

- 能够审计安装了哪些扩展

### For enterprises | 对于企业

- Group Policy (Windows) and MDM (macOS) support

- 组策略（Windows）和 MDM（macOS）支持

- Ability to pre-install approved extensions

- 能够预安装批准的扩展

- Blocklist specific extensions or publishers

- 阻止特定扩展或发布者

- Disable the extension directory entirely

- 完全禁用扩展目录

- Deploy private extension directories

- 部署私有扩展目录

For more information about how to manage extensions within your organization, see our documentation.

有关如何在组织内管理扩展的更多信息，请参阅我们的文档。

## Getting started | 入门指南

Ready to build your own extension? Here's how to start:

准备构建你自己的扩展了吗？以下是开始的方法：

**For MCP server developers:** Review our [developer documentation](https://docs.anthropic.com/) – or dive right in by running the following commands in your local MCP servers' directory:

**对于 MCP 服务器开发者**：查看我们的[开发者文档](https://docs.anthropic.com/)——或者直接在你的本地 MCP 服务器目录中运行以下命令：

```
npm install -g @anthropic-ai/mcpb
mcpb init
mcpb pack
```

**For Claude Desktop users:** Update to the latest version and look for the Extensions section in Settings

**对于 Claude Desktop 用户**：更新到最新版本并在设置中查找扩展部分

**For enterprises:** Review our enterprise documentation for deployment options

**对于企业**：查看我们的企业文档以了解部署选项

## Building with Claude Code | 使用 Claude Code 构建

Internally at Anthropic, we have found that Claude is great at building extensions with minimal intervention. If you too want to use Claude Code, we recommend that you briefly explain what you want your extension to do and then add the following context to the prompt:

在 Anthropic 内部，我们发现 Claude 非常擅长以最少的干预构建扩展。如果你想使用 Claude Code，我们建议你简要解释你想要扩展做什么，然后在提示词中添加以下上下文：

```
I want to build this as a Desktop Extension, abbreviated as "MCPB". Please follow these steps:

我想将其构建为 Desktop Extension，缩写为"MCPB"。请遵循以下步骤：

1. **Read the specifications thoroughly:**
   **1. 彻底阅读规范：**
   - https://github.com/anthropics/mcpb/blob/main/README.md - MCPB architecture overview, capabilities, and integration patterns
     - https://github.com/anthropics/mcpb/blob/main/README.md - MCPB 架构概览、功能和集成模式
   - https://github.com/anthropics/mcpb/blob/main/MANIFEST.md - Complete extension manifest structure and field definitions
     - https://github.com/anthropics/mcpb/blob/main/MANIFEST.md - 完整的扩展 manifest 结构和字段定义
   - https://github.com/anthropics/mcpb/tree/main/examples - Reference implementations including a "Hello World" example
     - https://github.com/anthropics/mcpb/tree/main/examples - 参考实现，包括"Hello World"示例

2. **Create a proper extension structure:**
   **2. 创建正确的扩展结构：**
   - Generate a valid manifest.json following the MANIFEST.md spec
     - 遵循 MANIFEST.md 规范生成有效的 manifest.json
   - Implement an MCP server using @modelcontextprotocol/sdk with proper tool definitions
     - 使用 @modelcontextprotocol/sdk 实现 MCP 服务器，具有正确的工具定义
   - Include proper error handling and timeout management
     - 包含适当的错误处理和超时管理

3. **Follow best development practices:**
   **3. 遵循最佳开发实践：**
   - Implement proper MCP protocol communication via stdio transport
     - 通过 stdio 传输实现正确的 MCP 协议通信
   - Structure tools with clear schemas, validation, and consistent JSON responses
     - 构建具有清晰模式、验证和一致 JSON 响应的工具
   - Make use of the fact that this extension will be running locally
     - 利用此扩展将在本地运行这一事实
   - Add appropriate logging and debugging capabilities
     - 添加适当的日志记录和调试功能
   - Include proper documentation and setup instructions
     - 包含适当的文档和设置说明

4. **Test considerations:**
   **4. 测试考虑：**
   - Validate that all tool calls return properly structured responses
     - 验证所有工具调用返回正确结构的响应
   - Verify manifest loads correctly and host integration works
     - 验证 manifest 正确加载且主机集成有效

Generate complete, production-ready code that can be immediately tested. Focus on defensive programming, clear error messages, and following the exact MCPB specifications to ensure compatibility with the ecosystem.

生成完整的、可立即测试的生产就绪代码。专注于防御性编程、清晰的错误消息，并遵循确切的 MCPB 规范以确保与生态系统的兼容性。
```

## Conclusion | 结论

Desktop Extensions represent a fundamental shift in how users interact with local AI tools. By removing installation friction, we're making powerful MCP servers accessible to everyone—not just developers.

Desktop Extensions 代表了用户与本地 AI 工具交互方式的根本性转变。通过消除安装摩擦，我们使强大的 MCP 服务器对每个人都可访问——而不仅仅是开发者。

Internally, we're using desktop extensions to share highly experimental MCP servers - some fun, some useful.. One team experimented to see how far our models could make it when directly connected to a GameBoy, similar to our "Claude plays Pokémon" research. We used Desktop Extensions to package a single extension that opens up the popular PyBoy GameBoy emulator and lets Claude take control. We believe that countless opportunities exist to connect the model's capabilities to the tools, data, and applications users already have on their local machines.

在内部，我们正在使用桌面扩展来分享高度实验性的 MCP 服务器——有些有趣，有些实用。一个团队尝试看看当模型直接连接到 GameBoy 时能走多远，类似于我们的"Claude plays Pokémon"研究。我们使用 Desktop Extensions 打包了一个扩展，打开流行的 PyBoy GameBoy 模拟器并让 Claude 接管控制。我们相信，存在无数机会将模型的能力与用户本地机器上已有的工具、数据和应用程序连接起来。

![A desktop showing the PyBoy MCP with Super Mario Land start screen](https://www-cdn.anthropic.com/images/4zrzovbb/website/d48f3ea1218a4b90450b9ab8134fa0e24db5a167-720x542.png)

一个显示 PyBoy MCP 和 Super Mario Land 启动屏幕的桌面

We can't wait to see what you build. The same creativity that brought us thousands of MCP servers can now reach millions of users with just one click. Ready to share your MCP server? Submit your extension for review.

我们迫不及待地想看到你构建什么。带给我们数千个 MCP 服务器的同样创造力现在可以一键触达数百万用户。准备分享你的 MCP 服务器了吗？提交你的扩展以供审查。

---

**Sources:**
- [One-click MCP server installation for Claude Desktop](https://www.anthropic.com/engineering/desktop-extensions)
- [Claude plays Pokémon research](https://www.anthropic.com/engineering/)
- [MCPB GitHub Repository](https://github.com/anthropics/mcpb)
- [Anthropic Developer Documentation](https://docs.anthropic.com/)
