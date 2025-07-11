#!/usr/bin/env python3
# mcp_server.py
import asyncio
from typing import Any, Dict
import httpx

from mcp.server import Server
from mcp.server.models import InitializationOptions
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent, ServerCapabilities

import sys

class FastAPIMCPServer:
    def __init__(self):
        self.client = httpx.AsyncClient()
        self.server = Server("FastAPI-MCP")

        self._register_tools()

    def _register_tools(self):
        @self.server.list_tools()
        async def list_tools():
            return [
                Tool(
                    name="get_carts",
                    description="Get shopping carts for a user using FastAPI",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "user_id": {"type": "integer"}
                        },
                        "required": ["user_id"]
                    }
                ),
                Tool(
                    name="search_products",
                    description="Search for products using FastAPI",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "channel_id": {"type": "integer"},
                            "catalog_id": {"type": "integer"}
                        },
                        "required": ["channel_id", "catalog_id"]
                    }
                )
            ]

        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]):
            try:
                if name == "get_carts":
                    resp = await self.client.get("http://localhost:8000/carts", params=arguments)
                elif name == "search_products":
                    resp = await self.client.get("http://localhost:8000/products", params=arguments)
                else:
                    return [TextContent(type="text", text=f"Error: Unknown tool {name}")]

                resp.raise_for_status()
                return [TextContent(type="text", text=resp.text)]

            except Exception as e:
                return [TextContent(type="text", text=f"Error: {str(e)}")]

    async def shutdown(self):
        await self.client.aclose()

    async def run(self):
        async with stdio_server() as (r, w):
            await self.server.run(
                r, w,
                InitializationOptions(
                    server_name="FastAPI-MCP", 
                    server_version="1.0",
                    capabilities=ServerCapabilities(
                        tools={}
                    )
                )
            )
        await self.shutdown()

if __name__ == "__main__":
    try:
        asyncio.run(FastAPIMCPServer().run())
    except KeyboardInterrupt:
        print("Server stopped by user", file=sys.stderr, flush=True)
    except Exception as e:
        print(f"Startup error: {e}", file=sys.stderr, flush=True)
        import traceback
        traceback.print_exc(file=sys.stderr)
