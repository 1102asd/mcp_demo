from mcp.server.fastmcp import FastMCP

# 创建一个 MCP 服务端实例，命名为 "SimpleServer"
mcp_server = FastMCP("SimpleServer")

from tools import *


# 定义一个资源：返回一个简单的问候语
@mcp_server.resource("greeting://hello")
def get_greeting() -> str:
    """Return a static greeting message."""
    return "Hello from MCP Server!"


# 运行服务端
if __name__ == "__main__":
    mcp_server.run(transport='sse')
