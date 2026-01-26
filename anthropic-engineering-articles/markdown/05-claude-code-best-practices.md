# Claude Code: Best practices for agentic coding | Claude Code：智能体编码的最佳实践

We recently released Claude Code, a command line tool for agentic coding. Developed as a research project, Claude Code gives Anthropic engineers and researchers a more native way to integrate Claude into their coding workflows.

我们最近发布了 Claude Code，这是一个用于智能体编码的命令行工具。作为研究项目开发的，Claude Code 为 Anthropic 的工程师和研究人员提供了一种更原生的方式，将 Claude 集成到他们的编码工作流程中。

Claude Code is intentionally low-level and unopinionated, providing close to raw model access without forcing specific workflows. This design philosophy creates a flexible, customizable, scriptable, and safe power tool. While powerful, this flexibility presents a learning curve for engineers new to agentic coding tools—at least until they develop their own best practices.

Claude Code 故意保持底层和无偏见，提供接近原始模型的访问，而不强制特定的工作流程。这种设计理念创造了一个灵活、可定制、可脚本化且安全的强大工具。虽然强大，但这种灵活性给新接触智能体编码工具的工程师带来了学习曲线——至少在他们开发出自己的最佳实践之前是这样。

This post outlines general patterns that have proven effective, both for Anthropic's internal teams and for external engineers using Claude Code across various codebases, languages, and environments. Nothing in this list is set in stone nor universally applicable; consider these suggestions as starting points. We encourage you to experiment and find what works best for you!

本文概述了已被证明有效的通用模式，无论是对于 Anthropic 的内部团队还是在外部工程师在各种代码库、语言和环境中使用 Claude Code。这份清单中的任何内容都不是一成不变的，也不是普遍适用的；将这些建议视为起点。我们鼓励您进行实验，找到最适合您的方法！

