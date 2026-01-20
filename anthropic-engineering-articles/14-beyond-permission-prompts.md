# Beyond Permission Prompts: The Architecture of Safe Tool Use
# 超越权限提示词：安全工具使用的架构

**Published:** Nov 6, 2024
**发布日期：** 2024年11月6日

**Author:** William Shannon
**作者：** William Shannon

---

In Claude Code, Claude writes, tests, and debugs code alongside you, navigating your codebase, editing multiple files, and running commands to verify its work. Giving Claude this much access to your codebase and files can introduce risks, especially in the case of prompt injection, such as Claude deleting files you didn't intend.
在 Claude Code 中，Claude 与你一起编写、测试和调试代码，导航你的代码库，编辑多个文件，并运行命令来验证其工作。给 Claude 这么多的代码库和文件访问权限可能会带来风险，特别是在提示词注入的情况下，例如 Claude 删除你不打算删除的文件。

To help address this, we've introduced two new features in Claude Code built on top of sandboxing, both of which are designed to provide a more secure place for developers to work, while also allowing Claude to run more autonomously and with fewer permission prompts.
为了帮助解决这个问题，我们在 Claude Code 中引入了两个基于沙盒的新功能，这两个功能旨在为开发者提供更安全的工作场所，同时也允许 Claude 更自主地运行并减少权限提示。

ByThese features are examples of __native sandboxing__: defining set boundaries within which Claude can work freely, they increase security and agency.
这些功能是__原生沙盒__的示例：定义 Claude 可以自由工作的既定边界，它们提高了安全性和代理能力。

## Our current approach to keeping users secure
## 我们当前保持用户安全的方法

Claude Code runs on a permission-based model: by default, it's read-only, which means it asks for permission before making modifications or running any commands. There are some exceptions to this: we use static analysis to auto-allow safe commands like echo or cat, but most operations still need explicit approval.
Claude Code 运行在基于权限的模型上：默认情况下，它是只读的，这意味着它在进行修改或运行任何命令之前都会请求权限。对此有一些例外：我们使用静态分析自动允许安全的命令，如 echo 或 cat，但大多数操作仍然需要明确批准。

But constantly clicking "approve" slows down development and can lead to 'approval fatigue', where users might not pay close attention to what they're approving. To make Claude Code both safer and more effective, we wanted to find a better method.
但不断点击"批准"会减慢开发速度，并可能导致"批准疲劳"，用户可能不会密切关注他们正在批准的内容。为了使 Claude Code 既更安全又更有效，我们希望找到更好的方法。

## Sandboxing: a safer and more autonomous approach
## 沙盒：更安全、更自主的方法

Sandboxing creates pre-defined boundaries within which Claude can work more freely, instead of asking for permission for each action.
沙盒创建了预定义的边界，Claude 可以在其中更自由地工作，而不是为每个操作请求权限。

With our update to Claude Code, we're shifting to this approach. We're building Our approach to sandboxing is built on top of operating system-level features to enable two new features, each of which are based on the followingtwo sets of boundariesmain things:
随着我们对 Claude Code 的更新，我们正在转向这种方法。我们构建的沙盒方法基于操作系统级别的功能，以启用两个新功能，每个功能都基于以下两件事：

1. __Filesystem isolation__, which ensures that Claude can only access or modify specific directories. This is particularly important in preventing a prompt-injected Claude from modifying sensitive system files.
1. __文件系统隔离__，确保 Claude 只能访问或修改特定目录。这对于防止提示词注入的 Claude 修改敏感系统文件特别重要。
2. __Network isolation__, which ensures that Claude can only connect to approved servers. This prevents a prompt-injected Claude from leaking sensitive information or downloading malware.
2. __网络隔离__，确保 Claude 只能连接到批准的服务器。这可以防止提示词注入的 Claude 泄露敏感信息或下载恶意软件。

It is worth noting that effective sandboxing requires _both_ filesystem and network isolation. Without network isolation, a compromised agent could exfiltrate sensitive files like SSH keys; without filesystem isolation, a compromised agent could easily escape the sandbox and gain network access. It's by using both techniques that we can provide a safer agentic experience for Claude Code users.
值得注意的是，有效的沙盒需要_同时_进行文件系统和网络隔离。没有网络隔离，受损的代理可能会泄露敏感文件（如 SSH 密钥）；没有文件系统隔离，受损的代理可以轻松逃脱沙盒并获得网络访问权限。正是通过同时使用这两种技术，我们才能为 Claude Code 用户提供更安全的代理体验。

### Two new sandboxing features in Claude Code
### Claude Code 中的两个新沙盒功能

#### Sandboxed bash tool: safe bash execution without permission prompts
#### 沙盒化的 bash 工具：无需权限提示词的安全 bash 执行

Today, wWe're introducing a new sandbox runtime, available in research preview, that lets you define exactly which directories and network hosts your agent can access, without the overhead of spinning up and managing a container. This can be used to sandbox arbitrary processes, agents and MCP servers. It is now available as an open source research preview here:  [Github link?]
今天，我们正在推出一个新的沙盒运行时，可用于研究预览，它让你可以精确地定义你的代理可以访问哪些目录和网络主机，而无需启动和管理容器的开销。这可用于沙盒化任意进程、代理和 MCP 服务器。它现在作为开源研究预览版提供：[Github 链接？]

In Claude Code, we use this runtime to sandbox the bash tool, which allows Claude to run commands within the defined limits you set. These commands are safer by default, they require fewer user permission prompts, so Claude can run more autonomously. If Claude tries to access something _outside_ of the sandbox, you'll be notified immediately, and can choose whether or not to allow it.
在 Claude Code 中，我们使用这个运行时来沙盒化 bash 工具，它允许 Claude 在你定义的限制范围内运行命令。这些命令默认更安全，它们需要更少的用户权限提示词，因此 Claude 可以更自主地运行。如果 Claude 尝试访问沙盒_之外_的内容，你会立即收到通知，并可以选择是否允许它。

