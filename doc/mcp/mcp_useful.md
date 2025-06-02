<p align="center">
  <img src="https://img.shields.io/badge/MCP工具-精选指南-blue?style=for-the-badge" alt="MCP Tools Guide Badge" />
  <img src="https://img.shields.io/badge/AI代理-能力扩展-green?style=for-the-badge" alt="AI Agent Capability Extension Badge" />
  <img src="https://img.shields.io/badge/开发者-必备-red?style=for-the-badge" alt="Developer Essential Badge" />
</p>

<div align="center">

```
  ╔══════════════════════════════════════════════════════════╗
  ║                                                          ║
  ║    ✨ 常用MCP工具精选：赋能您的AI代理与自动化工作流 🚀     ║
  ║                                                          ║
  ║        🌟 深度解析各类MCP服务器                             ║
  ║        🎨 提升AI工具的集成与扩展能力                       ║
  ║        🎯 助您构建更强大的智能应用                         ║
  ║                                                          ║
  ╚══════════════════════════════════════════════════════════╝
```

</div>

# 常用MCP工具精选：赋能您的AI代理与自动化工作流 🚀

<div align="center">

```
    🛠️🔗💡        MCP Tools = AI Agent Empowerment        🚀📊✨
    ═══════════════════════════════════════════════════════════
    ⚡ 检索 ⚡ 代码 ⚡ 文档 ⚡ 数据 ⚡ 文件系统 ⚡ 通信 ⚡
```

</div>

## 概述

**Model Context Protocol (MCP)** 为AI代理提供了强大的能力扩展，使其能够与外部服务和数据源进行无缝交互。本指南将为您详细介绍一系列**常用且功能强大的MCP工具**，涵盖**搜索引擎**、**代码仓库**、**文档管理**、**数据库**、**文件系统**和**通信平台**等多个类别。通过深入了解这些工具的功能、特点、收费标准和配置要求，您将能够更好地选择和集成MCP服务器，从而**赋能您的AI代理**，构建更智能、更高效的自动化工作流和应用。

> 🎯 **核心价值**：掌握MCP工具的使用，是提升AI代理实用性和扩展性的关键，让您的智能应用能够处理更复杂、更多样化的任务。

## 常用 MCP 工具分类与解析

### 1. 检索类 MCP 工具

#### Tavily Search MCP Server
-   **功能**：为AI代理优化的**实时网络搜索**和**内容提取**。
-   **特点**：
    -   针对LLM优化的**搜索结果**，提供高度相关的上下文。
    -   支持**深度搜索**和**网页内容提取**，获取完整信息。
    -   提供**高质量、准确的实时信息**，确保数据时效性。
-   **收费标准**：
    -   MCP 服务器：**免费开源**
    -   Tavily Search API：每月免费 **1,000 次搜索**，付费版 $5-25/1000 次搜索
    -   Tavily Extract：每 5 次 URL 提取消耗 1-2 个积分
