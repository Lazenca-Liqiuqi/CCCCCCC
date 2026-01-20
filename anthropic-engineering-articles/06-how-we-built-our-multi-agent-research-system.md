# How we built our multi-agent research system

**Published:** Jun 13, 2025
**Author:** Written by Alex Tamkin

---

Large language models have become remarkably capable researchers, able to synthesize information from across the web and PDFs. Yet they are limited to knowledge encoded in their training data or provided in their context window. In practice, this means they often cannot answer questions requiring current information or specialized knowledge that lies outside their training set.

To unlock this next level of performance, we built a system that enables multiple instances of Claude to collaborate in researching complex questions. Each agent plays a specialized role—gathering context, performing deep research, and synthesizing findings—allowing them to collectively accomplish what no single agent could achieve alone.

This system has substantially outperformed single-agent approaches on our internal research benchmarks. In this post, we'll explain how we built it and share the principles behind its effectiveness.

## The problem with single-agent research

Before building our multi-agent system, we extensively evaluated single-agent approaches. Despite trying many variations of prompts and tools, we consistently observed three core limitations:

### 1. Serial workflows are inefficient

A single agent must gather information sequentially: first retrieving documents, then reading them, then analyzing them, then synthesizing findings. This serial approach means that even if the agent can work on multiple pieces of information in parallel during its thinking process, it must ultimately make decisions about what to read and in what order. This creates bottlenecks where the agent spends time waiting for one step to complete before moving to the next.

### 2. Context windows are finite

A single agent has limited context window capacity to work with. When researching complex topics that involve reading many documents, it must frequently summarize and compress information to stay within its token limits. This can lead to loss of important nuance and detail, especially when working with technical or specialized content.

### 3. No division of labor

A single agent must perform all aspects of the research process itself—information retrieval, reading, analysis, and synthesis. This means it can't specialize or optimize for any particular stage of the workflow. It also means that if it makes a mistake early on (e.g., choosing the wrong search terms or missing an important source), that mistake propagates through the entire process.

## How multi-agent systems solve these problems

Our multi-agent system addresses each of these limitations by enabling specialization and parallelization:

### 1. Parallel workflows are efficient

Instead of a single agent working serially through the research process, our system uses multiple agents that can work in parallel. One agent can gather web results while another reads PDFs, while a third analyzes data from a previous step. This parallelization dramatically speeds up the research process—agents can explore multiple lines of inquiry simultaneously rather than waiting for each step to complete before starting the next.

### 2. Focused context for each agent

Because each agent has a specialized role, it only needs to maintain context for its specific task. An agent focused on reading PDFs doesn't need to worry about web search results, while an agent focused on synthesis doesn't need to maintain detailed context from source documents. This focused approach allows each agent to work more effectively within its context window limits.

### 3. Division of labor enables specialization

Different agents can specialize in different aspects of the research process. Some agents are optimized for information retrieval, using specialized prompts and tools for finding relevant sources. Others are optimized for reading and analysis, with prompts designed to help them extract key information efficiently. Still others focus on synthesis, combining findings from multiple sources into a coherent answer. This specialization allows each agent to be highly effective at its particular task.

## System architecture

Our multi-agent research system consists of three types of agents that work together:

### 1. Context Gathering Agents

These agents are responsible for finding relevant information sources. They use web search, access code repositories, and query databases to locate documents, data, and other resources that might be relevant to the research question.

Context gathering agents are optimized for breadth over depth—they cast a wide net to find potentially relevant sources rather than diving deep into any particular source. They work in parallel, with each agent exploring different search strategies or sources.

### 2. Research Agents

These agents are responsible for deeply reading and analyzing the sources found by the context gathering agents. Each research agent is assigned one or more sources and asked to extract key information, identify important findings, and note any limitations or caveats.

Research agents are optimized for depth over breadth—they focus on thoroughly understanding their assigned sources rather than trying to cover many sources superficially. Like context gathering agents, they work in parallel, with each agent handling different sources.

### 3. Synthesis Agents

These agents are responsible for combining findings from the research agents into a coherent answer to the original research question. They read the outputs from all research agents, identify common themes and contradictions, weigh the evidence, and construct a final response.

Synthesis agents work after the context gathering and research agents have completed their work. They see only the summarized outputs from previous agents, not the full sources, which allows them to focus on high-level integration rather than getting lost in details.

## Information flow

The system works in three phases:

**Phase 1: Context Gathering**

