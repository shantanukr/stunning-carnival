# run_agent.py
from agent import call_perplexity
from mcp_tools import tool_schema

prompt = "What's the weather like in Tokyo?"

response = call_perplexity(prompt, tool_schema)

message = response["choices"][0]["message"]["content"]
print("🧠 Model Response:")
print(message)