We've built this on top of OS level primitives such as [Linux bubblewrap](https://github.com/containers/bubblewrap) and MacOS seatbelt to enforce these restrictions at the OS level. They cover not just Claude Code's direct interactions, but also any scripts, programs, or subprocesses that are spawned by the command.
我们基于操作系统级别的原语（如 [Linux bubblewrap](https://github.com/containers/bubblewrap) 和 MacOS seatbelt）构建了这个功能，以便在操作系统级别强制执行这些限制。它们不仅覆盖 Claude Code 的直接交互，还覆盖命令生成的任何脚本、程序或子进程。

As described above, this sandbox enforces both:
如上所述，这个沙盒强制执行：

1. __Filesystem isolation,__ by allowing read and write access to the current working directory, but blocking the modification of any files outside of it.
1. __文件系统隔离__，通过允许对当前工作目录的读写访问，但阻止修改其之外的任何文件。
2. __Network isolation,__ by only allowing internet access through a unix domain socket connected to a proxy server running outside the sandbox. This proxy server enforces restrictions on the domains that a process can connect to, and handles user confirmation for newly requested domains. IAnd if you'd like further-increased security, we alsoeven support customizing this proxy to enforce arbitrary rules on outgoing traffic.
2. __网络隔离__，通过仅允许通过连接到沙盒外运行的代理服务器的 unix 域套接字进行互联网访问。此代理服务器强制执行进程可以连接的域的限制，并处理新请求域的用户确认。如果你希望进一步提高安全性，我们甚至支持自定义此代理以对传出流量强制执行任意规则。

‍

Both components are configurable: you can easily choose to allow or disallow specific file paths or domains.
两个组件都是可配置的：你可以轻松选择允许或禁止特定文件路径或域。

Sandboxing ensures that even a successful prompt injection is fully isolated, and cannot impact overall user security. This way, a compromised Claude Code can't steal your SSH keys, or phone home to an attacker's server.
沙盒确保即使成功的提示词注入也完全隔离，并且不会影响整体用户安全性。这样，受损的 Claude Code 无法窃取你的 SSH 密钥或拨通攻击者的服务器。

To get started with this feature, run: `claude --sandbox`, and read more technical details about our security model here.
要开始使用此功能，请运行：`claude --sandbox`，并在此处阅读有关我们安全模型的更多技术细节。

To make it easier for other teams to build safer agents, we have open sourced [XXX]. We believe that other AI companies should consider adopting this technology for their own agents in order to enhance the security posture of their agents.
为了使其他团队更容易构建更安全的代理，我们开源了 [XXX]。我们相信其他 AI 公司应该考虑为其自己的代理采用这项技术，以提高其代理的安全态势。

#### Claude Code on the web: running Claude Code securely in the cloud
#### 网页版 Claude Code：在云端安全地运行 Claude Code

Today, we're also releasing [Claude Code on the web](TODO: Link to docs on CCR), enabling users to run Claude Code in an isolated sandbox in the cloud. Claude Code on the web executes each Claude Code session in an isolated sandbox where it has full access to its server in a safe and secure way. We've designed this sandbox to ensure that sensitive credentials (such as git credentials or signing keys) are never inside the sandbox with Claude Codenever enter the sandbox environment. This way, even if the code running in the sandbox is compromised, the user is kept safe from further harm.
今天，我们还发布了[网页版 Claude Code](TODO: 链接到 CCR 上的文档)，使用户能够在云端的隔离沙盒中运行 Claude Code。网页版 Claude Code 在隔离的沙盒中执行每个 Claude Code 会话，在其中它以安全的方式完全访问其服务器。我们设计了这个沙盒，以确保敏感凭据（如 git 凭据或签名密钥）永远不会进入沙盒环境。这样，即使沙盒中运行的代码受到损害，用户也能免受进一步伤害。

Claude Code on the web uses a custom proxy service that transparently handles all git interactions. Inside the sandbox, the git client authenticates to this service with a custom-built scoped credential. The proxy verifies this credential and the contents of the git interaction (e.g. ensuring it is only pushing to the configured branch), then attaches the right authentication token before sending the request to GitHub.
网页版 Claude Code 使用自定义代理服务来透明地处理所有 git 交互。在沙盒内，git 客户端使用自定义的作用域凭据向此服务进行身份验证。代理验证此凭据和 git 交互的内容（例如，确保它只是推送到配置的分支），然后在将请求发送到 GitHub 之前附加正确的身份验证令牌。

## Getting started
## 开始使用

Our new sandboxed bash tool and Claude Code on the web offer substantial improvements in both security and productivity for developers using Claude for their engineering work.
我们新的沙盒化 bash 工具和网页版 Claude Code 为使用 Claude 进行工程工作的开发者在安全性和生产力方面提供了显著改进。

To get started with these tools:
要开始使用这些工具：

1. Run `claude --sandbox` and check out [our docs](TODO) on how to configure this sandbox.
1. 运行 `claude --sandbox` 并查看[我们的文档](TODO)以了解如何配置此沙盒。
2. Go to claude.com/code to try out Claude Code on the web.
2. 访问 claude.com/code 尝试网页版 Claude Code。

‍

Or, if you're building your own agents, check out our open-sourced sandboxing code, and consider integrating it into your work. We look forward to seeing what you build.
或者，如果你正在构建自己的代理，请查看我们的开源沙盒代码，并考虑将其集成到你的工作中。我们期待看到你构建的东西。
