#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import time


async def hello(n):
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        #name = input("What's your name? ")
        await websocket.send(f"msg[{n}]")
        greeting = await websocket.recv()
        print(f"----------> {greeting}")

num = 0
while True:
    asyncio.get_event_loop().run_until_complete(hello(num))
    num += 1
    time.sleep(0.5)
