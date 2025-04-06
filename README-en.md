# Have-a-Think MCP Server
English｜[中文]()

All Created By Claude。

This MCP (Model Context Protocol) server provides a tool that allows Claude to use the DeepSeek Reasoner model for deeper reasoning on complex topics.

## Overview

The `have-a-think` tool sends queries to the DeepSeek Reasoner model, which excels at step-by-step reasoning and can help with complex problem-solving when Claude wants to "think more deeply" about a subject.

## Setup

1. Make sure you have Python 3.10+ installed
2. Install the required dependencies:

```bash
pip install "mcp[cli]" httpx python-dotenv
```

3. Create a `.env` file with your DeepSeek API key:

```
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

You can get an API key from [DeepSeek's website](https://platform.deepseek.com/).

## Usage

### Running the server directly

Run the server with:

```bash
python have-a-think.py
```

### Using with MCP Inspector

For development and testing:

```bash
mcp dev have-a-think.py
```

### Installing with Claude Desktop

1. Make sure you have [Claude Desktop](https://claude.ai/download) installed
2. Use the mcp CLI to install the server:

```bash
mcp install have-a-think.py
```

Or configure Claude Desktop manually by editing the configuration file:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Add this to the `mcpServers` object in the config:

```json
{
  "mcpServers": {
    "deepseek-reasoner": {
      "command": "python",
      "args": ["/path/to/have-a-think.py"],
      "env": {
        "DEEPSEEK_API_KEY": "your_deepseek_api_key_here"
      }
    }
  }
}
```

## Using in Claude

Once installed in Claude Desktop, Claude can use the `have-a-think` tool when it needs to reason through complex problems. The tool takes a single argument:

- `question`: The topic or question for deeper reasoning

Claude will automatically decide when to use the tool when faced with complex reasoning tasks.

## License

MIT
