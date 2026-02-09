# 北大法宝 (PKULaw) Claude Code Plugin

这是一个专为法律专业人士设计的 Claude Code 插件，集成了北大法宝（PKULaw）的检索能力，并提供智能化的合同审查与合规咨询功能。

## 功能特性

*   **法律检索 (`/research`)**：
    *   检索最新的中国法律法规。
    *   查询相关的司法判例（指导性案例、公报案例等）。
    *   自动生成法律研究报告。

*   **合同审查 (`/review`)**：
    *   自动扫描 Word 文档 (`.docx`)。
    *   识别责任限制、知识产权、违约责任等关键条款的风险。
    *   **直接在文档中添加批注**，方便审阅和修改。

*   **合规咨询 (`/compliance`)**：
    *   针对企业规章制度或具体业务场景进行合规性检查。
    *   引用法规原文作为依据。

## 安装指南

### 1. 准备环境

确保已安装 [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview) 和 Python 3.10+。

```bash
# 安装 Python 依赖
pip install -r requirements.txt
```

### 2. 添加为本地插件

在项目根目录下运行：

```bash
# 1. 添加当前目录为插件市场
claude plugin marketplace add .

# 2. 安装插件
claude plugin install pkulaw@local-market
```

### 3. 开始使用

安装完成后，直接在 Claude Code 中输入命令：

- `/research 民法典关于居住权的规定`
- `/review /path/to/contract.docx`
- `/compliance 审查这份员工手册`

## 目录结构

*   `commands/`：定义了 Claude Code 的斜杠命令。
*   `skills/`：定义了具体的业务逻辑和处理流程。
*   `server.py`：基于 MCP (Model Context Protocol) 实现的后端服务，提供检索和文档处理能力。
*   `scripts/`：核心功能脚本（检索模拟、文档批注）。

## 数据来源

本插件现已配置为从北大法宝（PKULaw）真实 API获取数据。

**必须配置 Authentication Token**：
使用前，您必须在运行环境中设置环境变量 `PKULAW_API_TOKEN`。

```bash
export PKULAW_API_TOKEN="your_token_here"
```

如果您使用 Claude Desktop，可以在 `claude_desktop_config.json` 的 `env` 字段中配置：

```json
{
  "mcpServers": {
    "pkulaw": {
      "command": "...",
      "env": {
        "PKULAW_API_TOKEN": "your_token_here"
      }
    }
  }
}
```