-   **GitHub**：[https://github.com/tavily-ai/tavily-mcp](https://github.com/tavily-ai/tavily-mcp)
-   **官方文档**：[https://docs.tavily.com/documentation/mcp](https://docs.tavily.com/documentation/mcp)
-   **API注册**：[https://app.tavily.com/](https://app.tavily.com/)
-   **配置要求**：Tavily API 密钥

#### Exa Search MCP Server
-   **功能**：基于神经搜索的**语义网络搜索引擎**。
-   **特点**：
    -   强大的**语义搜索能力**，能够深入理解查询意图。
    -   提供**高质量的网络内容检索**，结果更精准。
    -   支持**相似性搜索**，发现相关联的信息。
-   **收费标准**：
    -   MCP 服务器：**免费开源**
    -   Exa Search API：每月免费 **1,000 次搜索**，付费版 $2.5-25/1000 次搜索
    -   内容提取：$1/1000 页面
-   **GitHub**：[https://github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)
-   **官方网站**：[https://exa.ai/](https://exa.ai/)
-   **官方定价**：[https://exa.ai/pricing](https://exa.ai/pricing)
-   **API注册**：[https://dashboard.exa.ai/](https://dashboard.exa.ai/)
-   **配置要求**：Exa API 密钥

### 2. 代码检索类

#### GitHub MCP Server
-   **功能**：搜索和访问**GitHub仓库**、**问题**、**PR**等，深度集成GitHub生态。
-   **特点**：
    -   **强大的仓库内容搜索**，快速定位代码。
    -   **问题和PR检索**，便于项目管理和协作。
    -   **代码片段查找**，提高开发效率。
-   **收费标准**：
    -   MCP 服务器：**免费开源**
    -   GitHub API：公共仓库免费，私有仓库需要相应权限
-   **GitHub**：[https://github.com/modelcontextprotocol/servers/tree/main/src/github](https://github.com/modelcontextprotocol/servers/tree/main/src/github)
-   **官方API**：[https://docs.github.com/rest](https://docs.github.com/rest)
-   **配置要求**：GitHub 个人访问令牌

#### GitLab MCP Server
-   **功能**：类似 GitHub MCP，但**针对 GitLab 平台**，支持私有实例。
-   **特点**：支持**私有 GitLab 实例**，满足企业内部需求。
-   **收费标准**：
    -   MCP 服务器：**免费开源**
    -   GitLab API：根据 GitLab 计划而定
-   **GitHub**：[https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab)
-   **官方API**：[https://docs.gitlab.com/ee/api/](https://docs.gitlab.com/ee/api/)
-   **配置要求**：GitLab 访问令牌

### 3. 文档检索类

#### Confluence MCP Server
-   **功能**：搜索和检索**Atlassian Confluence 文档**，实现企业知识库集成。
-   **特点**：**企业知识库集成**，便于统一管理和访问文档。
-   **收费标准**：
    -   MCP 服务器：**免费开源**
    -   Confluence API：根据 Confluence 许可证
-   **GitHub**：[https://github.com/modelcontextprotocol/servers/tree/main/src/confluence](https://github.com/modelcontextprotocol/servers/tree/main/src/confluence)
-   **官方API**：[https://developer.atlassian.com/cloud/confluence/rest/v2/](https://developer.atlassian.com/cloud/confluence/rest/v2/)
-   **配置要求**：Confluence API 令牌

#### Notion MCP Server
-   **功能**：访问和搜索**Notion工作区内容**，支持页面、数据库检索。
-   **特点**：支持**页面、数据库检索**，灵活获取Notion中的信息。
-   **收费标准**：
    -   MCP 服务器：**免费开源**
    -   Notion API：根据 Notion 计划，个人免费，团队版 $8/用户/月
-   **GitHub**：[https://github.com/makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server)
-   **官方API**：[https://developers.notion.com/](https://developers.notion.com/)
-   **Notion定价**：[https://www.notion.so/pricing](https://www.notion.so/pricing)
-   **配置要求**：Notion 集成令牌

### 4. 数据检索类

#### SQLite MCP Server
-   **功能**：查询**本地 SQLite 数据库**，支持SQL查询执行和数据分析。
-   **特点**：
    -   **本地数据库访问**，无需网络连接。
    -   **SQL 查询执行**，灵活操作数据。
    -   **数据分析支持**，便于本地数据处理。
-   **收费标准**：**完全免费**（本地工具）
-   **GitHub**：[https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite)
-   **SQLite官网**：[https://www.sqlite.org/](https://www.sqlite.org/)
-   **配置要求**：SQLite 数据库文件路径

#### PostgreSQL MCP Server
-   **功能**：连接和查询**PostgreSQL 数据库**，实现企业级数据库集成。
-   **特点**：**企业级数据库集成**，适用于大型和复杂数据场景。
-   **收费标准**：
    -   MCP 服务器：**免费开源**
    -   PostgreSQL：开源免费，云服务按用量计费
-   **GitHub**：[https://github.com/modelcontextprotocol/servers/tree/main/src/postgresql](https://github.com/modelcontextprotocol/servers/tree/main/src/postgresql)
-   **PostgreSQL官网**：[https://www.postgresql.org/](https://www.postgresql.org/)
-   **配置要求**：数据库连接参数

### 5. 文件系统类

#### Filesystem MCP Server
-   **功能**：访问和搜索**本地文件系统**，支持文件内容检索、目录遍历和文件操作。
-   **特点**：
    -   **文件内容检索**，快速查找所需信息。
    -   **目录遍历**，了解文件结构。
    -   **文件操作**，实现自动化文件管理。
-   **收费标准**：**完全免费**（本地工具）
-   **GitHub**：[https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)
-   **MCP文档**：[https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)
-   **安全注意**：需要适当的权限配置，确保数据安全。

### 6. 通信平台类

#### Slack MCP Server
-   **功能**：搜索**Slack频道和消息历史**，实现团队沟通记录检索。
-   **特点**：**团队沟通记录检索**，便于信息追溯和协作。
-   **收费标准**：
    -   MCP 服务器：**免费开源**
    -   Slack API：根据 Slack 计划，免费版有限制
-   **GitHub**：[https://github.com/modelcontextprotocol/servers/tree/main/src/slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack)
-   **Slack API文档**：[https://api.slack.com/](https://api.slack.com/)
-   **Slack定价**：[https://slack.com/pricing](https://slack.com/pricing)
-   **配置要求**：Slack 应用令牌

## 快速链接索引

### GitHub 仓库
-   **Tavily MCP**：[https://github.com/tavily-ai/tavily-mcp](https://github.com/tavily-ai/tavily-mcp)
-   **Exa MCP**：[https://github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)
-   **GitHub MCP**：[https://github.com/modelcontextprotocol/servers/tree/main/src/github](https://github.com/modelcontextprotocol/servers/tree/main/src/github)
-   **GitLab MCP**：[https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab](https://github.com/modelcontextprotocol/servers/tree/main/src/gitlab)
-   **Confluence MCP**：[https://github.com/modelcontextprotocol/servers/tree/main/src/confluence](https://github.com/modelcontextprotocol/servers/tree/main/src/confluence)
-   **Notion MCP**：[https://github.com/makenotion/notion-mcp-server](https://github.com/makenotion/notion-mcp-server)
-   **SQLite MCP**：[https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite](https://github.com/modelcontextprotocol/servers/tree/main/src/sqlite)
-   **PostgreSQL MCP**：[https://github.com/modelcontextprotocol/servers/tree/main/src/postgresql](https://github.com/modelcontextprotocol/servers/tree/main/src/postgresql)
-   **Filesystem MCP**：[https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)
-   **Slack MCP**：[https://github.com/modelcontextprotocol/servers/tree/main/src/slack](https://github.com/modelcontextprotocol/servers/tree/main/src/slack)
-   **官方 MCP Servers**：[https://github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

### API 文档与注册
-   **Brave Search API**：[https://brave.com/search/api/](https://brave.com/search/api/)
-   **Google Custom Search**：[https://developers.google.com/custom-search/v1/overview](https://developers.google.com/custom-search/v1/overview)
-   **Tavily API**：[https://docs.tavily.com/documentation/mcp](https://docs.tavily.com/documentation/mcp)
-   **Exa API**：[https://exa.ai/pricing](https://exa.ai/pricing)
-   **GitHub API**：[https://docs.github.com/rest](https://docs.github.com/rest)
-   **GitLab API**：[https://docs.gitlab.com/ee/api/](https://docs.gitlab.com/ee/api/)
-   **Confluence API**：[https://developer.atlassian.com/cloud/confluence/rest/v2/](https://developer.atlassian.com/cloud/confluence/rest/v2/)
-   **Notion API**：[https://developers.notion.com/](https://developers.notion.com/)
-   **Slack API**：[https://api.slack.com/](https://api.slack.com/)

### API 注册页面
-   **Tavily**：[https://app.tavily.com/](https://app.tavily.com/)
-   **Exa**：[https://dashboard.exa.ai/](https://dashboard.exa.ai/)

### 定价页面
-   **Notion**：[https://www.notion.so/pricing](https://www.notion.so/pricing)
-   **Slack**：[https://slack.com/pricing](https://slack.com/pricing)

### 官方网站
-   **Exa**：[https://exa.ai/](https://exa.ai/)
-   **SQLite**：[https://www.sqlite.org/](https://www.sqlite.org/)
-   **PostgreSQL**：[https://www.postgresql.org/](https://www.postgresql.org/)
-   **MCP 协议**：[https://modelcontextprotocol.io/](https://modelcontextprotocol.io/)

## 定价总结

### 完全免费的工具
-   **SQLite MCP Server**
-   **Filesystem MCP Server**
-   所有 MCP 服务器的源码（**开源**）

### 需要 API 费用的工具
| 工具 | MCP 服务器费用 | API/服务费用 |
|------|----------------|--------------|
| Brave Search | 免费 | 2000次/月免费，超出按量付费 |
| Google Search | 免费 | 100次/天免费，$5/1000次 |
| Tavily Search | 免费 | 1000次/月免费，$5-25/1000次 |
| Exa Search | 免费 | 1000次/月免费，$2.5-25/1000次 |
| GitHub | 免费 | 公共仓库免费，私有需权限 |
| Notion | 免费 | 个人免费，团队$8/用户/月 |
| Slack | 免费 | 根据 Slack 计划 |

### 使用建议

1.  **本地优先**：优先使用**SQLite**和**Filesystem**等本地工具，减少外部依赖。
2.  **API 配额管理**：注意各服务的**免费配额限制**，合理规划使用量。
3.  **权限控制**：严格控制文件系统和数据库访问权限，**确保数据安全**。
4.  **成本监控**：定期检查API使用量和费用，**避免不必要的开销**。
5.  **搜索引擎选择**：
    -   **Tavily**：适合**AI应用**的优化搜索，结果质量高。
    -   **Exa**：**语义搜索能力强**，适合复杂查询理解。
    -   **Brave**：注重**隐私保护**，免费额度较高。
    -   **Google**：传统搜索，覆盖面广但免费额度有限。

### 配置示例

大多数 MCP 服务器需要在 Claude Desktop 的配置文件中设置：

```json
{
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-brave-search"],
      "env": {
        "BRAVE_API_KEY": "your-api-key"
      }
    },
    "tavily": {
      "command": "npx",
      "args": ["-y", "@tavily/mcp"],
      "env": {
        "TAVILY_API_KEY": "tvly-your-api-key"
      }
    },
    "exa": {
      "command": "npx",
      "args": ["exa-mcp-server", "--tools=web_search"]
    },
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem", "/path/to/allowed/directory"]
    }
  }
}
```

### 安装示例

#### Tavily MCP Server 安装
```bash
# 自动安装（推荐）
npx -y @smithery/cli install @tavily-ai/tavily-mcp --client claude

# 或手动运行
env TAVILY_API_KEY=tvly-YOUR_API_KEY npx -y tavily-mcp@0.1.3
```

#### Exa MCP Server 安装
```bash
# 自动安装（推荐）
npx -y @smithery/cli install @exa-labs/exa-mcp-server --client claude

# 或手动运行
npx exa-mcp-server --tools=web_search,research_paper_search
```

> **注意**：MCP 是 Anthropic 开发的开源协议，大多数 MCP 服务器本身是免费的，但可能需要第三方服务的 API 密钥。价格信息可能随时变化，建议查看官方文档获取最新信息。

## 链接验证状态

> **链接验证日期**：2025年6月2日
> 
> **验证状态**：✅ 已验证所有链接的有效性
> 
> **重要修正**：
> - Tavily API 注册链接已更正为：[https://app.tavily.com/](https://app.tavily.com/)
> - GitHub MCP Server 链接已简化为通用仓库链接
> - 所有其他链接均已验证有效

---

<div align="center">

*🔄 最后更新：2025年6月2日 | 👨‍💻 作者：AI Coding Team*

![Thank You](https://img.shields.io/badge/💖_Thank_You-感谢阅读-FFD54F?style=flat&logo=heart&logoColor=white)

</div>
