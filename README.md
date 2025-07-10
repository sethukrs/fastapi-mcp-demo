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

## Project Structure

### 📁 Files Explained

- **`main.py`** - A simple FastAPI web application with two endpoints:
  - `/health` - Checks if the service is running
  - `/products` - Returns a list of products

- **`mcp_server.py`** - The MCP server that:
  - Connects to your FastAPI app
  - Exposes your API endpoints as "tools" that AI can use
  - Handles communication between AI assistants and your app

- **`demo_client.py`** - A simple script to test if the MCP server starts correctly

- **`test_tools.py`** - Tests the FastAPI endpoints directly to make sure they work

## Real-World Use Cases

### 🏪 E-commerce Assistant
Imagine an AI assistant that can:
- Search your product catalog
- Check inventory levels
- Process orders
- Answer customer questions about products

### 🏥 Healthcare System
An AI assistant could:
- Check patient records
- Schedule appointments
- Look up medical information
- Process insurance claims

### 🏢 Business Dashboard
AI could help by:
- Generating reports from your data
- Monitoring system health
- Sending notifications
- Analyzing trends

## How to Use This Demo

### 1. Start the FastAPI Server
```bash
uvicorn main:app --reload
```

### 2. Start the MCP Server
```bash
python mcp_server.py
```

### 3. Connect an AI Assistant
Any MCP-compatible AI tool can now:
- Check if your service is healthy
- Search for products in your catalog

## The Magic Behind the Scenes

### FastAPIMCPServer Class
This is the main class that:
- **Creates the bridge** between AI and your FastAPI app
- **Registers tools** that AI can use (like `health_check` and `search_products`)
- **Translates requests** from AI into HTTP calls to your API
- **Returns results** back to the AI in a format it understands

### 🔧 Internal Class Flow

```mermaid
graph TD
    A[FastAPIMCPServer] -->|"1. Initialize"| B[Create HTTP Client]
    A -->|"2. Register Tools"| C[Define Available Tools]
    C -->|"3. List Tools"| D[health_check, search_products]
    E[AI Request] -->|"4. Call Tool"| F[Tool Handler]
    F -->|"5. Check Tool Type"| G[Which Tool?]
    G -->|"health_check"| H[GET /health]
    G -->|"search_products"| I[GET /products]
    H -->|"6. Call FastAPI"| J[FastAPI Response]
    I -->|"6. Call FastAPI"| J
    J -->|"7. Format"| K[Return to AI]
```

### Key Methods:
- `_register_tools()` - Defines what actions AI can perform
- `call_tool()` - Executes the actual API calls when AI requests something
- `run()` - Starts the MCP server and keeps it running

## Why This Matters

### 🔒 Security
- AI assistants can only access what you explicitly allow
- No direct database access - everything goes through your API
- You control the permissions and data exposure

### 🔄 Flexibility
- Add new tools by simply adding new API endpoints
- Works with any MCP-compatible AI assistant
- Easy to extend and modify

### 🚀 Productivity
- AI can automate repetitive tasks
- Natural language interface to your systems
- Reduce manual work and errors

## Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start your FastAPI server:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Test the endpoints:**
   ```bash
   python test_tools.py
   ```

4. **Start the MCP server:**
   ```bash
   python mcp_server.py
   ```

5. **Connect an AI assistant** that supports MCP and start asking questions!

## Next Steps

- Add more API endpoints to your FastAPI app
- Create new tools in the MCP server
- Connect to databases or external services
- Add authentication and authorization
- Deploy to production

This demo shows the foundation - you can build much more complex systems using the same principles!