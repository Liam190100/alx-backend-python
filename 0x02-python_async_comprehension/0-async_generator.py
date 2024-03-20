#!/usr/bin/env python3
'''
Task module.
'''
from typing import Generator
import asyncio
import random


async def async_generator() -> Generator[float, None, None]:
    '''Generate sequence of 10 numbers.
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
