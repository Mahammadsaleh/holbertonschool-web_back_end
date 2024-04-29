#!/usr/bin/env python3
"""Documentation"""
from typing import Union

Num = Union[int, float]

def to_kv(k: str, v: Num) -> tuple:
    """Documentation"""
    return (k, v**2)
