#!/usr/bin/env python3
"""
Simple demo client for the FastAPI MCP Server
"""
import subprocess
import json
import time

def demo_mcp_server():
    """Demo the MCP server by running it and testing basic functionality"""
    
    print("Starting MCP Demo Client...")
    print("Make sure your FastAPI server is running on port 8000!")
    print("=" * 50)
    
    # Start the MCP server as a subprocess
    process = subprocess.Popen(
        ["python", "mcp_server.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    try:
        # Give it a moment to start
        time.sleep(1)
        
        # Check if process is still running
        if process.poll() is None:
            print("MCP Server started successfully!")
            print("The server is now ready to accept MCP client connections.")
            print("\nYou can test it with any MCP-compatible client.")
            print("\nTo test manually, you can:")
            print("1. Use an MCP client library in another script")
            print("2. Use the MCP CLI tools")
            print("3. Connect from an IDE that supports MCP")
        else:
            # Get error output
            stderr_output = process.stderr.read() if process.stderr else "No error output available"
            print("MCP Server failed to start:")
            print(stderr_output)
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Clean up
        process.terminate()
        process.wait()
        print("\nDemo completed.")

if __name__ == "__main__":
    demo_mcp_server() 