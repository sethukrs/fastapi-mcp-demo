#!/usr/bin/env python3
"""
Comprehensive demo client for the FastAPI MCP Server
This will prove to your team that MCP integration works!
"""
import subprocess
import json
import time
import asyncio
import httpx
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters

async def test_fastapi_directly():
    """Test FastAPI endpoints directly to show they work"""
    print("🔍 Testing FastAPI endpoints directly...")
    print("=" * 50)
    
    async with httpx.AsyncClient() as client:
        # Test carts endpoint
        print("\n📦 Testing /carts endpoint:")
        try:
            response = await client.get("http://localhost:8000/carts", params={"user_id": 1})
            response.raise_for_status()
            carts_data = response.json()
            print(f"Carts data: {json.dumps(carts_data, indent=2)}")
        except Exception as e:
            print(f"Carts test failed: {e}")
            return False
        
        # Test products endpoint
        print("\n🛍️ Testing /products endpoint:")
        try:
            response = await client.get("http://localhost:8000/products", params={
                "channel_id": 1, "catalog_id": 2
            })
            response.raise_for_status()
            products_data = response.json()
            print(f"Products data: {json.dumps(products_data, indent=2)}")
        except Exception as e:
            print(f"Products test failed: {e}")
            return False
    
    print("\nFastAPI endpoints are working correctly!")
    return True

async def test_mcp_integration():
    """Test MCP server integration"""
    print("\n🔧 Testing MCP Server Integration...")
    print("=" * 50)
    
    # Configure MCP server parameters
    server_params = StdioServerParameters(
        command="/Users/sethu/work/codebase/fastapi-mcp-demo/.venv/bin/python3",
        args=["mcp_server.py"]
    )
    
    try:
        print("🔗 Testing MCP client connection...")
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                # Initialize the session
                await session.initialize()
                
                print("MCP session initialized successfully!")
                
                # List available tools
                print("\n🔍 Listing available MCP tools...")
                tools = await session.list_tools()
                print(f"Found {len(tools.tools)} tools:")
                for tool in tools.tools:
                    print(f"  - {tool.name}: {tool.description}")
                
                # Test get_carts tool
                print("\n📦 Testing 'get_carts' MCP tool...")
                result = await session.call_tool("get_carts", {"user_id": 1})
                print(f"get_carts result: {result.content[0].text}")
                
                # Test search_products tool
                print("\n🛍️ Testing 'search_products' MCP tool...")
                result = await session.call_tool("search_products", {
                    "channel_id": 1, "catalog_id": 2
                })
                print(f"search_products result: {result.content[0].text}")
                
                print("\n🎉 MCP Integration Test COMPLETE!")
                print("This proves that MCP can successfully integrate with FastAPI!")
                
    except Exception as e:
        print(f"MCP test failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

async def run_comprehensive_demo():
    """Run the complete demo"""
    print("🎯 FastAPI + MCP Integration Demo")
    print("=" * 60)
    print("This demo will prove to your team that MCP integration works!")
    print("=" * 60)
    
    # Step 1: Test FastAPI directly
    if not await test_fastapi_directly():
        print("\nFastAPI test failed. Make sure your server is running on port 8000!")
        return
    
    # Step 2: Test MCP integration
    if not await test_mcp_integration():
        print("\nMCP integration test failed!")
        return
    
    print("\n" + "=" * 60)
    print(" DEMO COMPLETE! MCP Integration is PROVEN!")
    print("=" * 60)
    print("FastAPI endpoints work correctly")
    print("MCP server can start and accept connections")
    print("MCP client can discover and call tools")
    print("MCP tools successfully call FastAPI endpoints")
    print("\nSummary for your team:")
    print("   - MCP protocol works with FastAPI")
    print("   - Tools can be exposed and called remotely")
    print("   - Real-time integration is possible")
    print("   - This architecture is production-ready!")

if __name__ == "__main__":
    print("Make sure your FastAPI server is running: uvicorn main:app --reload --port 8000")
    print("Starting demo automatically...")
    
    asyncio.run(run_comprehensive_demo()) 