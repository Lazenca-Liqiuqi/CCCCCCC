# Introducing Advanced Tool Use on the Claude Developer Platform
Claude 开发者平台高级工具使用介绍

Claude can now discover, learn, and execute tools dynamically to enable agents that take action in the real world. Here's how.
Claude 现在可以动态发现、学习和执行工具，以实现能够在现实世界中采取行动的智能体。以下是如何实现。

---

The future of AI agents is one where models work seamlessly across hundreds or thousands of tools. An IDE assistant that integrates git operations, file manipulation, package managers, testing frameworks, and deployment pipelines. An operations coordinator that connects Slack, GitHub, Google Drive, Jira, company databases, and dozens of MCP servers simultaneously.
AI 智能体的未来是模型在数百或数千个工具之间无缝工作的世界。一个集成 git 操作、文件操作、包管理器、测试框架和部署管道的 IDE 助手。一个同时连接 Slack、GitHub、Google Drive、Jira、公司数据库和数十个 MCP 服务器的运营协调器。

To build effective agents, they need to work with unlimited tool libraries without stuffing every definition into context upfront. Our blog article on using code execution with MCP discussed how tool results and definitions can sometimes consume 50,000+ tokens before an agent reads a request. Agents should discover and load tools on-demand, keeping only what's relevant for the current task.
要构建有效的智能体，它们需要与无限的工具库一起工作，而不会将每个定义都预先填充到上下文中。我们关于使用 MCP 执行代码的博客文章讨论了工具结果和定义有时如何在智能体读取请求之前消耗 50,000+ 个令牌。智能体应该按需发现和加载工具，只保留与当前任务相关的内容。

Agents also need the ability to call tools from code. When using natural language tool calling, each invocation requires a full inference pass, and intermediate results pile up in context whether they're useful or not. Code is a natural fit for orchestration logic, such as loops, conditionals, and data transformations. Agents need the flexibility to choose between code execution and inference based on the task at hand.
智能体还需要从代码调用工具的能力。当使用自然语言工具调用时，每次调用都需要完整的推理过程，中间结果在上下文中堆积，无论它们是否有用。代码是编排逻辑的自然选择，例如循环、条件语句和数据转换。智能体需要根据手头的任务在代码执行和推理之间进行选择的灵活性。

Agents also need to learn correct tool usage from examples, not just schema definitions. JSON schemas define what's structurally valid, but can't express usage patterns: when to include optional parameters, which combinations make sense, or what conventions your API expects.
智能体还需要从示例中学习正确的工具使用，而不仅仅是模式定义。JSON 模式定义了结构上有效的内容，但无法表达使用模式：何时包含可选参数，哪些组合有意义，或者你的 API 期望什么约定。

Today, we're releasing three features that make this possible:
今天，我们发布了三个实现这一点的功能：

- __Tool Search Tool,__ which allows Claude to use search tools to access thousands of tools without consuming its context window
- __工具搜索工具__，允许 Claude 使用搜索工具访问数千个工具，而不会消耗其上下文窗口

- __Programmatic Tool Calling__, which allows Claude to invoke tools in a code execution environment reducing the impact on the model's context window
- __编程式工具调用__，允许 Claude 在代码执行环境中调用工具，减少对模型上下文窗口的影响

- __Tool Use Examples__, which provides a universal standard for demonstrating how to effectively use a given tool
- __工具使用示例__，提供了演示如何有效使用给定工具的通用标准

In internal testing, we've found these features have helped us build things that wouldn't have been possible with conventional tool use patterns. For example, __Claude for Excel__ uses Programmatic Tool Calling to read and modify spreadsheets with thousands of rows without overloading the model's context window.
在内部测试中，我们发现这些功能帮助我们构建了使用传统工具使用模式无法实现的东西。例如，__Excel 版 Claude__ 使用编程式工具调用来读取和修改具有数千行的电子表格，而不会使模型的上下文窗口过载。

Based on our experience, we believe these features open up new possibilities for what you can build with Claude.
根据我们的经验，我们认为这些功能为你使用 Claude 构建的东西开辟了新的可能性。

## Tool Search Tool
工具搜索工具

### The Challenge
挑战

MCP tool definitions provide important context, but as more servers connect, those tokens can add up. Consider a five-server setup:
MCP 工具定义提供了重要的上下文，但随着更多服务器的连接，这些令牌会累积。考虑一个五服务器设置：

- GitHub: 35 tools (~26K tokens)
- Slack: 11 tools (~21K tokens)
- Sentry: 5 tools (~3K tokens)
- Grafana: 5 tools (~3K tokens)
- Splunk: 2 tools (~2K tokens)