_Looking for more detailed information? Our comprehensive [documentation](https://claude.ai/code) covers all the features mentioned in this post and provides additional examples, implementation details, and advanced techniques._

_寻找更详细的信息？我们在[综合文档](https://claude.ai/code)中涵盖了本文提到的所有功能，并提供额外的示例、实现细节和高级技术。_

---

## 1. Customize your setup | 1. 自定义您的设置

Claude Code is an agentic coding assistant that automatically pulls context into prompts. This context gathering consumes time and tokens, but you can optimize it through environment tuning.

Claude Code 是一个智能体编码助手，会自动将上下文拉取到提示中。这种上下文收集会消耗时间和 token，但您可以通过环境调优来优化它。

### a. Create `CLAUDE.md` files | a. 创建 `CLAUDE.md` 文件

`CLAUDE.md` is a special file that Claude automatically pulls into context when starting a conversation. This makes it an ideal place for documenting:

`CLAUDE.md` 是一个特殊文件，Claude 在开始对话时会自动将其拉取到上下文中。这使其成为记录以下内容的理想场所：

- Common bash commands
- 常用 bash 命令

- Core files and utility functions
- 核心文件和实用函数

- Code style guidelines
- 代码风格指南

- Testing instructions
- 测试说明

- Repository etiquette (e.g., branch naming, merge vs. rebase, etc.)
- 仓库礼仪（例如，分支命名、合并 vs rebase 等）

- Developer environment setup (e.g., pyenv use, which compilers work)
- 开发者环境设置（例如 pyenv use、哪些编译器可用）

- Any unexpected behaviors or warnings particular to the project
- 项目特有的任何意外行为或警告

- Other information you want Claude to remember
- 您希望 Claude 记住的其他信息

There's no required format for `CLAUDE.md` files. We recommend keeping them concise and human-readable. For example:

`CLAUDE.md` 文件没有必需的格式。我们建议保持简洁和人类可读。例如：

```markdown
# Bash commands
- npm run build: Build the project
- npm run typecheck: Run the typechecker

# Code style
- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible (eg. import { foo } from 'bar')

# Workflow
- Be sure to typecheck when you're done making a series of code changes
- Prefer running single tests, and not the whole test suite, for performance
```

You can place `CLAUDE.md` files in several locations:

您可以在几个位置放置 `CLAUDE.md` 文件：

- __The root of your repo__, or wherever you run `claude` from (the most common usage). Name it `CLAUDE.md` and check it into git so that you can share it across sessions and with your team (recommended), or name it `CLAUDE.local.md` and `.gitignore` it

- __您仓库的根目录__，或您运行 `claude` 的任何位置（最常见）。将其命名为 `CLAUDE.md` 并检入 git，以便您可以在会话之间和与团队共享（推荐），或将其命名为 `CLAUDE.local.md` 并添加到 `.gitignore`

- __Any parent of the directory__ where you run `claude`. This is most useful for monorepos, where you might run `claude` from `root/foo`, and have `CLAUDE.md` files in both `root/CLAUDE.md` and `root/foo/CLAUDE.md`. Both of these will be pulled into context automatically

- __您运行 `claude` 的目录的任何父目录__。这对于 monorepos 最有用，您可能从 `root/foo` 运行 `claude`，并且在 `root/CLAUDE.md` 和 `root/foo/CLAUDE.md` 中都有 `CLAUDE.md` 文件。这两个文件都将自动拉取到上下文中

- __Any child of the directory__ where you run `claude`. This is the inverse of the above, and in this case, Claude will pull in `CLAUDE.md` files on demand when you work with files in child directories

- __您运行 `claude` 的目录的任何子目录__。这与上述相反，在这种情况下，当您在子目录中处理文件时，Claude 将按需拉取 `CLAUDE.md` 文件

- __Your home folder__ (`~/.claude/CLAUDE.md`), which applies it to all your _claude_ sessions

- __您的主文件夹__（`~/.claude/CLAUDE.md`），它适用于您所有的 _claude_ 会话

When you run the `/init` command, Claude will automatically generate a `CLAUDE.md` for you.

当您运行 `/init` 命令时，Claude 将自动为您生成一个 `CLAUDE.md`。

### b. Tune your `CLAUDE.md` files | b. 调整您的 `CLAUDE.md` 文件

Your `CLAUDE.md` files become part of Claude's prompts, so they should be refined like any frequently used prompt. A common mistake is adding extensive content without iterating on its effectiveness. Take time to experiment and determine what produces the best instruction following from the model.

您的 `CLAUDE.md` 文件成为 Claude 提示的一部分，因此应该像任何频繁使用的提示一样进行改进。一个常见的错误是添加大量内容而不迭代其有效性。花时间进行实验，确定什么能产生模型的最佳指令遵循。

You can add content to your `CLAUDE.md` manually or press the `#` key to give Claude an instruction that it will automatically incorporate into the relevant `CLAUDE.md`. Many engineers use `#` frequently to document commands, files, and style guidelines while coding, then include `CLAUDE.md` changes in commits so team members benefit as well.

您可以手动向 `CLAUDE.md` 添加内容，或按 `#` 键给 Claude 一个指令，它会自动将其合并到相关的 `CLAUDE.md` 中。许多工程师在编码时频繁使用 `#` 来记录命令、文件和风格指南，然后将 `CLAUDE.md` 更改包含在提交中，以便团队成员也能受益。

At Anthropic, we occasionally run `CLAUDE.md` files through the prompt improver and often tune instructions (e.g. adding emphasis with "IMPORTANT" or "YOU MUST") to improve adherence.

在 Anthropic，我们偶尔会通过提示改进器运行 `CLAUDE.md` 文件，并经常调整指令（例如，添加"IMPORTANT"或"YOU MUST"等强调）以提高遵循度。

![Claude Code tool allowlist | Claude Code 工具允许列表](https://www-cdn.anthropic.com/images/4zrzovbb/website/6961243cc6409e41ba93895faded4f4bc1772366-1600x1231.png)

Claude Code 工具允许列表界面显示了可自定义的工具权限设置。

### c. Curate Claude's list of allowed tools | c. 策展 Claude 的允许工具列表

By default, Claude Code requests permission for any action that might modify your system: file writes, many bash commands, MCP tools, etc. We designed Claude Code with this deliberately conservative approach to prioritize safety. You can customize the allowlist to permit additional tools that you know are safe, or to allow potentially unsafe tools that are easy to undo (e.g., file editing, `git commit`).

默认情况下，Claude Code 对任何可能修改系统的操作请求权限：文件写入、许多 bash 命令、MCP 工具等。我们以这种刻意保守的方法设计 Claude Code，以优先考虑安全性。您可以自定义允许列表以允许您知道安全的其他工具，或允许容易撤销的潜在不安全工具（例如，文件编辑、`git commit`）。

There are four ways to manage allowed tools:

有四种方法可以管理允许的工具：

- __Select "Always allow"__ when prompted during a session.

- __在会话期间提示时选择"始终允许"__。

- __Use the `/permissions` command__ after starting Claude Code to add or remove tools from the allowlist. For example, you can add `Edit` to always allow file edits, `Bash(git commit:*)` to allow git commits, or `mcp__puppeteer__puppeteer_navigate` to allow navigating with the Puppeteer MCP server.

- __在启动 Claude Code 后使用 `/permissions` 命令__从允许列表中添加或删除工具。例如，您可以添加 `Edit` 以始终允许文件编辑，添加 `Bash(git commit:*)` 以允许 git 提交，或添加 `mcp__puppeteer__puppeteer_navigate` 以允许使用 Puppeteer MCP 服务器进行导航。

- __Manually edit__ your `.claude/settings.json` or `~/.claude.json` (we recommend checking the former into source control to share with your team).

- __手动编辑__您的 `.claude/settings.json` 或 `~/.claude.json`（我们建议将前者检入源代码控制以与您的团队共享）。

- __Use the `--allowedTools` CLI flag__ for session-specific permissions.

- __使用 `--allowedTools` CLI 标志__进行特定于会话的权限设置。

### d. If using GitHub, install the gh CLI | d. 如果使用 GitHub，请安装 gh CLI

Claude knows how to use the `gh` CLI to interact with GitHub for creating issues, opening pull requests, reading comments, and more. Without `gh` installed, Claude can still use the GitHub API or MCP server (if you have it installed).

Claude 知道如何使用 `gh` CLI 与 GitHub 交互以创建问题、打开拉取请求、阅读评论等。如果没有安装 `gh`，Claude 仍然可以使用 GitHub API 或 MCP 服务器（如果您已安装）。

---

## 2. Give Claude more tools | 2. 给 Claude 更多工具

Claude has access to your shell environment, where you can build up sets of convenience scripts and functions for it just like you would for yourself. It can also leverage more complex tools through MCP and REST APIs.

Claude 可以访问您的 shell 环境，您可以在其中为它构建一组便利脚本和函数，就像您为自己做的那样。它还可以通过 MCP 和 REST API 利用更复杂的工具。

### a. Use Claude with bash tools | a. 将 Claude 与 bash 工具一起使用

Claude Code inherits your bash environment, giving it access to all your tools. While Claude knows common utilities like unix tools and `gh`, it won't know about your custom bash tools without instructions:

Claude Code 继承您的 bash 环境，使其能够访问您的所有工具。虽然 Claude 知道常见的实用程序，如 unix 工具和 `gh`，但在没有指令的情况下，它不会知道您的自定义 bash 工具：

1. Tell Claude the tool name with usage examples
告诉 Claude 工具名称并提供用法示例。

2. Tell Claude to run `--help` to see tool documentation
告诉 Claude 运行 `--help` 查看工具文档。

3. Document frequently used tools in `CLAUDE.md`
在 `CLAUDE.md` 中记录常用工具。

### b. Use Claude with MCP | b. 将 Claude 与 MCP 一起使用

Claude Code functions as both an MCP server and client. As a client, it can connect to any number of MCP servers to access their tools in three ways:

Claude Code 既作为 MCP 服务器又作为 MCP 客户端运行。作为客户端，它可以连接到任意数量的 MCP 服务器以通过三种方式访问它们的工具：

- __In project config__ (available when running Claude Code in that directory)
- __在项目配置中__（在该目录运行 Claude Code 时可用）

- __In global config__ (available in all projects)
- __在全局配置中__（在所有项目中可用）

- __In a checked-in `.mcp.json` file__ (available to anyone working in your codebase). For example, you can add Puppeteer and Sentry servers to your `.mcp.json`, so that every engineer working on your repo can use these out of the box.
- __在检入的 `.mcp.json` 文件中__（对代码库中工作的任何人可用）。例如，您可以在 `.mcp.json` 中添加 Puppeteer 和 Sentry 服务器，以便在仓库中工作的每位工程师都可以开箱即用。

When working with MCP, it can also be helpful to launch Claude with the `--mcp-debug` flag to help identify configuration issues.

在使用 MCP 时，使用 `--mcp-debug` 标志启动 Claude 也有助于识别配置问题。

### c. Use custom slash commands | c. 使用自定义斜杠命令

For repeated workflows—debugging loops, log analysis, etc.—store prompt templates in Markdown files within the `.claude/commands` folder. These become available through the slash commands menu when you type `/`. You can check these commands into git to make them available for the rest of your team.

对于重复的工作流程——调试循环、日志分析等——将提示模板存储在 `.claude/commands` 文件夹内的 Markdown 文件中。当您输入 `/` 时，这些模板可通过斜杠命令菜单获得。您可以将这些命令检入 git，以使其对团队的其余成员可用。

Custom slash commands can include the special keyword `$ARGUMENTS` to pass parameters from command invocation.

自定义斜杠命令可以包含特殊关键字 `$ARGUMENTS` 以从命令调用传递参数。

For example, here's a slash command that you could use to automatically pull and fix a Github issue:

例如，这是一个您可以使用来自动拉取和修复 GitHub 问题的斜杠命令：

```markdown
Please analyze and fix the GitHub issue: $ARGUMENTS.

请分析和修复 GitHub 问题：$ARGUMENTS。

Follow these steps:

请遵循以下步骤：

1. Use `gh issue view` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
4. Implement the necessary changes to fix the issue
5. Write and run tests to verify the fix
6. Ensure code passes linting and type checking
7. Create a descriptive commit message
8. Push and create a PR

Remember to use the GitHub CLI (`gh`) for all GitHub-related tasks.
```

Putting the above content into `.claude/commands/fix-github-issue.md` makes it available as the `/project:fix-github-issue` command in Claude Code. You could then for example use `/project:fix-github-issue 1234` to have Claude fix issue #1234. Similarly, you can add your own personal commands to the `~/.claude/commands` folder for commands you want available in all of your sessions.

将上述内容放入 `.claude/commands/fix-github-issue.md` 中，使其在 Claude Code 中作为 `/project:fix-github-issue` 命令可用。例如，您可以使用 `/project:fix-github-issue 1234` 让 Claude 修复问题 #1234。同样，您可以将自己的个人命令添加到 `~/.claude/commands` 文件夹中，以便在所有会话中使用这些命令。

---

## 3. Try common workflows | 3. 尝试常见的工作流程

Claude Code doesn't impose a specific workflow, giving you the flexibility to use it how you want. Within the space this flexibility affords, several successful patterns for effectively using Claude Code have emerged across our community of users:

Claude Code 不强制特定的工作流程，给您提供灵活使用它的自由。在这种灵活性赋予的空间内，我们的用户社区中出现了几种有效使用 Claude Code 的成功模式：

### a. Explore, plan, code, commit | a. 探索、计划、编码、提交

This versatile workflow suits many problems:

这种通用的工作流程适合许多问题：

1. __Ask Claude to read relevant files, images, or URLs__, providing either general pointers ("read the file that handles logging") or specific filenames ("read logging.py"), but explicitly tell it not to write any code just yet.

让 Claude 阅读相关文件、图片或 URL：可以给出泛化指引（例如“读取处理日志的文件”）或具体文件名（例如“读取 logging.py”），但要明确告诉它现在先不要写任何代码。

   1. This is the part of the workflow where you should consider strong use of subagents, especially for complex problems. Telling Claude to use subagents to verify details or investigate particular questions it might have, especially early on in a conversation or task, tends to preserve context availability without much downside in terms of lost efficiency.

   这是您应该考虑大量使用子智能体的工作流程部分，尤其是对于复杂问题。告诉 Claude 使用子智能体来验证细节或调查它可能有的特定问题，尤其是在对话或任务的早期，往往能够在不损失太多效率的情况下保持上下文的可用性。

2. __Ask Claude to make a plan for how to approach a specific problem__. We recommend using the word "think" to trigger extended thinking mode, which gives Claude additional computation time to evaluate alternatives more thoroughly. These specific phrases are mapped directly to increasing levels of thinking budget in the system: "think" < "think hard" < "think harder" < "ultrathink." Each level allocates progressively more thinking budget for Claude to use.

让 Claude 制定解决某个具体问题的计划。我们建议使用“think”等词触发扩展思考模式，从而给 Claude 更多计算时间以更充分地评估替代方案。这些短语会映射到系统中逐级增加的思考预算：“think” < “think hard” < “think harder” < “ultrathink”。每个级别都会为 Claude 分配更多思考预算。

   1. If the results of this step seem reasonable, you can have Claude create a document or a GitHub issue with its plan so that you can reset to this spot if the implementation (step 3) isn't what you want.

   如果这一步的结果看起来合理，您可以让 Claude 创建一个文档或 GitHub 问题及其计划，以便如果实现（第 3 步）不是您想要的，您可以重置到此位置。

3. __Ask Claude to implement its solution in code__. This is also a good place to ask it to explicitly verify the reasonableness of its solution as it implements pieces of the solution.

让 Claude 用代码实现其解决方案。在实现过程中，这也是一个要求它显式检查方案合理性的好时机（例如边写边自检关键假设）。

4. __Ask Claude to commit the result and create a pull request__. If relevant, this is also a good time to have Claude update any READMEs or changelogs with an explanation of what it just did.

让 Claude 提交结果并创建一个拉取请求（PR）。如果相关，这也是让 Claude 更新 README 或变更日志、解释刚刚做了什么的好时机。
Steps #1-#2 are crucial—without them, Claude tends to jump straight to coding a solution. While sometimes that's what you want, asking Claude to research and plan first significantly improves performance for problems requiring deeper thinking upfront.

步骤 #1-#2 至关重要——没有它们，Claude 往往会直接跳转到编码解决方案。虽然有时这正是您想要的，但要求 Claude 首先进行研究和规划会显著提高需要提前深入思考的问题的性能。

### b. Write tests, commit; code, iterate, commit | b. 编写测试、提交；编码、迭代、提交

This is an Anthropic-favorite workflow for changes that are easily verifiable with unit, integration, or end-to-end tests. Test-driven development (TDD) becomes even more powerful with agentic coding:

这是 Anthropic 偏爱的工作流程，用于易于通过单元、集成或端到端测试验证的更改。测试驱动开发（TDD）在智能体编码中变得更加强大：

1. __Ask Claude to write tests based on expected input/output pairs__. Be explicit about the fact that you're doing test-driven development so that it avoids creating mock implementations, even for functionality that doesn't exist yet in the codebase.

让 Claude 根据预期的输入/输出对编写测试。要明确说明你在做测试驱动开发（TDD），从而让它避免创建 mock 实现（即便代码库中还不存在该功能）。

2. __Tell Claude to run the tests and confirm they fail__. Explicitly telling it not to write any implementation code at this stage is often helpful.

让 Claude 运行测试并确认它们失败。在这个阶段，明确告诉它不要写任何实现代码通常会有帮助。

3. __Ask Claude to commit the tests__ when you're satisfied with them.

当你对测试满意后，让 Claude 提交这些测试。

4. __Ask Claude to write code that passes the tests__, instructing it not to modify the tests. Tell Claude to keep going until all tests pass. It will usually take a few iterations for Claude to write code, run the tests, adjust the code, and run the tests again.

让 Claude 编写能通过测试的代码，并指示它不要修改测试。告诉 Claude 持续迭代直到所有测试通过。通常需要多次循环：写代码 → 跑测试 → 调整代码 → 再跑测试。

   1. At this stage, it can help to ask it to verify with independent subagents that the implementation isn't overfitting to the tests

   在这个阶段，可以要求它使用独立的子智能体验证实现没有过度拟合测试

5. __Ask Claude to commit the code__ once you're satisfied with the changes.

当你对更改满意后，让 Claude 提交代码。
Claude performs best when it has a clear target to iterate against—a visual mock, a test case, or another kind of output. By providing expected outputs like tests, Claude can make changes, evaluate results, and incrementally improve until it succeeds.

当 Claude 有一个明确的目标进行迭代时，它的表现最佳——视觉模型、测试用例或其他类型的输出。通过提供预期的输出（如测试），Claude 可以进行更改、评估结果并增量改进，直到成功。

### c. Write code, screenshot result, iterate | c. 编写代码、截图结果、迭代

Similar to the testing workflow, you can provide Claude with visual targets:

与测试工作流程类似，您可以为 Claude 提供视觉目标：

1. __Give Claude a way to take browser screenshots__ (e.g., with the Puppeteer MCP server, an iOS simulator MCP server, or manually copy / paste screenshots into Claude).

给 Claude 一个截取浏览器截图的方式（例如使用 Puppeteer MCP 服务器、iOS 模拟器 MCP 服务器，或手动复制/粘贴截图到 Claude）。

2. __Give Claude a visual mock__ by copying / pasting or drag-dropping an image, or giving Claude the image file path.

通过复制/粘贴或拖拽图片（或提供图片文件路径）给 Claude 一个视觉稿（mock）。

3. __Ask Claude to implement the design__ in code, take screenshots of the result, and iterate until its result matches the mock.

让 Claude 用代码实现该设计，对结果截图并迭代，直到与视觉稿匹配。

4. __Ask Claude to commit__ when you're satisfied.

当你满意后，让 Claude 进行提交。
Like humans, Claude's outputs tend to improve significantly with iteration. While the first version might be good, after 2-3 iterations it will typically look much better. Give Claude the tools to see its outputs for best results.

与人类一样，Claude 的输出往往会随着迭代而显著改善。虽然第一个版本可能很好，但在 2-3 次迭代后，它通常会看起来好得多。给 Claude 提供查看其输出的工具以获得最佳结果。

![Safe YOLO mode | 安全 YOLO 模式](https://www-cdn.anthropic.com/images/4zrzovbb/website/6ea59a36fe82c2b300bceaf3b880a4b4852c552d-1600x1143.png)

安全 YOLO 模式演示了如何在容器中使用 `--dangerously-skip-permissions` 标志。

### d. Safe YOLO mode | d. 安全 YOLO 模式

Instead of supervising Claude, you can use `claude --dangerously-skip-permissions` to bypass all permission checks and let Claude work uninterrupted until completion. This works well for workflows like fixing lint errors or generating boilerplate code.

您可以不监督 Claude，而是使用 `claude --dangerously-skip-permissions` 绕过所有权限检查，让 Claude 不间断地工作直到完成。这适用于修复 lint（静态检查）错误或生成样板代码等工作流程。

Letting Claude run arbitrary commands is risky and can result in data loss, system corruption, or even data exfiltration (e.g., via prompt injection attacks). To minimize these risks, use `--dangerously-skip-permissions` in a container without internet access. You can follow this reference implementation using Docker Dev Containers.

让 Claude 运行任意命令是有风险的，可能导致数据丢失、系统损坏甚至数据外泄（例如，通过提示注入攻击）。为了最小化这些风险，请在没有互联网访问的容器中使用 `--dangerously-skip-permissions`。您可以按照这个参考实现使用 Docker Dev Containers。

### e. Codebase Q&A | e. 代码库问答

When onboarding to a new codebase, use Claude Code for learning and exploration. You can ask Claude the same sorts of questions you would ask another engineer on the project when pair programming. Claude can agentically search the codebase to answer general questions like:

在加入新代码库时，使用 Claude Code 进行学习和探索。您可以向 Claude 提出您在结对编程时会问项目中另一位工程师的同样类型的问题。Claude 可以智能地搜索代码库来回答一般性问题，例如：

- How does logging work?
- 日志是如何工作的？
- How do I make a new API endpoint?
- 如何创建新的 API 端点？
- What does `async move { ... }` do on line 134 of `foo.rs`?
- `foo.rs` 第 134 行的 `async move { ... }` 做什么？
- What edge cases does `CustomerOnboardingFlowImpl` handle?
- `CustomerOnboardingFlowImpl` 处理哪些边缘情况？
- Why are we calling `foo()` instead of `bar()` on line 333?
- 为什么在第 333 行调用 `foo()` 而不是 `bar()`？
- What's the equivalent of line 334 of `baz.py` in Java?
- `baz.py` 第 334 行在 Java 中的等价实现是什么？

At Anthropic, using Claude Code in this way has become our core onboarding workflow, significantly improving ramp-up time and reducing load on other engineers. No special prompting is required! Simply ask questions, and Claude will explore the code to find answers.

在 Anthropic，以这种方式使用 Claude Code 已成为我们核心的入职工作流程，显著提高了上手时间并减少了对其他工程师的负担。不需要特殊的提示！只需提问，Claude 将探索代码以找到答案。

![Use Claude to interact with git | 使用 Claude 与 git 交互](https://www-cdn.anthropic.com/images/4zrzovbb/website/a08ea13c2359aac0eceacebf2e15f81e8e8ec8d2-1600x1278.png)

使用 Claude 与 git 交互的示例界面，显示了搜索 git 历史记录的功能。

### f. Use Claude to interact with git | f. 使用 Claude 与 git 交互

Claude can effectively handle many git operations. Many Anthropic engineers use Claude for 90%+ of our _git_ interactions:

Claude 可以有效地处理许多 git 操作。许多 Anthropic 工程师使用 Claude 处理我们 90% 以上的 _git_ 交互：

- __Searching _git_ history__ to answer questions like "What changes made it into v1.2.3?", "Who owns this particular feature?", or "Why was this API designed this way?" It helps to explicitly prompt Claude to look through git history to answer queries like these.

- __搜索 _git_ 历史记录__以回答诸如"哪些更改进入了 v1.2.3？"、"谁拥有这个特定功能？"或"为什么这个 API 这样设计？"等问题。明确提示 Claude 查看 git 历史记录来回答此类查询会有所帮助。

- __Writing commit messages__. Claude will look at your changes and recent history automatically to compose a message taking all the relevant context into account

- __编写提交消息__。Claude 将自动查看您的更改和最近的历史记录，以撰写一条考虑所有相关上下文的消息

- __Handling complex git operations__ like reverting files, resolving rebase conflicts, and comparing and grafting patches

- __处理复杂的 git 操作__，例如恢复文件、解决 rebase 冲突以及比较和移植补丁

### g. Use Claude to interact with GitHub | g. 使用 Claude 与 GitHub 交互

Claude Code can manage many GitHub interactions:

Claude Code 可以管理许多 GitHub 交互：

- __Creating pull requests__: Claude understands the shorthand "pr" and will generate appropriate commit messages based on the diff and surrounding context.

- __创建拉取请求__：Claude 理解简写"pr"，并将根据差异和周围上下文生成适当的提交消息。

- __Implementing one-shot resolutions__ for simple code review comments: just tell it to fix comments on your PR (optionally, give it more specific instructions) and push back to the PR branch when it's done.

- __实现一次性解决方案__，用于简单的代码审查评论：只需告诉它修复您的 PR（Pull Request，拉取请求）上的评论（可选地，给它更具体的指令），并在完成后推回 PR 分支。

- __Fixing failing builds__ or linter warnings

- __修复失败的构建__或 linter 警告

- __Categorizing and triaging open issues__ by asking Claude to loop over open GitHub issues

- __对开放问题进行分类和分类__，通过要求 Claude 循环遍历开放的 GitHub 问题

This eliminates the need to remember `gh` command line syntax while automating routine tasks.

这消除了记住 `gh` 命令行语法的需要，同时自动化了常规任务。

### h. Use Claude to work with Jupyter notebooks | h. 使用 Claude 处理 Jupyter 笔记本

Researchers and data scientists at Anthropic use Claude Code to read and write Jupyter notebooks. Claude can interpret outputs, including images, providing a fast way to explore and interact with data. There are no required prompts or workflows, but a workflow we recommend is to have Claude Code and a `.ipynb` file open side-by-side in VS Code.

Anthropic 的研究人员和数据科学家使用 Claude Code 来读写 Jupyter 笔记本。Claude 可以解释输出（包括图像），提供一种快速探索和交互数据的方式。没有必需的提示或工作流程，但我们推荐的工作流程是在 VS Code 中并排打开 Claude Code 和 `.ipynb` 文件。

You can also ask Claude to clean up or make aesthetic improvements to your Jupyter notebook before you show it to colleagues. Specifically telling it to make the notebook or its data visualizations "aesthetically pleasing" tends to help remind it that it's optimizing for a human viewing experience.

您还可以要求 Claude 在向同事展示之前清理或对 Jupyter 笔记本进行美观改进。特别告诉它使笔记本或其数据可视化"美观"有助于提醒它正在优化人类观看体验。

---

## 4. Optimize your workflow | 4. 优化您的工作流程

The suggestions below apply across all workflows:

以下建议适用于所有工作流程：

### a. Be specific in your instructions | a. 在您的指令中要具体

Claude Code's success rate improves significantly with more specific instructions, especially on first attempts. Giving clear directions upfront reduces the need for course corrections later.

Claude Code 的成功率随着更具体的指令而显著提高，尤其是在第一次尝试时。提前给出明确的方向可以减少以后纠正航向的需要。

For example:

例如：

| Poor | 差 | Good | 好 |
| --- | --- | --- | --- |
| add tests for foo.py | 为 foo.py 添加测试 | write a new test case for foo.py, covering the edge case where the user is logged out. avoid mocks | 为 foo.py 编写一个新的测试用例，覆盖用户注销的边缘情况。避免使用 mocks（模拟对象） |
| why does ExecutionFactory have such a weird api? | 为什么 ExecutionFactory 有这么奇怪的 api（Application Programming Interface，应用程序接口）？ | look through ExecutionFactory's git history and summarize how its api came to be | 查看 ExecutionFactory 的 git 历史记录并总结其 api 是如何形成的 |
| add a calendar widget | 添加日历小部件 | look at how existing widgets are implemented on the home page to understand the patterns and specifically how code and interfaces are separated out. HotDogWidget.php is a good example to start with. then, follow the pattern to implement a new calendar widget that lets the user select a month and paginate forwards/backwards to pick a year. Build from scratch without libraries other than the ones already used in the rest of the codebase. | 查看主页上现有小部件的实现方式，以了解模式，特别是代码和接口是如何分离的。HotDogWidget.php 是一个很好的起点示例。然后，按照该模式实现一个新的日历小部件，让用户可以选择一个月份并向前/向后分页来选择年份。从头开始构建，不使用代码库其余部分中已使用的库以外的库。 |

Claude can infer intent, but it can't read minds. Specificity leads to better alignment with expectations.

Claude 可以推断意图，但它不能读心。具体性导致与期望的更好一致性。

![Give Claude images | 给 Claude 提供图片](https://www-cdn.anthropic.com/images/4zrzovbb/website/75e1b57a0b696e7aafeca1ed5fa6ba7c601a5953-1360x1126.png)

给 Claude 提供图片的示例界面，显示了拖放图片的功能。

### b. Give Claude images | b. 给 Claude 提供图片

Claude excels with images and diagrams through several methods:

Claude 通过几种方法在图像和图表方面表现出色：

- __Paste screenshots__ (pro tip: hit _cmd+ctrl+shift+4_ in macOS to screenshot to clipboard and _ctrl+v_ to paste. Note that this is not cmd+v like you would usually use to paste on mac and does not work remotely.)

- __粘贴截图__（专业提示：在 macOS 中按 _cmd+ctrl+shift+4_ 截图到剪贴板，然后按 _ctrl+v_ 粘贴。请注意，这不是 mac 上通常用于粘贴的 cmd+v，并且不能远程工作。）

- __Drag and drop__ images directly into the prompt input

- __直接将图片拖放到__提示输入中

- __Provide file paths__ for images

- __提供图片的文件路径__

This is particularly useful when working with design mocks as reference points for UI development, and visual charts for analysis and debugging. If you are not adding visuals to context, it can still be helpful to be clear with Claude about how important it is for the result to be visually appealing.

这在将设计模型作为 UI 开发的参考点以及用于分析和调试的视觉图表时特别有用。如果您不向上下文添加视觉效果，仍然可以向 Claude 明确结果在视觉上有多重要。

![Mention files you want Claude to look at or work on | 提及您希望 Claude 查看或处理的文件](https://www-cdn.anthropic.com/images/4zrzovbb/website/7372868757dd17b6f2d3fef98d499d7991d89800-1450x1164.png)

提及您希望 Claude 查看或处理的文件的示例界面，显示了 tab-completion（Tab 键自动补全）功能。

### c. Mention files you want Claude to look at or work on | c. 提及您希望 Claude 查看或处理的文件

Use tab-completion to quickly reference files or folders anywhere in your repository, helping Claude find or update the right resources.

使用 tab-completion（Tab 补全）快速引用存储库中任何位置的文件或文件夹，帮助 Claude 找到或更新正确的资源。

![Give Claude URLs | 给 Claude 提供 URL](https://www-cdn.anthropic.com/images/4zrzovbb/website/e071de707f209bbaa7f16b593cc7ed0739875dae-1306x1088.png)

给 Claude 提供 URL（统一资源定位符）的示例界面，显示了如何提供网页链接。

### d. Give Claude URLs | d. 给 Claude 提供 URL

Paste specific URLs alongside your prompts for Claude to fetch and read. To avoid permission prompts for the same domains (e.g., docs.foo.com), use `/permissions` to add domains to your allowlist.

将特定的 URL 与您的提示一起粘贴，以供 Claude 获取和阅读。为避免对相同域名（例如 docs.foo.com）的权限提示，请使用 `/permissions` 将域名添加到您的允许列表中。

### e. Course correct early and often | e. 及早且经常纠正航向

While auto-accept mode (shift+tab to toggle) lets Claude work autonomously, you'll typically get better results by being an active collaborator and guiding Claude's approach. You can get the best results by thoroughly explaining the task to Claude at the beginning, but you can also course correct Claude at any time.

虽然自动接受模式（shift+tab 切换）让 Claude 自主工作，但通过成为积极的协作者并指导 Claude 的方法，您通常会获得更好的结果。您可以通过在开始时彻底向 Claude 解释任务来获得最佳结果，但您也可以随时纠正 Claude 的航向。

These four tools help with course correction:

这四个工具有助于纠正航向：

- __Ask Claude to make a plan__ before coding. Explicitly tell it not to code until you've confirmed its plan looks good.

- __在编码之前要求 Claude 制定计划__。明确告诉它在您确认计划看起来不错之前不要编码。

- __Press Escape to interrupt__ Claude during any phase (thinking, tool calls, file edits), preserving context so you can redirect or expand instructions.

- __按 Escape 键中断__ Claude 在任何阶段（思考、工具调用、文件编辑），保留上下文以便您可以重定向或扩展指令。

- __Double-tap Escape to jump back in history__, edit a previous prompt, and explore a different direction. You can edit the prompt and repeat until you get the result you're looking for.

- __双击 Escape 键跳回历史记录__，编辑以前的提示，并探索不同的方向。您可以编辑提示并重复，直到获得您正在寻找的结果。

- __Ask Claude to undo changes__, often in conjunction with option #2 to take a different approach.

- __要求 Claude 撤销更改__，通常与选项 #2 结合使用以采用不同的方法。

Though Claude Code occasionally solves problems perfectly on the first attempt, using these correction tools generally produces better solutions faster.

虽然 Claude Code 偶尔会在第一次尝试时完美解决问题，但使用这些纠正工具通常会更快地产生更好的解决方案。

### f. Use `/clear` to keep context focused | f. 使用 `/clear` 保持上下文专注

During long sessions, Claude's context window can fill with irrelevant conversation, file contents, and commands. This can reduce performance and sometimes distract Claude. Use the `/clear` command frequently between tasks to reset the context window.

在长会话期间，Claude 的上下文窗口可能充满不相关的对话、文件内容和命令。这可能会降低性能，有时会分散 Claude 的注意力。在任务之间频繁使用 `/clear` 命令来重置上下文窗口。

### g. Use checklists and scratchpads for complex workflows | g. 使用清单和草稿本处理复杂的工作流程

For large tasks with multiple steps or requiring exhaustive solutions—like code migrations, fixing numerous lint errors, or running complex build scripts—improve performance by having Claude use a Markdown file (or even a GitHub issue!) as a checklist and working scratchpad:

对于具有多个步骤或需要详尽解决方案的大型任务——例如代码迁移、修复大量 lint 错误或运行复杂的构建脚本——通过让 Claude 使用 Markdown 文件（甚至 GitHub 问题！）作为清单和工作草稿本来提高性能：

For example, to fix a large number of lint issues, you can do the following:

例如，要修复大量 lint 问题，您可以执行以下操作：

1. __Tell Claude to run the lint command__ and write all resulting errors (with filenames and line numbers) to a Markdown checklist

指示 Claude 运行 lint 命令并将所有结果错误（包括文件名和行号）写入 Markdown 清单。

2. __Instruct Claude to address each issue one by one__, fixing and verifying before checking it off and moving to the next

指示 Claude 逐一解决每个问题，在修复和验证后再检查并移动到下一个。

### h. Pass data into Claude | h. 将数据传递给 Claude

Several methods exist for providing data to Claude:

有几种方法可以为 Claude 提供数据：

- __Copy and paste__ directly into your prompt (most common approach)

- __直接复制和粘贴__到您的提示中（最常见的方法）

- __Pipe into Claude Code__ (e.g., `cat foo.txt | claude`), particularly useful for logs, CSVs, and large data

- __通过管道传输到 Claude Code__（例如，`cat foo.txt | claude`），特别适用于日志、CSV 和大数据

- __Tell Claude to pull data__ via bash commands, MCP tools, or custom slash commands

- __告诉 Claude 通过 bash 命令、MCP 工具或自定义斜杠命令拉取数据__

- __Ask Claude to read files__ or fetch URLs (works for images too)

- __要求 Claude 读取文件__或获取 URL（也适用于图片）

Most sessions involve a combination of these approaches. For example, you can pipe in a log file, then tell Claude to use a tool to pull in additional context to debug the logs.

大多数会话涉及这些方法的组合。例如，您可以通过管道传输日志文件，然后告诉 Claude 使用工具拉入额外的上下文来调试日志。

---

## 5. Use headless mode to automate your infra | 5. 使用无头模式自动化您的基础设施

Claude Code includes headless mode for non-interactive contexts like CI, pre-commit hooks, build scripts, and automation. Use the `-p` flag with a prompt to enable headless mode, and `--output-format stream-json` for streaming JSON output.

Claude Code 包含用于非交互式上下文（如 CI、预提交挂钩、构建脚本和自动化）的无头模式。使用 `-p` 标志和提示来启用无头模式，并使用 `--output-format stream-json` 进行流式 JSON 输出。

Note that headless mode does not persist between sessions. You have to trigger it each session.

请注意，无头模式不会在会话之间持久化。您必须在每次会话时触发它。

### a. Use Claude for issue triage | a. 使用 Claude 进行问题分类

Headless mode can power automations triggered by GitHub events, such as when a new issue is created in your repository. For example, the public Claude Code repository uses Claude to inspect new issues as they come in and assign appropriate labels.

无头模式可以为由 GitHub 事件触发的自动化提供动力，例如在您的存储库中创建新问题时。例如，公共 Claude Code 存储库使用 Claude 来检查传入的新问题并分配适当的标签。

### b. Use Claude as a linter | b. 使用 Claude 作为 linter

Claude Code can provide subjective code reviews beyond what traditional linting tools detect, identifying issues like typos, stale comments, misleading function or variable names, and more.

Claude Code 可以提供传统 lint 工具无法检测的主观代码审查，识别诸如拼写错误、过时评论、误导性的函数或变量名称等问题。

---

## 6. Uplevel with multi-Claude workflows | 6. 通过多 Claude 工作流程提升

Beyond standalone usage, some of the most powerful applications involve running multiple Claude instances in parallel:

除了独立使用之外，一些最强大的应用程序涉及并行运行多个 Claude 实例：

### a. Have one Claude write code; use another Claude to verify | a. 让一个 Claude 编写代码；使用另一个 Claude 验证

A simple but effective approach is to have one Claude write code while another reviews or tests it. Similar to working with multiple engineers, sometimes having separate context is beneficial:

一个简单但有效的方法是让一个 Claude 编写代码，而另一个审查或测试它。与使用多个工程师类似，有时拥有独立的上下文是有益的：

1. Use Claude to write code
使用 Claude 编写代码。

2. Run `/clear` or start a second Claude in another terminal
运行 `/clear` 或在另一个终端启动第二个 Claude。

3. Have the second Claude review the first Claude's work
让第二个 Claude 审查第一个 Claude 的工作。

4. Start another Claude (or `/clear` again) to read both the code and review feedback
再启动一个 Claude（或再次 `/clear`），让它同时阅读代码和审查反馈。

5. Have this Claude edit the code based on the feedback
让这个 Claude 根据反馈修改代码。

You can do something similar with tests: have one Claude write tests, then have another Claude write code to make the tests pass. You can even have your Claude instances communicate with each other by giving them separate working scratchpads and telling them which one to write to and which one to read from.

您可以对测试做类似的事情：让一个 Claude 编写测试，然后让另一个 Claude 编写代码以使测试通过。您甚至可以通过为您的 Claude 实例提供独立的工作草稿本并告诉它们写入哪一个和从哪一个读取来让它们相互通信。

This separation often yields better results than having a single Claude handle everything.

这种分离通常会产生比让单个 Claude 处理所有事情更好的结果。

### b. Have multiple checkouts of your repo | b. 拥有多个存储库签出

Rather than waiting for Claude to complete each step, something many engineers at Anthropic do is:

与其等待 Claude 完成每个步骤，许多 Anthropic 工程师做的事情是：

1. __Create 3-4 git checkouts__ in separate folders

在单独的文件夹中创建 3-4 个 git 签出。

2. __Open each folder__ in separate terminal tabs

在单独的终端选项卡中打开每个文件夹。

3. __Start Claude in each folder__ with different tasks

在每个文件夹中启动 Claude 并执行不同的任务。

4. __Cycle through__ to check progress and approve/deny permission requests

循环检查进度并批准/拒绝权限请求。

### c. Use git worktrees | c. 使用 git worktrees

This approach shines for multiple independent tasks, offering a lighter-weight alternative to multiple checkouts. Git worktrees allow you to check out multiple branches from the same repository into separate directories. Each worktree has its own working directory with isolated files, while sharing the same Git history and reflog.

这种方法在多个独立任务方面表现出色，提供了多个签出的轻量级替代方案。Git worktrees（工作树）允许您从同一存储库中签出多个分支到单独的目录中。每个 worktree 都有自己的工作目录和隔离的文件，同时共享相同的 Git 历史记录和 reflog（引用日志）。

Using git worktrees enables you to run multiple Claude sessions simultaneously on different parts of your project, each focused on its own independent task. For instance, you might have one Claude refactoring your authentication system while another builds a completely unrelated data visualization component. Since the tasks don't overlap, each Claude can work at full speed without waiting for the other's changes or dealing with merge conflicts:

使用 git worktrees（工作树）使您能够在项目的不同部分同时运行多个 Claude 会话，每个会话专注于其独立的任务。例如，您可能有一个 Claude 重构您的身份验证系统，而另一个构建完全不相关的数据可视化组件。由于任务不重叠，每个 Claude 可以全速工作，而无需等待另一个的更改或处理合并冲突：

1. __Create worktrees__: `git worktree add ../project-feature-a feature-a`

创建 worktrees：`git worktree add ../project-feature-a feature-a`

2. __Launch Claude in each worktree__: `cd ../project-feature-a && claude`

在每个 worktree 中启动 Claude：`cd ../project-feature-a && claude`

3. __Create additional worktrees__ as needed (repeat steps 1-2 in new terminal tabs)

根据需要创建额外的 worktrees（在新终端选项卡中重复步骤 1-2）。

Some tips:

一些提示：

- Use consistent naming conventions
- 使用一致的命名规范

- Maintain one terminal tab per worktree
- 为每个 worktree 维护一个终端选项卡

- If you're on a Mac and use iTerm2, set a notification when Claude needs attention
- 如果您在 Mac 上使用 iTerm2，请在 Claude 需要注意时设置通知

- Use a separate IDE window per worktree
- 为不同的 worktree 使用单独的 IDE（集成开发环境）窗口

- Clean up when you're done: `git worktree remove ../project-feature-a`
- 完成后清理：`git worktree remove ../project-feature-a`

### d. Use headless mode with a custom harness | d. 将无头模式与自定义工具一起使用

`claude -p` (headless mode) integrates Claude Code programmatically into larger workflows while leveraging its built-in tools and system prompt. There are two primary patterns for using headless mode:

`claude -p`（无头模式）以编程方式将 Claude Code 集成到更大的工作流程中，同时利用其内置工具和系统提示。使用无头模式有两种主要模式：

1. __Fanning out__ handles large migrations or analyses (e.g., analyzing sentiment in hundreds of logs or analyzing thousands of CSVs):

__Fanning out__（扇出）用于处理大规模迁移或分析（例如分析数百份日志的情感倾向，或分析数千个 CSV）：

   1. Have Claude write a script to generate a task list. For example, generate a list of 2k files that need to be migrated from framework A to framework B.

   让 Claude 编写脚本生成任务列表。例如，生成一个需要从框架 A 迁移到框架 B 的 2000 个文件清单。

   2. Loop through tasks, calling Claude programmatically for each and giving it a task and a set of tools it can use. For example: `claude -p "migrate foo.py from React to Vue. When you are done, you MUST return the string OK if you succeeded, or FAIL if the task failed." --allowedTools Edit Bash(git commit:*)`

   遍历任务，对每个任务以编程方式调用 Claude，并给它任务说明与可用工具集合。例如：`claude -p "migrate foo.py from React to Vue. When you are done, you MUST return the string OK if you succeeded, or FAIL if the task failed." --allowedTools Edit Bash(git commit:*)`

   3. Run the script several times and refine your prompt to get the desired outcome.

   多次运行脚本，并不断迭代你的提示，直到达到期望的结果。

2. __Pipelining__ integrates Claude into existing data/processing pipelines:

__Pipelining__（流水线）将 Claude 集成到现有的数据/处理流水线中：

   1. Call `claude -p "<your prompt>" --json | your_command`, where `your_command` is the next step of your processing pipeline

   调用 `claude -p "<your prompt>" --json | your_command`，其中 `your_command` 是你处理流水线的下一步命令。

   2. That's it! JSON output (optional) can help provide structure for easier automated processing.

   就是这样！JSON 输出（可选）可以提供结构，便于自动化处理。
For both of these use cases, it can be helpful to use the `--verbose` flag for debugging the Claude invocation. We generally recommend turning verbose mode off in production for cleaner output.

对于这两个用例，使用 `--verbose` 标志来调试 Claude 调用可能会有所帮助。我们通常建议在生产环境中关闭详细模式以获得更清晰的输出。

What are your tips and best practices for working with Claude Code? Tag [@AnthropicAI](https://twitter.com/AnthropicAI) so we can see what you're building!

您在使用 Claude Code 时有什么技巧和最佳实践？标记 [@AnthropicAI](https://twitter.com/AnthropicAI)，让我们看看您正在构建什么！

---

## Acknowledgements | 致谢

Written by Boris Cherny. This work draws upon best practices from across the broader Claude Code user community, whose creative approaches and workflows continue to inspire us. Special thanks also to Daisy Hollman, Ashwin Bhat, Cat Wu, Sid Bidasaria, Cal Rueb, Nodir Turakulov, Barry Zhang, Drew Hodun and many other Anthropic engineers whose valuable insights and practical experience with Claude Code helped shape these recommendations.

本文由 Boris Cherny 撰写。这项工作借鉴了更广泛的 Claude Code 用户社区的最佳实践，他们的创造性方法和工作流程继续激励着我们。特别感谢 Daisy Hollman、Ashwin Bhat、Cat Wu、Sid Bidasaria、Cal Rueb、Nodir Turakulov、Barry Zhang、Drew Hodun 和许多其他 Anthropic 工程师，他们宝贵的见解和使用 Claude Code 的实践经验帮助塑造了这些建议。

---

## Sources | 来源

- [Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices)

- [Claude Code：智能体编码的最佳实践](https://www.anthropic.com/engineering/claude-code-best-practices)
