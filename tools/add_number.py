#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  : add_number.py
# @Time      : 2025/4/25 11:25
# @Author    : 何顺昌
# 定义一个工具：计算两个数字之和
from cmd_demo.server import mcp_server


@mcp_server.tool()
def add_numbers(a, b):
    try:
        """Add two numbers together."""
        return float(a) + float(b)
    except Exception as e:
        return f"Error: {e}"
