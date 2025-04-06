#!/usr/bin/env python3
"""
MCP server that provides a 'have-a-think' tool to let Claude use the DeepSeek Reasoner model
for deeper reasoning on complex topics.
"""

import os
import json
import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP, Context

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variable
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
if not DEEPSEEK_API_KEY:
    print("WARNING: DEEPSEEK_API_KEY not set in environment or .env file.")
    print("The server will start, but the have-a-think tool will fail without an API key.")

# Create the MCP server
mcp = FastMCP("DeepSeek Reasoner")


@mcp.tool()
async def have_a_think(question: str, ctx: Context = None) -> str:
    """
    Use the DeepSeek Reasoner model to think deeply about a complex question.
    
    Args:
        question: The question or topic to think about
    
    Returns:
        Detailed reasoning process and thoughts about the question
    """
    if ctx:
        ctx.info(f"Thinking deeply about: {question}")
    
    if not DEEPSEEK_API_KEY:
        return "Error: DeepSeek API key not configured. Please set the DEEPSEEK_API_KEY environment variable."
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://api.deepseek.com/chat/completions",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
                },
                json={
                    "model": "deepseek-reasoner",
                    "messages": [
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": question}
                    ],
                    "stream": False,
                    "max_tokens": 1  # Set a reasonable limit
                },
                timeout=60.0  # Longer timeout for detailed reasoning
            )
            
            if response.status_code != 200:
                return f"Error from DeepSeek API: {response.status_code} {response.text}"
            
            data = response.json()
            
            # Extract the reasoning content from the response
            reasoning = data.get("choices", [{}])[0].get("message", {}).get("reasoning_content", "")
            
            if not reasoning:
                return "No reasoning content was provided by the DeepSeek model."
                
            return reasoning
    
    except Exception as e:
        return f"Error connecting to DeepSeek API: {str(e)}"


if __name__ == "__main__":
    # Run the server
    mcp.run()
