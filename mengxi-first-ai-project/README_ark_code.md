# 使用 ark-code-latest 模型进行代码优化

## 概述

本项目提供了一个示例脚本，用于调用字节跳动的 `ark-code-latest` 模型进行代码优化。该模型专门为代码生成、补全和优化任务设计，具有强大的代码理解和优化能力。

## 环境配置

### 1. 安装依赖
确保安装了所需的 Python 库：
```bash
pip install httpx
```

### 2. 配置环境变量
在终端中设置以下环境变量，或者将它们添加到 `~/.zshrc` 文件中永久生效：
```bash
export ANTHROPIC_AUTH_TOKEN="your-api-key"
export ANTHROPIC_BASE_URL="https://ark.cn-beijing.volces.com/api/coding"
export ANTHROPIC_MODEL="ark-code-latest"
```

## 使用方法

### 1. 基本使用

#### 代码优化任务
运行脚本以使用默认的代码优化示例：
```bash
python call_ark_code.py
```

### 2. 自定义任务

#### 使用自定义消息
```bash
python call_ark_code.py --task custom --message "你的问题或任务描述"
```

#### 示例：解释代码功能
```bash
python call_ark_code.py --task custom --message "请解释以下代码的功能：\ndef factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n-1)\n"
```

#### 示例：优化 JavaScript 代码
```bash
python call_ark_code.py --task custom --message "请优化以下 JavaScript 代码以提高性能：\nfunction fibonacci(n) {\n    if (n <= 1) return n;\n    return fibonacci(n-1) + fibonacci(n-2);\n}\n"
```

### 3. 配置参数

#### 调整最大输出长度
```bash
python call_ark_code.py --max-tokens 4096
```

## 脚本功能

### 核心功能

1. **代码优化**：自动分析和优化代码，提高性能和可读性
2. **代码解释**：解释代码功能和工作原理
3. **代码转换**：在不同编程语言之间转换代码
4. **调试帮助**：帮助识别和修复代码中的错误

### 高级特性

1. **结构化输出**：返回格式规范的 Markdown 文档
2. **详细分析**：提供优化方案的详细说明
3. **输入验证**：对输入进行验证，确保安全性
4. **错误处理**：完善的错误处理机制

## 支持的编程语言

`ark-code-latest` 支持多种编程语言的优化，包括但不限于：

- Python
- JavaScript
- TypeScript
- Java
- C++
- Go
- Rust

## 示例输出说明

模型的输出通常包含以下部分：

1. **代码优化分析**：对原始代码的问题分析
2. **优化方案**：提出的优化策略
3. **优化后的代码**：最终的优化结果
4. **优化说明**：详细说明修改点和改进原因

## 注意事项

1. **API 密钥安全**：确保 `ANTHROPIC_AUTH_TOKEN` 的安全，不要在代码中硬编码
2. **网络连接**：调用 API 需要稳定的网络连接
3. **API 限制**：注意 API 调用频率和配额限制
4. **复杂代码**：对于非常复杂的代码，可能需要多次调用或更详细的描述

## 常见问题

### 1. 如何获取 API 密钥？
您可以通过字节跳动的火山引擎平台申请 API 密钥。

### 2. 模型返回的代码有错误怎么办？
如果模型返回的代码有错误，可以尝试更详细地描述问题，或者提供更多上下文信息。

### 3. 如何提高优化质量？
可以尝试：
- 更详细地描述优化目标
- 提供代码的上下文信息
- 指定编程语言和版本
- 明确性能或可读性要求

## 扩展功能

本脚本可以进一步扩展，添加以下功能：

1. **文件处理**：支持读取文件内容作为输入
2. **批量处理**：对多个文件进行批量优化
3. **结果保存**：将结果保存到文件
4. **GUI 界面**：提供图形用户界面
5. **集成开发环境**：与 IDE 集成，提供实时优化建议

## 技术细节

### API 调用

脚本使用 HTTP POST 请求直接调用字节跳动的 Ark API：
```python
url = f"{base_url}/v1/messages"
headers = {
    "Content-Type": "application/json",
    "x-api-key": api_key
}
data = {
    "model": model,
    "max_tokens": max_tokens,
    "messages": messages
}
```

### 请求格式

使用聊天格式，每个请求包含一个或多个消息，消息包含角色（user 或 assistant）和内容。

### 响应格式

响应格式为 JSON，包含模型回复和使用信息。

## 许可证

本项目遵循 MIT 许可证。
