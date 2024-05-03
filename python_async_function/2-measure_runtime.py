#!/usr/bin/env python3
"""Documentation"""
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Wait for a random delay between 0 and max_delay"""
    start = asyncio.get_event_loop().time()
    await wait_n(n, max_delay)
    end = asyncio.get_event_loop().time()
    return (end - start) / n
