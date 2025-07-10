#!/usr/bin/env python3
"""
Test script to verify the FastAPI endpoints that the MCP server calls
"""
import httpx
import asyncio

async def test_fastapi_endpoints():
    """Test the FastAPI endpoints directly"""
    
    print("Testing FastAPI endpoints that the MCP server uses...")
    print("=" * 50)
    
    async with httpx.AsyncClient() as client:
        # Test health endpoint
        print("\n--- Testing /health endpoint ---")
        try:
            response = await client.get("http://localhost:8000/health")
            response.raise_for_status()
            print(f"✅ Health check successful: {response.json()}")
        except Exception as e:
            print(f"❌ Health check failed: {e}")
        
        # Test products endpoint
        print("\n--- Testing /products endpoint ---")
        try:
            response = await client.get("http://localhost:8000/products", params={
                "channel_id": 1,
                "catalog_id": 2
            })
            response.raise_for_status()
            print(f"✅ Products search successful: {response.json()}")
        except Exception as e:
            print(f"❌ Products search failed: {e}")

if __name__ == "__main__":
    print("Make sure your FastAPI server is running on port 8000!")
    asyncio.run(test_fastapi_endpoints()) 