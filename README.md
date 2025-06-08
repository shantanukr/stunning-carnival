# stunning-carnival

This project sets up a simple **MCP-style AI agent** using [Perplexity’s API](https://www.perplexity.ai) to run model-powered applications and tools.  
It uses **FastAPI** to expose callable functions (tools) and lets Perplexity's Sonar models intelligently decide when to use them.

---

## 🚀 Features

- 🌐 MCP-compatible tool server using FastAPI
- 🤖 Calls Perplexity’s Sonar models via API
- 🧰 Supports dynamic tool invocation via function-calling
- 🔐 Secure API key via `.env`
- 🐳 Dockerized for easy deployment

---

## 🧪 Example Use Case

Ask the model:

> “What’s the weather like in Tokyo?”

And the model can choose to call the `/tool/get_weather` API to fetch live or simulated data.

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/mcp-agent-perplexity.git
cd mcp-agent-perplexity
