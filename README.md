# FastAPI MCP Demo

A simple demonstration of how to connect AI assistants to your FastAPI applications using the Model Context Protocol (MCP).

## What is MCP?

**Model Context Protocol (MCP)** is like a universal translator that lets AI assistants talk to your applications and services. Think of it as a bridge that allows AI tools (like ChatGPT, Claude, or other AI assistants) to safely access and control your software systems.

## How This Demo Works

This demo shows how to create an MCP server that connects AI assistants to a FastAPI web application. Here's the flow:

1. **FastAPI App** (`main.py`) - Your web application with endpoints
2. **MCP Server** (`mcp_server.py`) - The bridge that translates AI requests into API calls
3. **AI Assistant** - Any MCP-compatible AI tool that can use your services

### 🔄 System Flow Diagram

```mermaid
graph LR
    A[User] -->|"Ask question"| B[AI Assistant]
    B -->|"Request tool"| C[MCP Server]
    C -->|"Call API"| D[FastAPI App]
    D -->|"Return data"| C
    C -->|"Format response"| B
    B -->|"Show answer"| A
```

### 🏗️ Real-World Architecture

```mermaid
graph TB
    subgraph AI_Layer
        A1[ChatGPT]
        A2[Claude]
        A3[Custom AI]
    end
    subgraph MCP_Layer
        B1[MCP Server]
        B2[Tool Registry]
    end
    subgraph Application_Layer
        C1[FastAPI App]
        C2[Database]
        C3[External APIs]
    end
    A1 --> B1
    A2 --> B1
    A3 --> B1
    B1 --> B2
    B1 --> C1
    C1 --> C2
    C1 --> C3
```

## Real-World Use Cases

### 🏪 E-commerce Assistant
Imagine an AI assistant that can:
- 🔍 Search product catalog
- 🛒 View customer carts
- 📦 Track inventory


### Connect an AI Assistant
Any MCP-compatible AI tool can now:
- Show user shopping carts
- Search for products in your catalog


### 🔧 Internal Class Flow

```mermaid
graph TD
    A[FastAPIMCPServer] -->|"Initialize"| B[Create HTTP Client]
    A -->|"Register Tools"| C[Define Available Tools]
    C -->|"List Tools"| D[get_carts, search_products]
    E[AI Request] -->|"Call Tool"| F[Tool Handler]
    F -->|"Check Tool Type"| G[Which Tool?]
    G -->|"get_carts"| H[GET /carts]
    G -->|"search_products"| I[GET /products]
    H -->|"Call FastAPI"| J[FastAPI Response]
    I -->|"Call FastAPI"| J
    J -->|"Format"| K[Return to AI]
```

5. **Connect an AI assistant** that supports MCP and start asking questions!

This demo shows the foundation feasibility!