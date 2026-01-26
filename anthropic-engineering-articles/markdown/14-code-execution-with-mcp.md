# Code Execution with MCP: Building More Efficient AI Agents | 使用 MCP 执行代码：构建更高效的 AI 智能体

The Model Context Protocol (MCP) is an open standard for connecting AI agents to external systems. Connecting agents to tools and data traditionally requires a custom integration for each pairing, creating fragmentation and duplicated effort that makes it difficult to scale truly connected systems. MCP provides a universal protocol—developers implement MCP once in their agent and it unlocks an entire ecosystem of integrations.

模型上下文协议（MCP）是连接 AI 智能体与外部系统的开放标准。传统上，将智能体连接到工具和数据需要为每个配对进行自定义集成，这导致碎片化和重复工作，使真正连接系统的扩展变得困难。MCP 提供了一个通用协议——开发者在智能体中实现一次 MCP，就能解锁整个集成生态系统。

Since launching MCP in November 2024, adoption has been rapid: the community has built thousands of MCP servers, SDKs are available for all major programming languages, and the industry has adopted MCP as the de-facto standard for connecting agents to tools and data. You can learn more at [modelcontextprotocol.io](https://modelcontextprotocol.io/).

自 2024 年 11 月推出 MCP 以来，采用速度很快：社区已经构建了数千个 MCP 服务器，所有主要编程语言都有可用的 SDK，业界已采用 MCP 作为连接智能体与工具和数据的事实标准。你可以在 [modelcontextprotocol.io](https://modelcontextprotocol.io/) 了解更多信息。

Today developers routinely build agents with access to hundreds or thousands of tools across dozens of MCP servers. However, as the number of connected tools grows, loading all tool definitions upfront and passing intermediate results through the context window slows down agents and increases costs.

如今，开发者经常构建具有数百或数千个工具访问权限的智能体，这些工具分布在数十个 MCP 服务器上。然而，随着连接工具数量的增加，预先加载所有工具定义并通过上下文窗口传递中间结果会减慢智能体速度并增加成本。

In this blog we'll explore how code execution can enable agents to interact with MCP servers more efficiently, handling more tools while using fewer tokens.

在本博客中，我们将探讨代码执行如何使智能体更高效地与 MCP 服务器交互，在使用更少令牌的同时处理更多工具。

## Excessive Token Consumption from Tools Makes Agents Less Efficient | 工具过度消耗令牌使智能体效率降低

As MCP usage scales, there are two common patterns that can increase agent cost and latency:

随着 MCP 使用的扩展，有两种常见模式可能会增加智能体的成本和延迟：

1. Tool definitions overload the context window;
2. Intermediate tool results consume additional tokens.

工具定义过载上下文窗口；
中间工具结果消耗额外令牌。

### 1. Tool Definitions Overload the Context Window | 工具定义过载上下文窗口

Most MCP clients load all tool definitions upfront directly into context, exposing them to the model using a direct tool-calling syntax. These tool definitions might look like:

大多数 MCP 客户端预先将所有工具定义直接加载到上下文中，使用直接工具调用语法将它们暴露给模型。这些工具定义可能如下所示：

```
gdrive.getDocument
     Description: Retrieves a document from Google Drive
     Parameters:
                documentId (required, string): The ID of the document to retrieve
                fields (optional, string): Specific fields to return
     Returns: Document object with title, body content, metadata, permissions, etc.
```

```
salesforce.updateRecord
    Description: Updates a record in Salesforce
    Parameters:
               objectType (required, string): Type of Salesforce object (Lead, Contact,      Account, etc.)
               recordId (required, string): The ID of the record to update
               data (required, object): Fields to update with their new values
     Returns: Updated record object with confirmation
```

Tool descriptions occupy more context window space, increasing response time and costs. In cases where agents are connected to thousands of tools, they'll need to process hundreds of thousands of tokens before reading a request.

工具描述占用更多上下文窗口空间，增加响应时间和成本。在智能体连接到数千个工具的情况下，它们需要处理数十万个令牌才能读取请求。

### 2. Intermediate Tool Results Consume Additional Tokens | 中间工具结果消耗额外令牌

Most MCP clients allow models to directly call MCP tools. For example, you might ask your agent: "Download my meeting transcript from Google Drive and attach it to the Salesforce lead."

大多数 MCP 客户端允许模型直接调用 MCP 工具。例如，你可能会问你的智能体："从 Google Drive 下载我的会议记录并将其附加到 Salesforce 潜在客户。"

The model will make calls like:

模型将进行如下调用：

```
TOOL CALL: gdrive.getDocument(documentId: "abc123")
        → returns "Discussed Q4 goals...\n[full transcript text]"
           (loaded into model context)

TOOL CALL: salesforce.updateRecord(
				objectType: "SalesMeeting",
				recordId: "00Q5f000001abcXYZ",
  			data: { "Notes": "Discussed Q4 goals...\n[full transcript text written out]" }
			)
			(model needs to write entire transcript into context again)
```

Every intermediate result must pass through the model. In this example, the full call transcript flows through twice. For a 2-hour sales meeting, that could mean processing an additional 50,000 tokens. Even larger documents may exceed context window limits, breaking the workflow.

每个中间结果都必须通过模型。在此示例中，完整的通话记录流经两次。对于 2 小时的销售会议，这可能意味着处理额外的 50,000 个令牌。更大的文档可能会超过上下文窗口限制，破坏工作流程。

With large documents or complex data structures, models may be more likely to make mistakes when copying data between tool calls.

对于大型文档或复杂数据结构，模型在工具调用之间复制数据时可能更容易出错。

![Image 1: Image of how the MCP client works with the MCP server and LLM.](https://www-cdn.anthropic.com/images/4zrzovbb/website/9ecf165020005c09a22a9472cee6309555485619-1920x1080.png)

The MCP client loads tool definitions into the model's context window and orchestrates a message loop where each tool call and result passes through the model between operations.

MCP 客户端将工具定义加载到模型的上下文窗口中，并编排消息循环，其中每个工具调用和结果在操作之间通过模型。

## Code Execution with MCP Improves Context Efficiency | 使用 MCP 执行代码提高上下文效率

With code execution environments becoming more common for agents, a solution is to present MCP servers as code APIs rather than direct tool calls. The agent can then write code to interact with MCP servers. This approach addresses both challenges: agents can load only the tools they need and process data in the execution environment before passing results back to the model.

随着代码执行环境在智能体中变得越来越普遍，一种解决方案是将 MCP 服务器呈现为代码 API 而不是直接工具调用。然后，智能体可以编写代码与 MCP 服务器交互。这种方法解决了两个挑战：智能体只能加载其需要的工具，并在执行环境中处理数据，然后将结果传递回模型。

There are a number of ways to do this. One approach is to generate a file tree of all available tools from connected MCP servers. Here's an implementation using TypeScript:

有多种方法可以做到这一点。一种方法是生成连接的 MCP 服务器的所有可用工具的文件树。以下是使用 TypeScript 的实现：

```
servers
├── google-drive
│   ├── getDocument.ts
│   ├── ... (other tools)
│   └── index.ts
├── salesforce
│   ├── updateRecord.ts
│   ├── ... (other tools)
│   └── index.ts
└── ... (other servers)
```

Then each tool corresponds to a file, something like:

然后，每个工具对应一个文件，类似于：

```typescript
// ./servers/google-drive/getDocument.ts
import { callMCPTool } from "../../../client.js";

interface GetDocumentInput {
  documentId: string;
}

interface GetDocumentResponse {
  content: string;
}

/* Read a document from Google Drive */
export async function getDocument(input: GetDocumentInput): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>('google_drive__get_document', input);
}
```

Our Google Drive to Salesforce example above becomes the code:

我们上面的 Google Drive 到 Salesforce 示例变成了代码：

```typescript
// Read transcript from Google Docs and add to Salesforce prospect
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

const transcript = (await gdrive.getDocument({ documentId: 'abc123' })).content;
await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

The agent discovers tools by exploring the filesystem: listing the `./servers/` directory to find available servers (like `google-drive` and `salesforce`), then reading the specific tool files it needs (like `getDocument.ts` and `updateRecord.ts`) to understand each tool's interface. This lets the agent load only the definitions it needs for the current task. This reduces the token usage from 150,000 tokens to 2,000 tokens—a time and cost saving of 98.7%.

智能体通过探索文件系统来发现工具：列出 `./servers/` 目录以查找可用的服务器（如 `google-drive` 和 `salesforce`），然后读取其需要的特定工具文件（如 `getDocument.ts` 和 `updateRecord.ts`）以了解每个工具的接口。这使得智能体只能加载当前任务所需的定义。这将令牌使用量从 150,000 个令牌减少到 2,000 个令牌——节省了 98.7% 的时间和成本。

Cloudflare published similar findings, referring to code execution with MCP as "Code Mode." The core insight is the same: LLMs are adept at writing code and developers should take advantage of this strength to build agents that interact with MCP servers more efficiently.

Cloudflare 发布了类似的发现，将使用 MCP 执行代码称为"代码模式"。核心洞察是相同的：LLM 擅长编写代码，开发者应该利用这一优势来构建更高效地与 MCP 服务器交互的智能体。

## Benefits of Code Execution with MCP | 使用 MCP 执行代码的好处

Code execution with MCP enables agents to use context more efficiently by loading tools on demand, filtering data before it reaches the model, and executing complex logic in a single step. There are also security and state management benefits to using this approach.

使用 MCP 执行代码使智能体能够通过按需加载工具、在数据到达模型之前过滤数据以及单步执行复杂逻辑来更高效地使用上下文。使用这种方法还有安全性和状态管理的好处。

### Progressive Disclosure | 渐进式披露

Models are great at navigating filesystems. Presenting tools as code on a filesystem allows models to read tool definitions on-demand, rather than reading them all up-front.

模型非常擅长导航文件系统。将工具作为文件系统上的代码呈现，使模型能够按需读取工具定义，而不是预先读取所有定义。

Alternatively, a `search_tools` tool can be added to the server to find relevant definitions. For example, when working with the hypothetical Salesforce server used above, the agent searches for "salesforce" and loads only those tools that it needs for the current task. Including a detail level parameter in the `search_tools` tool that allows the agent to select the level of detail required (such as name only, name and description, or the full definition with schemas) also helps the agent conserve context and find tools efficiently.

或者，可以将 `search_tools` 工具添加到服务器以查找相关定义。例如，当使用上面使用的假设 Salesforce 服务器时，智能体搜索"salesforce"并仅加载当前任务需要的那些工具。在 `search_tools` 工具中包含一个详细信息级别参数，允许智能体选择所需的详细信息级别（例如仅名称、名称和描述，或带有模式的完整定义），也有助于智能体节省上下文并高效查找工具。

### Context Efficient Tool Results | 上下文高效的工具结果

When working with large datasets, agents can filter and transform results in code before returning them. Consider fetching a 10,000-row spreadsheet:

在使用大型数据集时，智能体可以在返回结果之前在代码中过滤和转换结果。考虑获取 10,000 行的电子表格：

```typescript
// Without code execution - all rows flow through context
TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
        → returns 10,000 rows in context to filter manually

// With code execution - filter in the execution environment
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(row =>
  row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // Only log first 5 for review
```

The agent sees five rows instead of 10,000. Similar patterns work for aggregations, joins across multiple data sources, or extracting specific fields—all without bloating the context window.

智能体看到五行而不是 10,000 行。类似的模式适用于聚合、跨多个数据源的联接或提取特定字段——所有这些都不会膨胀上下文窗口。

#### More Powerful and Context-Efficient Control Flow | 更强大且上下文高效的控制流

Loops, conditionals, and error handling can be done with familiar code patterns rather than chaining individual tool calls. For example, if you need a deployment notification in Slack, the agent can write:

循环、条件和错误处理可以使用熟悉的代码模式来完成，而不是链接单个工具调用。例如，如果你需要 Slack 中的部署通知，智能体可以编写：

```typescript
let found = false;
while (!found) {
  const messages = await slack.getChannelHistory({ channel: 'C123456' });
  found = messages.some(m => m.text.includes('deployment complete'));
  if (!found) await new Promise(r => setTimeout(r, 5000));
}
console.log('Deployment notification received');
```

This approach is more efficient than alternating between MCP tool calls and sleep commands through the agent loop.

这种方法比通过智能体循环在 MCP 工具调用和休眠命令之间交替更高效。

Additionally, being able to write out a conditional tree that gets executed also saves on "time to first token" latency: rather than having to wait for a model to evaluate an if-statement, the agent can let the code execution environment do this.

此外，能够写出被执行的条件树也节省了"首令牌时间"延迟：智能体可以让代码执行环境来评估 if 语句，而不必等待模型来评估。

### Privacy-Preserving Operations | 隐私保护操作

When agents use code execution with MCP, intermediate results stay in the execution environment by default. This way, the agent only sees what you explicitly log or return, meaning data you don't wish to share with the model can flow through your workflow without ever entering the model's context.

当智能体使用 MCP 执行代码时，中间结果默认保留在执行环境中。这样，智能体只能看到你明确记录或返回的内容，这意味着你不希望与模型共享的数据可以流经你的工作流程，而无需进入模型的上下文。

For even more sensitive workloads, the agent harness can tokenize sensitive data automatically. For example, imagine you need to import customer contact details from a spreadsheet into Salesforce. The agent writes:

对于更敏感的工作负载，智能体工具可以自动标记敏感数据。例如，假设你需要将客户联系详细信息从电子表格导入 Salesforce。智能体编写：

```typescript
const sheet = await gdrive.getSheet({ sheetId: 'abc123' });
for (const row of sheet.rows) {
  await salesforce.updateRecord({
    objectType: 'Lead',
    recordId: row.salesforceId,
    data: {
      Email: row.email,
      Phone: row.phone,
      Name: row.name
    }
  });
}
console.log(`Updated ${sheet.rows.length} leads`);
```

The MCP client intercepts the data and tokenizes PII before it reaches the model:

MCP 客户端在数据到达模型之前拦截数据并标记 PII：

```typescript
// What the agent would see, if it logged the sheet.rows:
[
  { salesforceId: '00Q...', email: '[EMAIL_1]', phone: '[PHONE_1]', name: '[NAME_1]' },
  { salesforceId: '00Q...', email: '[EMAIL_2]', phone: '[PHONE_2]', name: '[NAME_2]' },
  ...
]
```

Then, when the data is shared in another MCP tool call, it is untokenized via a lookup in the MCP client. The real email addresses, phone numbers, and names flow from Google Sheets to Salesforce, but never through the model. This prevents the agent from accidentally logging or processing sensitive data. You can also use this to define deterministic security rules, choosing where data can flow to and from.

然后，当数据在另一个 MCP 工具调用中共享时，它通过 MCP 客户端中的查找进行非标记化。真实的电子邮件地址、电话号码和名称从 Google Sheets 流向 Salesforce，但从不通过模型。这可以防止智能体意外记录或处理敏感数据。你也可以使用它来定义确定性安全规则，选择数据可以流入和流出的位置。

### State Persistence and Skills | 状态持久化和技能

Code execution with filesystem access allows agents to maintain state across operations. Agents can write intermediate results to files, enabling them to resume work and track progress:

具有文件系统访问权限的代码执行允许智能体在操作之间保持状态。智能体可以将中间结果写入文件，使它们能够恢复工作并跟踪进度：

```typescript
const leads = await salesforce.query({
  query: 'SELECT Id, Email FROM Lead LIMIT 1000'
});
const csvData = leads.map(l => `${l.Id},${l.Email}`).join('\n');
await fs.writeFile('./workspace/leads.csv', csvData);

// Later execution picks up where it left off
const saved = await fs.readFile('./workspace/leads.csv', 'utf-8');
```

Agents can also persist their own code as reusable functions. Once an agent develops working code for a task, it can save that implementation for future use:

智能体还可以将自己的代码持久化为可重用函数。一旦智能体为任务开发了工作代码，它就可以保存该实现以供将来使用：

```typescript
// In ./skills/save-sheet-as-csv.ts
import * as gdrive from './servers/google-drive';
export async function saveSheetAsCsv(sheetId: string) {
  const data = await gdrive.getSheet({ sheetId });
  const csv = data.map(row => row.join(',')).join('\n');
  await fs.writeFile(`./workspace/sheet-${sheetId}.csv`, csv);
  return `./workspace/sheet-${sheetId}.csv`;
}

// Later, in any agent execution:
import { saveSheetAsCsv } from './skills/save-sheet-as-csv';
const csvPath = await saveSheetAsCsv('abc123');
```

This ties in closely to the concept of Skills, folders of reusable instructions, scripts, and resources for models to improve performance on specialized tasks. Adding a SKILL.md file to these saved functions creates a structured skill that models can reference and use. Over time, this allows your agent to build a toolbox of higher-level capabilities, evolving the scaffolding that it needs to work most effectively.

这与技能的概念密切相关，技能是可重用指令、脚本和资源的文件夹，用于模型在专门任务上提高性能。将 SKILL.md 文件添加到这些保存的函数中会创建一个结构化技能，模型可以引用和使用。随着时间的推移，这允许你的智能体构建更高级别能力的工具箱，演进其最有效工作所需的脚手架。

Note that code execution introduces its own complexity. Running agent-generated code requires a secure execution environment with appropriate sandboxing, resource limits, and monitoring. These infrastructure requirements add operational overhead and security considerations that direct tool calls avoid. The benefits of code execution—reduced token costs, lower latency, and improved tool composition—should be weighed against these implementation costs.

请注意，代码执行引入了自己的复杂性。运行智能体生成的代码需要一个安全的执行环境，具有适当的沙箱、资源限制和监控。这些基础设施要求增加了运营开销和安全考虑，而直接工具调用可以避免这些。代码执行的好处——降低令牌成本、降低延迟和改进的工具组合——应与这些实现成本进行权衡。

## Summary | 总结

MCP provides a foundational protocol for agents to connect to many tools and systems. However, once too many servers are connected, tool definitions and results can consume excessive tokens, reducing agent efficiency.

MCP 为智能体连接到许多工具和系统提供了基础协议。然而，一旦连接了太多服务器，工具定义和结果可能会消耗过多的令牌，降低智能体效率。

Although many of the problems here feel novel—context management, tool composition, state persistence—they have known solutions from software engineering. Code execution applies these established patterns to agents, letting them use familiar programming constructs to interact with MCP servers more efficiently. If you implement this approach, we encourage you to share your findings with the [MCP community](https://modelcontextprotocol.io/community).

尽管这里的许多问题看起来很新颖——上下文管理、工具组合、状态持久化——它们在软件工程中已有已知的解决方案。代码执行将这些已建立的模式应用于智能体，使它们能够使用熟悉的编程结构更高效地与 MCP 服务器交互。如果你实现这种方法，我们鼓励你与 [MCP 社区](https://modelcontextprotocol.io/community)分享你的发现。

### Acknowledgments | 致谢

This article was written by Adam Jones and Conor Kelly. Thanks to Jeremy Fox, Jerome Swannack, Stuart Ritchie, Molly Vorwerck, Matt Samuels, and Maggie Vo for feedback on drafts of this post.

本文由 Adam Jones 和 Conor Kelly 撰写。感谢 Jeremy Fox、Jerome Swannack、Stuart Ritchie、Molly Vorwerck、Matt Samuels 和 Maggie Vo 对本文草稿的反馈。
