import asyncio
import websockets
from datetime import datetime


async def handle_message(message):
    now = datetime.now().isoformat()
    print(f"Received message at {now}. {message=}")


async def listen_to_server():
    try:
        async with websockets.connect("ws://localhost:8765") as websocket:
            while True:
                await asyncio.sleep(2)
                message = await websocket.recv()
                await handle_message(message)

    except websockets.ConnectionClosedOK:
        print("Server disconnected")


if __name__ == "__main__":
    asyncio.run(listen_to_server())
