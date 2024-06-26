#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async Comprehensions"""
    return [rand async for rand in async_generator()]
