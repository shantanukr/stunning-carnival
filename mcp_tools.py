# mcp_tools.py
tool_schema = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather in a city",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "The name of the city"}
            },
            "required": ["city"]
        }
    }
}]
