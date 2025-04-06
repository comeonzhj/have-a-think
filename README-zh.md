# Have a think MCP Server

[English](README-en.md)|中文

全程由 Claude 构建，相关提示词参考[how-to-prompt](how-to-prompt.md)

## 如何使用

1. 确保已经安装了 python 3.10+
2. clone 仓库

```bash
git clone https://github.com/comeonzhj/have-a-think.git
```
3. 安装依赖
```bash
pip install "mcp[cli]" httpx python-dotenv
```

4. 创建一个 `.env` 文件保存你的 DeepSeek API key:

```
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

你可以从 [DeepSeek's website](https://platform.deepseek.com/) 获取 DeepSeek 的 Key


直接运行服务:

```bash
python have-a-think.py
```

安装到 Claude / windsurf / cursor / 5ir 等客户端：

```json
{
    "mcpServers": {
      "deepseek-reasoner": {
        "command": "python",
        "args": [
          "/path/to/have-a-think/have-a-think.py"
        ],
        "env": {
          "DEEPSEEK_API_KEY": "your_deepseek_api_key_here"
        }
      }
    }
  }
```