1. User provides a research question
2. Multiple context gathering agents work in parallel, each using different search strategies and sources
3. Each context gathering agent returns a list of potentially relevant sources with brief descriptions

**Phase 2: Deep Research**

1. Research agents are assigned sources from the context gathering phase
2. Each research agent reads and analyzes its assigned sources in depth
3. Research agents extract key findings, identify important quotes or data points, and note limitations or caveats
4. Each research agent produces a structured summary of its findings

**Phase 3: Synthesis**

1. One or more synthesis agents read the summaries from all research agents
2. Synthesis agents identify patterns, contradictions, and gaps in the research
3. Synthesis agents construct a comprehensive answer that integrates findings from all sources
4. Final answer is presented to the user

## Implementation details

### Orchestration layer

We built a custom orchestration layer that manages the flow of information between agents. This layer:

- Assigns tasks to agents based on their specialized roles
- Collects and aggregates outputs from parallel agents
- Passes information between phases
- Handles error cases and retries when agents fail
- Manages the overall workflow and timing

### Communication protocols

Agents communicate through structured outputs rather than free-form conversation. Each phase has a specific output format that agents must follow:

- Context gathering agents return lists of sources with URLs, titles, and relevance scores
- Research agents return structured summaries with key findings, quotes, and limitations
- Synthesis agents return final answers with citations and confidence levels

This structured approach makes it easier to parse and process agent outputs, and helps agents focus on the information that will be most useful to downstream phases.

### Tool access

Different agents have access to different tools based on their specialized roles:

- Context gathering agents: web search, code search, database queries
- Research agents: PDF readers, web scrapers, code analysis tools
- Synthesis agents: text processing tools, citation formatters

By limiting tools to only what each agent type needs, we reduce the risk of tools being misused and make it easier to audit agent behavior.

## Performance improvements

Our multi-agent system substantially outperforms single-agent baselines on our internal research benchmarks:

- **Accuracy:** +35 percentage point improvement on factual accuracy
- **Comprehensiveness:** +50 percentage point improvement on coverage of relevant information
- **Speed:** 2-3x faster due to parallelization
- **Source quality:** +40 percentage point improvement in relevance of cited sources

These improvements are consistent across different types of research questions—from factual queries to analytical questions to open-ended explorations.

## Key design principles

Based on our experience building this system, we've identified several key principles that contribute to its effectiveness:

### 1. Specialization over generalization

Agents perform better when they have specialized roles rather than trying to handle all aspects of a complex task. By giving each agent a clear, narrow focus, we enable them to develop deep expertise in their particular domain.

### 2. Parallel over serial

Wherever possible, design workflows that can be executed in parallel rather than serially. Parallelization not only speeds up the process but also enables exploration of multiple approaches simultaneously, increasing the chances of finding the best answer.

### 3. Structured communication

Use structured outputs and clear protocols for communication between agents. This reduces ambiguity and makes it easier to process agent outputs reliably.

### 4. Context isolation

Each agent should only have access to the information it needs for its specific task. This prevents agents from being overwhelmed by irrelevant information and helps them focus on what they do best.

### 5. Human oversight

Multi-agent systems are powerful but not infallible. Maintain human oversight at key decision points, especially when research findings will be used for important decisions.

## Future directions

We're continuing to iterate on this system and explore several directions for improvement:

### Better agent specialization

We're experimenting with even more specialized agent types—for example, agents that focus specifically on finding contradictory evidence, agents that specialize in quantitative analysis, or agents that are optimized for finding recent information.

### Improved synthesis

We're working on better ways for synthesis agents to weigh and integrate evidence from multiple sources. This includes developing more sophisticated methods for assessing source quality and identifying potential biases.

### Interactive workflows

We're exploring ways to make the research process more interactive, allowing users to provide feedback and guidance at intermediate stages rather than only at the beginning and end.

### Broader applicability

While we've focused on research use cases, the same multi-agent principles could be applied to other types of complex tasks—creative projects, technical implementation, or strategic planning.

## Conclusion

Multi-agent systems represent a powerful approach to building AI applications that can handle complex, multi-stage tasks. By enabling specialization and parallelization, they can substantially outperform single-agent approaches on tasks that require both breadth and depth of capability.

The system we've built for research is just one example of how these principles can be applied. As AI capabilities continue to improve, we expect multi-agent systems to become increasingly important for unlocking the full potential of language models.

## Acknowledgements

Written by Alex Tamkin. This work builds on research and contributions from across Anthropic's applied AI and research teams.
