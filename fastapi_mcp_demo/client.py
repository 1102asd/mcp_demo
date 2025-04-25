# client.py
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    server_params = StdioServerParameters(
        command="mcp-proxy",
        args=["http://localhost:8080/mcp"]
    )

    async with stdio_client(server_params) as (stream, write):
        async with ClientSession(stream, write) as session:
            await session.initialize()

            # 获取 tool 列表
            tools_response = await session.list_tools()
            print("可用工具:", [tool.name for tool in tools_response.tools])

            # 调用 add_number 工具
            result = await session.call_tool("add_number", {"a": 12, "b": 30})
            print("add_number 返回:", result.content[0].text)

if __name__ == "__main__":
    asyncio.run(main())
