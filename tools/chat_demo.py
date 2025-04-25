#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : chat_demo.py
# @Time      : 2025/4/25 11:23
# @Author    : 何顺昌
from openai import AsyncOpenAI

from cmd_demo.server import mcp_server


@mcp_server.tool()
async def stream_completion(prompt: str):
    """流式文本生成"""
    client = AsyncOpenAI()

    async with client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            stream=True
    ) as stream:
        async for chunk in stream:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content
