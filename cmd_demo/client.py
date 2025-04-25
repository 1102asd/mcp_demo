import asyncio
import json
import sys

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main(tool_name=None, tool_params=None):
    # 定义服务端参数
    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
        env=None
    )

    async with stdio_client(server_params) as (stdio, write):
        async with ClientSession(stdio, write) as session:
            await session.initialize()

            # 列出可用工具
            tools_response = await session.list_tools()
            tool_names = [tool.name for tool in tools_response.tools]
            print("可用工具:", tool_names)

            if tool_name and tool_params and tool_name in tool_names:
                # 调用指定工具
                result = await session.call_tool(tool_name, tool_params)
                print(f"工具调用结果 ({tool_name}):", result.content[0].text)


if __name__ == "__main__":
    print(len(sys.argv))
    if len(sys.argv) >= 3:
        # 从命令行获取工具名和参数
        tool_name = sys.argv[1]
        params = sys.argv[2]
        print(tool_name, params)
        try:
            tool_params = json.loads(params)  # 参数为 JSON 格式
        except json.JSONDecodeError:
            print("参数必须为有效的 JSON 格式")
            sys.exit(1)
        asyncio.run(main(tool_name, tool_params))
    else:
        print("请提供工具名和参数，例如: python client.py add_numbers '{\"a\":5,\"b\":3}'")
