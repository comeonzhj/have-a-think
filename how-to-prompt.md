把[resources](resources)文件下的文件传给 Claude / windsurf / cursor

Prompt：

````md
学习理解项目知识库中关于 MCP 的资料，基于下面这个 API 请求和返回描述，为我构建一个`have-a-think`服务：当我需要大模型仔细想想时，大模型使用这个工具。把项目代码放在`/Users/jia/Downloads/codes/MCP`路径下，新建`have-a-think`文件。
API 请求示例：

```
curl https://api.deepseek.com/chat/completions \

  -H "Content-Type: application/json" \

  -H "Authorization: Bearer <DeepSeek API Key>" \

  -d '{

        "model": "deepseek-reasoner",

        "messages": [

          {"role": "system", "content": "You are a helpful assistant."},

          {"role": "user", "content": "需要深度思考的内容"}

        ],

        "stream": false,

        "max_tokens":1

      }'
```

API 返回内容示例,提取 `choices[0].message.reasoning_content` 的内容作为思考的结果。

```
{

  "id": "930c60df-bf64-41c9-a88e-3ec75f81e00e",

  "choices": [

    {

      "finish_reason": "stop",

      "index": 0,

      "message": {

        "reasoning_content": "Hello! How can I help you today?",

        "role": "assistant"

      }

    }

  ],

  "created": 1705651092,

  "model": "deepseek-chat",

  "object": "chat.completion",

  "usage": {

    "completion_tokens": 10,

    "prompt_tokens": 16,

    "total_tokens": 26

  }

}

```
````
