#!/usr/bin/env python

# WS server example

import asyncio
import websockets

async def hello(websocket, path):
    data = await websocket.recv()
    print(f"<message from client: {data} <----------")

    greeting = f"message from server: {data}"

    await websocket.send(greeting)

start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
