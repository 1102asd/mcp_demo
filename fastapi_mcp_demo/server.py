# server.py
from fastapi import FastAPI, Request, Query
from fastapi_mcp import FastApiMCP

app = FastAPI()


@app.get("/add_number", operation_id="add_number")
async def add_number(request: Request, a: int = Query(...), b: int = Query(...)):
    return {"result": a + b}


# 挂载 MCP，暴露 /mcp 路径
mcp = FastApiMCP(app, include_operations=["add_number"])
mcp.mount(transport="sse", mount_path="/mcp")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(mcp.fastapi, host="0.0.0.0", port=8080)