That's 58 tools consuming approximately 55K tokens before the conversation even starts. Add more servers like Jira (which alone uses ~17K tokens) and you're quickly approaching 100K+ token overhead. At Anthropic, we've seen tool definitions consume 134K tokens before optimization.
这是 58 个工具在对话甚至开始之前消耗了大约 55K 个令牌。添加更多服务器（如 Jira，仅它就使用约 17K 个令牌），你很快就接近 100K+ 令牌开销。在 Anthropic，我们看到工具定义在优化之前消耗了 134K 个令牌。

But token cost isn't the only issue. The most common failures are wrong tool selection and incorrect parameters, especially when tools have similar names like `notification-send-user` vs. `notification-send-channel`.
但令牌成本并不是唯一的问题。最常见的失败是错误的工具选择和不正确的参数，尤其是当工具具有相似名称时，例如 `notification-send-user` 与 `notification-send-channel`。

### Our Solution
我们的解决方案

Instead of loading all tool definitions upfront, the Tool Search Tool discovers tools on-demand. Claude only sees the tools it actually needs for the current task.
工具搜索工具不是预先加载所有工具定义，而是按需发现工具。Claude 只看到它当前任务实际需要的工具。

![Image 1: Tool Search Tool diagram](https://example.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2Ff359296f770706608901eadaffbff4ca0b67874c-1999x1125.png&w=3840&q=75)

_Tool Search Tool preserves 191,300 tokens of context compared to 122,800 with Claude's traditional approach._
_工具搜索工具保留了 191,300 个令牌的上下文，而 Claude 的传统方法为 122,800 个令牌。_

Traditional approach:
传统方法：

- All tool definitions loaded upfront (~72K tokens for 50+ MCP tools)
- 预先加载所有工具定义（50+ 个 MCP 工具约 72K 个令牌）
- Conversation history and system prompt compete for remaining space
- 对话历史和系统提示争夺剩余空间
- Total context consumption: ~77K tokens before any work begins
- 总上下文消耗：任何工作开始前约 77K 个令牌

With the Tool Search Tool:
使用工具搜索工具：

- Only the Tool Search Tool loaded upfront (~500 tokens)
- 只预先加载工具搜索工具（约 500 个令牌）
- Tools discovered on-demand as needed (3-5 relevant tools, ~3K tokens)
- 根据需要按需发现工具（3-5 个相关工具，约 3K 个令牌）
- Total context consumption: ~8.7K tokens, preserving 95% of context window
- 总上下文消耗：约 8.7K 个令牌，保留 95% 的上下文窗口

This represents an 85% reduction in token usage while maintaining access to your full tool library. Internal testing showed significant accuracy improvements on MCP evaluations when working with large tool libraries. Opus 4 improved from 49% to 74%, and Opus 4.5 improved from 79.5% to 88.1% with Tool Search Tool enabled.
这代表了令牌使用减少了 85%，同时保持对完整工具库的访问。内部测试显示，在使用大型工具库时，MCP 评估的准确性显著提高。Opus 4 从 49% 提高到 74%，Opus 4.5 从 79.5% 提高到 88.1%，启用了工具搜索工具。

### How the Tool Search Tool Works
工具搜索工具的工作原理

The Tool Search Tool lets Claude dynamically discover tools instead of loading all definitions upfront. You provide all your tool definitions to the API, but mark tools with `defer_loading: true` to make them discoverable on-demand. Deferred tools aren't loaded into Claude's context initially. Claude only sees the Tool Search Tool itself plus any tools with `defer_loading: false` (your most critical, frequently-used tools).
工具搜索工具允许 Claude 动态发现工具，而不是预先加载所有定义。你向 API 提供所有工具定义，但使用 `defer_loading: true` 标记工具以使其可按需发现。延迟的工具最初不会加载到 Claude 的上下文中。Claude 只看到工具搜索工具本身以及任何带有 `defer_loading: false` 的工具（你最重要、最常用的工具）。

When Claude needs specific capabilities, it searches for relevant tools. The Tool Search Tool returns references to matching tools, which get expanded into full definitions in Claude's context.
当 Claude 需要特定功能时，它会搜索相关工具。工具搜索工具返回匹配工具的引用，这些引用在 Claude 的上下文中扩展为完整定义。

For example, if Claude needs to interact with GitHub, it searches for "github," and only `github.createPullRequest` and `github.listIssues` get loaded—not your other 50+ tools from Slack, Jira, and Google Drive.
例如，如果 Claude 需要与 GitHub 交互，它会搜索"github"，只有 `github.createPullRequest` 和 `github.listIssues` 被加载——而不是来自 Slack、Jira 和 Google Drive 的其他 50+ 个工具。

This way, Claude has access to your full tool library while only paying the token cost for tools it actually needs.
这样，Claude 可以访问你的完整工具库，而只为其实际需要的工具支付令牌成本。

__Prompt caching note:__ Tool Search Tool doesn't break prompt caching because deferred tools are excluded from the initial prompt entirely. They're only added to context after Claude searches for them, so your system prompt and core tool definitions remain cacheable.
__提示缓存说明：__ 工具搜索工具不会破坏提示缓存，因为延迟的工具完全从初始提示中排除。它们只有在 Claude 搜索它们之后才会添加到上下文中，因此你的系统提示和核心工具定义仍然可缓存。

__Implementation:__
__实现：__

```json
{
  "tools": [
    // Include a tool search tool (regex, BM25, or custom)
    {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},

    // Mark tools for on-demand discovery
    {
      "name": "github.createPullRequest",
      "description": "Create a pull request",
      "input_schema": {...},
      "defer_loading": true
    }
    // ... hundreds more deferred tools with defer_loading: true
  ]
}
```

For MCP servers, you can defer loading entire servers while keeping specific high-use tools loaded:
对于 MCP 服务器，你可以延迟加载整个服务器，同时保持特定的高使用工具加载：

```json
{
  "type": "mcp_toolset",
  "mcp_server_name": "google-drive",
  "default_config": {"defer_loading": true}, # defer loading the entire server
  "configs": {
    "search_files": {
      "defer_loading": false
    }  // Keep most used tool loaded
  }
}
```

The Claude Developer Platform provides regex-based and BM25-based search tools out of the box, but you can also implement custom search tools using embeddings or other strategies.
Claude 开发者平台开箱即提供基于正则表达式和 BM25 的搜索工具，但你也可以使用嵌入或其他策略实现自定义搜索工具。

### When to Use the Tool Search Tool
何时使用工具搜索工具

Like any architectural decision, enabling the Tool Search Tool involves trade-offs. The feature adds a search step before tool invocation, so it delivers the best ROI when the context savings and accuracy improvements outweigh additional latency.
与任何架构决策一样，启用工具搜索工具涉及权衡。该功能在工具调用之前添加了搜索步骤，因此当上下文节省和准确性提高超过额外延迟时，它提供最佳投资回报率。

__Use it when:__
__使用它时：__

- Tool definitions consuming >10K tokens
- 工具定义消耗 >10K 个令牌
- Experiencing tool selection accuracy issues
- 遇到工具选择准确性问题
- Building MCP-powered systems with multiple servers
- 构建具有多个服务器的 MCP 驱动系统
- 10+ tools available
- 可用 10+ 个工具

__Less beneficial when:__
__不太有益时：__

- Small tool library (<10 tools)
- 小型工具库（<10 个工具）
- All tools used frequently in every session
- 每个会话中频繁使用所有工具
- Tool definitions are compact
- 工具定义紧凑

## Programmatic Tool Calling
编程式工具调用

### The Challenge
挑战

Traditional tool calling creates two fundamental problems as workflows become more complex:
传统工具调用在工作流变得更加复杂时会产生两个基本问题：

- __Context pollution from intermediate results__: When Claude analyzes a 10MB log file for error patterns, the entire file enters its context window, even though Claude only needs a summary of error frequencies. When fetching customer data across multiple tables, every record accumulates in context regardless of relevance. These intermediate results consume massive token budgets and can push important information out of the context window entirely.
- __来自中间结果的上下文污染：__ 当 Claude 分析 10MB 日志文件以查找错误模式时，整个文件进入其上下文窗口，尽管 Claude 只需要错误频率的摘要。当跨多个表获取客户数据时，每条记录都会累积在上下文中，无论是否相关。这些中间结果消耗大量的令牌预算，并且可能将重要信息完全推出上下文窗口。

- __Inference overhead and manual synthesis__: Each tool call requires a full model inference pass. After receiving results, Claude must "eyeball" the data to extract relevant information, reason about how pieces fit together, and decide what to do next—all through natural language processing. A five tool workflow means five inference passes plus Claude parsing each result, comparing values, and synthesizing conclusions. This is both slow and error-prone.
- __推理开销和手动综合：__ 每个工具调用都需要完整的模型推理过程。接收结果后，Claude 必须"目测"数据以提取相关信息，推理各部分如何组合在一起，并决定下一步做什么——所有这些都通过自然语言处理。五个工具的工作流程意味着五次推理过程加上 Claude 解析每个结果、比较值和综合结论。这既缓慢又容易出错。

### Our Solution
我们的解决方案

Programmatic Tool Calling enables Claude to orchestrate tools through code rather than through individual API round-trips. Instead of Claude requesting tools one at a time with each result being returned to its context, Claude writes code that calls multiple tools, processes their outputs, and controls what information actually enters its context window.
编程式工具调用使 Claude 能够通过代码而不是通过单独的 API 往返来编排工具。Claude 编写调用多个工具、处理其输出并控制实际进入其上下文窗口的信息的代码，而不是 Claude 一次请求一个工具，每个结果都返回到其上下文。

Claude excels at writing code and by letting it express orchestration logic in Python rather than through natural language tool invocations, you get more reliable, precise control flow. Loops, conditionals, data transformations, and error handling are all explicit in code rather than implicit in Claude's reasoning.
Claude 擅长编写代码，通过让它用 Python 而不是自然语言工具调用来表达编排逻辑，你会得到更可靠、精确的控制流。循环、条件语句、数据转换和错误处理都在代码中显式，而不是在 Claude 的推理中隐式。

#### Example: Budget Compliance Check
示例：预算合规检查

Consider a common business task: "Which team members exceeded their Q3 travel budget?"
考虑一个常见的业务任务："哪些团队成员超过了他们的第三季度差旅预算？"

You have three tools available:
你有三个可用的工具：

- `get_team_members(department)` - Returns team member list with IDs and levels
- `get_expenses(user_id, quarter)` - Returns expense line items for a user
- `get_budget_by_level(level)` - Returns budget limits for an employee level

__Traditional approach:__
__传统方法：__

- Fetch team members → 20 people
- 获取团队成员 → 20 人
- For each person, fetch their Q3 expenses → 20 tool calls, each returning 50-100 line items (flights, hotels, meals, receipts)
- 对于每个人，获取其第三季度费用 → 20 次工具调用，每次返回 50-100 个行项目（航班、酒店、餐饮、收据）
- Fetch budget limits by employee level
- 按员工级别获取预算限制
- All of this enters Claude's context: 2,000+ expense line items (50 KB+)
- 所有这些都进入 Claude 的上下文：2,000+ 费用行项目（50 KB+）
- Claude manually sums each person's expenses, looks up their budget, compares expenses against budget limits
- Claude 手动汇总每个人的费用，查找他们的预算，将费用与预算限制进行比较
- More round-trips to the model, significant context consumption
- 更多的模型往返，大量的上下文消耗

__With Programmatic Tool Calling:__
__使用编程式工具调用：__

Instead of each tool result returning to Claude, Claude writes a Python script that orchestrates the entire workflow. The script runs in the Code Execution tool (a sandboxed environment), pausing when it needs results from your tools. When you return tool results via the API, they're processed by the script rather than consumed by the model. The script continues executing, and Claude only sees the final output.
Claude 编写一个编排整个工作流程的 Python 脚本，而不是每个工具结果返回给 Claude。该脚本在代码执行工具（沙盒环境）中运行，在需要工具结果时暂停。当你通过 API 返回工具结果时，它们由脚本处理，而不是由模型消耗。脚本继续执行，Claude 只看到最终输出。

![Image 2: Programmatic tool calling flow](https://example.com/_next/image?url=https%3A%2F%2Fwww-cdn.anthropic.com%2Fimages%2F4zrzovbb%2Fwebsite%2F65737d69a3290ed5c1f3c3b8dc873645a9dcc2eb-1999x1491.png&w=3840&q=75)

Programmatic Tool Calling enables Claude to orchestrate tools through code rather than through individual API round-trips, allowing for parallel tool execution.
编程式工具调用使 Claude 能够通过代码而不是通过单独的 API 往返来编排工具，从而实现并行工具执行。

Here's what Claude's orchestration code looks like for the budget compliance task:
以下是 Claude 用于预算合规任务的编排代码：

```python
team = await get_team_members("engineering")

# Fetch budgets for each unique level
levels = list(set(m["level"] for m in team))
budget_results = await asyncio.gather(*[
    get_budget_by_level(level) for level in levels
])

# Create a lookup dictionary: {"junior": budget1, "senior": budget2, ...}
budgets = {level: budget for level, budget in zip(levels, budget_results)}

# Fetch all expenses in parallel
expenses = await asyncio.gather(*[
    get_expenses(m["id"], "Q3") for m in team
])

# Find employees who exceeded their travel budget
exceeded = []
for member, exp in zip(team, expenses):
    budget = budgets[member["level"]]
    total = sum(e["amount"] for e in exp)
    if total > budget["travel_limit"]:
        exceeded.append({
            "name": member["name"],
            "spent": total,
            "limit": budget["travel_limit"]
        })

print(json.dumps(exceeded))
```

Claude's context receives only the final result: the two to three people who exceeded their budget. The 2,000+ line items, the intermediate sums, and the budget lookups do not affect Claude's context, reducing consumption from 200KB of raw expense data to just 1KB of results.
Claude 的上下文只接收最终结果：超出预算的两三个人。2,000+ 行项目、中间汇总和预算查找不会影响 Claude 的上下文，将从 200KB 的原始费用数据减少到仅 1KB 的结果。

The efficiency gains are substantial:
效率收益是巨大的：

- __Token savings__: By keeping intermediate results out of Claude's context, PTC dramatically reduces token consumption. Average usage dropped from 43,588 to 27,297 tokens, a 37% reduction on complex research tasks.
- __令牌节省：__ 通过将中间结果排除在 Claude 的上下文之外，PTC 显著减少了令牌消耗。平均使用量从 43,588 个令牌下降到 27,297 个令牌，在复杂研究任务上减少了 37%。

- __Reduced latency__: Each API round-trip requires model inference (hundreds of milliseconds to seconds). When Claude orchestrates 20+ tool calls in a single code block, you eliminate 19+ inference passes. The API handles tool execution without returning to the model each time.
- __降低延迟：__ 每次 API 往返都需要模型推理（几百毫秒到几秒）。当 Claude 在单个代码块中编排 20+ 个工具调用时，你消除了 19+ 次推理过程。API 处理工具执行，而无需每次都返回模型。

- __Improved accuracy__: By writing explicit orchestration logic, Claude makes fewer errors than when juggling multiple tool results in natural language. Internal knowledge retrieval improved from 25.6% to 28.5%; GIA benchmarks from 46.5% to 51.2%.
- __提高准确性：__ 通过编写显式的编排逻辑，Claude 比在自然语言中处理多个工具结果时犯的错误更少。内部知识检索从 25.6% 提高到 28.5%；GIA 基准测试从 46.5% 提高到 51.2%。

Production workflows involve messy data, conditional logic, and operations that need to scale. Programmatic Tool Calling lets Claude handle that complexity programmatically while keeping its focus on actionable results rather than raw data processing.
生产工作流程涉及杂乱的数据、条件逻辑和需要扩展的操作。编程式工具调用让 Claude 能够以编程方式处理这些复杂性，同时将其重点放在可操作的结果上，而不是原始数据处理。

### How Programmatic Tool Calling Works
编程式工具调用的工作原理

#### 1. Mark tools as callable from code
#### 1. 将工具标记为可从代码调用

Add code_execution to tools, and set allowed_callers to opt-in tools for programmatic execution:
将 code_execution 添加到工具，并设置 allowed_callers 以选择加入编程执行的工具：

```json
{
  "tools": [
    {
      "type": "code_execution_20250825",
      "name": "code_execution"
    },
    {
      "name": "get_team_members",
      "description": "Get all members of a department...",
      "input_schema": {...},
      "allowed_callers": ["code_execution_20250825"] # opt-in to programmatic tool calling
    },
    {
      "name": "get_expenses",
      ...
    },
    {
      "name": "get_budget_by_level",
      ...
    }
  ]
}
```

The API converts these tool definitions into Python functions that Claude can call.
API 将这些工具定义转换为 Claude 可以调用的 Python 函数。

#### 2. Claude writes orchestration code
#### 2. Claude 编写编排代码

Instead of requesting tools one at a time, Claude generates Python code:
Claude 生成 Python 代码，而不是一次请求一个工具：

```json
{
  "type": "server_tool_use",
  "id": "srvtoolu_abc",
  "name": "code_execution",
  "input": {
    "code": "team = get_team_members('engineering')\n..." # the code example above
  }
}
```

#### 3. Tools execute without hitting Claude's context
#### 3. 工具执行而不影响 Claude 的上下文

When the code calls get_expenses(), you receive a tool request with a caller field:
当代码调用 get_expenses() 时，你会收到一个带有 caller 字段的工具请求：

```json
{
  "type": "tool_use",
  "id": "toolu_xyz",
  "name": "get_expenses",
  "input": {"user_id": "emp_123", "quarter": "Q3"},
  "caller": {
    "type": "code_execution_20250825",
    "tool_id": "srvtoolu_abc"
  }
}
```

You provide the result, which is processed in the Code Execution environment rather than Claude's context. This request-response cycle repeats for each tool call in the code.
你提供的结果在代码执行环境中处理，而不是在 Claude 的上下文中。这个请求-响应周期对代码中的每个工具调用重复。

#### 4. Only final output enters context
#### 4. 只有最终输出进入上下文

When the code finishes running, only the results of the code are returned to Claude:
当代码完成运行时，只有代码的结果返回给 Claude：

```json
{
  "type": "code_execution_tool_result",
  "tool_use_id": "srvtoolu_abc",
  "content": {
    "stdout": "[{\"name\": \"Alice\", \"spent\": 12500, \"limit\": 10000}...]"
  }
}
```

This is all Claude sees, not the 2000+ expense line items processed along the way.
这就是 Claude 看到的全部内容，而不是沿途处理的 2000+ 费用行项目。

### When to Use Programmatic Tool Calling
何时使用编程式工具调用

Programmatic Tool Calling adds a code execution step to your workflow. This extra overhead pays off when the token savings, latency improvements, and accuracy gains are substantial.
编程式工具调用为你的工作流程添加了一个代码执行步骤。当令牌节省、延迟改进和准确性提高很大时，这个额外开销是值得的。

__Most beneficial when:__
__最有益时：__

- Processing large datasets where you only need aggregates or summaries
- 处理大型数据集，只需要聚合或摘要
- Running multi-step workflows with three or more dependent tool calls
- 运行具有三个或更多依赖工具调用的多步骤工作流程
- Filtering, sorting, or transforming tool results before Claude sees them
- 在 Claude 看到之前过滤、排序或转换工具结果
- Handling tasks where intermediate data shouldn't influence Claude's reasoning
- 处理中间数据不应影响 Claude 推理的任务
- Running parallel operations across many items (checking 50 endpoints, for example)
- 跨许多项目运行并行操作（例如，检查 50 个端点）

__Less beneficial when:__
__不太有益时：__

- Making simple single-tool invocations
- 进行简单的单工具调用
- Working on tasks where Claude should see and reason about all intermediate results
- 在 Claude 应该看到并推理所有中间结果的任务上工作
- Running quick lookups with small responses
- 运行具有小响应的快速查找

## Tool Use Examples
工具使用示例

### The Challenge
挑战

JSON Schema excels at defining structure–types, required fields, allowed enums–but it can't express usage patterns: when to include optional parameters, which combinations make sense, or what conventions your API expects.
JSON 模式擅长定义结构——类型、必填字段、允许的枚举——但它无法表达使用模式：何时包含可选参数，哪些组合有意义，或者你的 API 期望什么约定。

Consider a support ticket API:
考虑一个支持工单 API：

```json
{
  "name": "create_ticket",
  "input_schema": {
    "properties": {
      "title": {"type": "string"},
      "priority": {"enum": ["low", "medium", "high", "critical"]},
      "labels": {"type": "array", "items": {"type": "string"}},
      "reporter": {
        "type": "object",
        "properties": {
          "id": {"type": "string"},
          "name": {"type": "string"},
          "contact": {
            "type": "object",
            "properties": {
              "email": {"type": "string"},
              "phone": {"type": "string"}
            }
          }
        }
      },
      "due_date": {"type": "string"},
      "escalation": {
        "type": "object",
        "properties": {
          "level": {"type": "integer"},
          "notify_manager": {"type": "boolean"},
          "sla_hours": {"type": "integer"}
        }
      }
    },
    "required": ["title"]
  }
}
```

The schema defines what's valid, but leaves critical questions unanswered:
模式定义了什么是有效的，但没有回答关键问题：

- __Format ambiguity:__ Should `due_date` use "2024-11-06", "Nov 6, 2024", or "2024-11-06T00:00:00Z"?
- __格式模糊：__ `due_date` 应该使用 "2024-11-06"、"Nov 6, 2024" 还是 "2024-11-06T00:00:00Z"？
- __ID conventions:__ Is `reporter.id` a UUID, "USR-12345", or just "12345"?
- __ID 约定：__ `reporter.id` 是 UUID、"USR-12345" 还是 "12345"？
- __Nested structure usage:__ When should Claude populate `reporter.contact`?
- __嵌套结构使用：__ Claude 应该何时填充 `reporter.contact`？
- __Parameter correlations:__ How do `escalation.level` and `escalation.sla_hours` relate to priority?
- **参数相关性：** `escalation.level` 和 `escalation.sla_hours` 与优先级有何关系？

These ambiguities can lead to malformed tool calls and inconsistent parameter usage.
这些模糊性可能导致格式错误的工具调用和不一致的参数使用。

### Our Solution
我们的解决方案

Tool Use Examples let you provide sample tool calls directly in your tool definitions. Instead of relying on schema alone, you show Claude concrete usage patterns:
工具使用示例允许你直接在工具定义中提供示例工具调用。你不是单独依赖模式，而是向 Claude 展示具体的用法模式：

```json
{
    "name": "create_ticket",
    "input_schema": { /* same schema as above */ },
    "input_examples": [
      {
        "title": "Login page returns 500 error",
        "priority": "critical",
        "labels": ["bug", "authentication", "production"],
        "reporter": {
          "id": "USR-12345",
          "name": "Jane Smith",
          "contact": {
            "email": "jane@acme.com",
            "phone": "+1-555-0123"
          }
        },
        "due_date": "2024-11-06",
        "escalation": {
          "level": 2,
          "notify_manager": true,
          "sla_hours": 4
        }
      },
      {
        "title": "Add dark mode support",
        "labels": ["feature-request", "ui"],
        "reporter": {
          "id": "USR-67890",
          "name": "Alex Chen"
        }
      },
      {
        "title": "Update API documentation"
      }
    ]
  }
```

From these three examples, Claude learns:
从这三个示例中，Claude 学到了：

- __Format conventions__: Dates use YYYY-MM-DD, user IDs follow USR-XXXXX, labels use kebab-case
- __格式约定：__ 日期使用 YYYY-MM-DD，用户 ID 遵循 USR-XXXXX，标签使用 kebab-case
- __Nested structure patterns__: How to construct the reporter object with its nested contact object
- __嵌套结构模式：** 如何构造带有嵌套联系人对象的报告者对象
- __Optional parameter correlations__: Critical bugs have full contact info + escalation with tight SLAs; feature requests have reporter but no contact/escalation; internal tasks have title only
- **可选参数相关性：** 关键错误具有完整的联系信息 + 升级以及严格的 SLA；功能请求有报告者但没有联系人/升级；内部任务只有标题

In our own internal testing, tool use examples improved accuracy from 72% to 90% on complex parameter handling.
在我们自己的内部测试中，工具使用示例在复杂参数处理上的准确性从 72% 提高到 90%。

### When to Use Tool Use Examples
何时使用工具使用示例

Tool Use Examples add tokens to your tool definitions, so they're most valuable when accuracy improvements outweigh the additional cost.
工具使用示例为你的工具定义添加令牌，因此当准确性提高超过额外成本时，它们最有价值。

__Most beneficial when:__
__最有益时：__

- Complex nested structures where valid JSON doesn't imply correct usage
- 复杂的嵌套结构，其中有效的 JSON 并不意味着正确的使用
- Tools with many optional parameters and inclusion patterns matter
- 具有许多可选参数且包含模式很重要的工具
- APIs with domain-specific conventions not captured in schemas
- 具有模式未捕获的领域特定约定的 API
- Similar tools where examples clarify which one to use (e.g., `create_ticket` vs. `create_incident`)
- 相似的工具，其中示例阐明了使用哪一个（例如，`create_ticket` 与 `create_incident`）

__Less beneficial when:__
__不太有益时：__

- Simple single-parameter tools with obvious usage
- 具有明显用法的简单单参数工具
- Standard formats like URLs or emails that Claude already understands
- Claude 已经理解的标准格式，如 URL 或电子邮件
- Validation concerns better handled by JSON Schema constraints
- 最好由 JSON 模式约束处理的验证问题

## Best Practices
最佳实践

Building agents that take real-world actions means handling scale, complexity, and precision simultaneously. These three features work together to solve different bottlenecks in tool use workflows. Here's how to combine them effectively.
构建在现实世界中采取行动的智能体意味着同时处理规模、复杂性和精度。这三个功能协同工作，解决了工具使用工作流程中的不同瓶颈。以下是如何有效地组合它们。

### Layer Features Strategically
战略性分层功能

Not every agent needs to use all three features for a given task. Start with your biggest bottleneck:
并非每个智能体都需要针对给定任务使用所有三个功能。从你最大的瓶颈开始：

- Context bloat from tool definitions → Tool Search Tool
- 来自工具定义的上下文膨胀 → 工具搜索工具
- Large intermediate results polluting context → Programmatic Tool Calling
- 污染上下文的大型中间结果 → 编程式工具调用
- Parameter errors and malformed calls → Tool Use Examples
- 参数错误和格式错误的调用 → 工具使用示例

This focused approach lets you address the specific constraint limiting your agent's performance, rather than adding complexity upfront.
这种专注的方法让你解决限制智能体性能的特定约束，而不是预先增加复杂性。

Then layer additional features as needed. They're complementary: Tool Search Tool ensures the right tools are found, Programmatic Tool Calling ensures efficient execution, and Tool Use Examples ensure correct invocation.
然后根据需要分层附加功能。它们是互补的：工具搜索工具确保找到正确的工具，编程式工具调用确保高效执行，工具使用示例确保正确调用。

### Set Up Tool Search Tool for Better Discovery
设置工具搜索工具以更好地发现

Tool search matches against names and descriptions, so clear, descriptive definitions improve discovery accuracy.
工具搜索匹配名称和描述，因此清晰、描述性的定义提高了发现准确性。

```javascript
// Good
{
    "name": "search_customer_orders",
    "description": "Search for customer orders by date range, status, or total amount. Returns order details including items, shipping, and payment info."
}

// Bad
{
    "name": "query_db_orders",
    "description": "Execute order query"
}
```

Add system prompt guidance so Claude knows what's available:
添加系统提示指导，以便 Claude 知道可用什么：

```text
You have access to tools for Slack messaging, Google Drive file management,
Jira ticket tracking, and GitHub repository operations. Use the tool search
to find specific capabilities.
```

Keep your three to five most-used tools always loaded, defer the rest. This balances immediate access for common operations with on-demand discovery for everything else.
保持你的三到五个最常用的工具始终加载，其余的延迟。这平衡了常见操作的即时访问与其他所有内容的按需发现。

### Set Up Programmatic Tool Calling for Correct Execution
设置编程式工具调用以正确执行

Since Claude writes code to parse tool outputs, document return formats clearly. This helps Claude write correct parsing logic:
由于 Claude 编写代码来解析工具输出，因此清楚地记录返回格式。这有助于 Claude 编写正确的解析逻辑：

```json
{
    "name": "get_orders",
    "description": "Retrieve orders for a customer.
Returns:
    List of order objects, each containing:
    - id (str): Order identifier
    - total (float): Order total in USD
    - status (str): One of 'pending', 'shipped', 'delivered'
    - items (list): Array of {sku, quantity, price}
    - created_at (str): ISO 8601 timestamp"
}
```

See below for opt-in tools that benefit from programmatic orchestration:
以下是受益于编程编排的选择加入工具：

- Tools that can run in parallel (independent operations)
- 可以并行运行的工具（独立操作）
- Operations safe to retry (idempotent)
- 可以安全重试的操作（幂等）

### Set Up Tool Use Examples for Parameter Accuracy
设置工具使用示例以提高参数准确性

Craft examples for behavioral clarity:
为行为清晰度制作示例：

- Use realistic data (real city names, plausible prices, not "string" or "value")
- 使用真实数据（真实城市名称、合理价格，而不是"string"或"value"）
- Show variety with minimal, partial, and full specification patterns
- 显示最小、部分和完整规范模式的多样性
- Keep it concise: 1-5 examples per tool
- 保持简洁：每个工具 1-5 个示例
- Focus on ambiguity (only add examples where correct usage isn't obvious from schema)
- 专注于模糊性（仅在模式中不清楚正确用法的地方添加示例）

## Getting Started
入门

These features are available in beta. To enable them, add the beta header and include the tools you need:
这些功能在测试版中可用。要启用它们，添加测试版标头并包含你需要的工具：

```python
client.beta.messages.create(
    betas=["advanced-tool-use-2025-11-20"],
    model="claude-sonnet-4-5-20250929",
    max_tokens=4096,
    tools=[
        {"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"},
        {"type": "code_execution_20250825", "name": "code_execution"},
        # Your tools with defer_loading, allowed_callers, and input_examples
    ]
)
```

For detailed API documentation and SDK examples, see our:
有关详细的 API 文档和 SDK 示例，请参阅我们的：

- Documentation and cookbook for Tool Search Tool
- 工具搜索工具的文档和手册
- Documentation and cookbook for Programmatic Tool Calling
- 编程式工具调用的文档和手册
- Documentation for Tool Use Examples
- 工具使用示例的文档

These features move tool use from simple function calling toward intelligent orchestration. As agents tackle more complex workflows spanning dozens of tools and large datasets, dynamic discovery, efficient execution, and reliable invocation become foundational.
这些功能将工具使用从简单的函数调用转向智能编排。随着智能体处理跨越数十个工具和大型数据集的更复杂工作流程，动态发现、高效执行和可靠调用变得基础。

We're excited to see what you build.
我们很期待看到你构建的东西。

## Acknowledgements
致谢

Written by Bin Wu, with contributions from Adam Jones, Artur Renault, Henry Tay, Jake Noble, Nathan McCandlish, Noah Picard, Sam Jiang, and the Claude Developer Platform team. This work builds on foundational research by Chris Gorgolewski, Daniel Jiang, Jeremy Fox and Mike Lambert. We also drew inspiration from across the AI ecosystem, including Joel Pobar's LLMVM, Cloudflare's Code Mode and Code Execution as MCP. Special thanks to Andy Schumeister, Hamish Kerr, Keir Bradwell, Matt Bleifer and Molly Vorwerck for their support.
本文由 Bin Wu 撰写，Adam Jones、Artur Renault、Henry Tay、Jake Noble、Nathan McCandlish、Noah Picard、Sam Jiang 和 Claude 开发者平台团队做出了贡献。这项工作建立在 Chris Gorgolewski、Daniel Jiang、Jeremy Fox 和 Mike Lambert 的基础研究之上。我们还从整个 AI 生态系统中汲取了灵感，包括 Joel Pobar 的 LLMVM、Cloudflare 的代码模式和作为 MCP 的代码执行。特别感谢 Andy Schumeister、Hamish Kerr、Keir Bradwell、Matt Bleifer 和 Molly Vorwerck 的支持。
