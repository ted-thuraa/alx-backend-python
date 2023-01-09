#!/usr/bin/env python3
'''task 0 syntax
'''

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    '''waits for some seconds
    '''
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait