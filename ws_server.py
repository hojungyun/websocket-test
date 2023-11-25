import asyncio
from datetime import datetime
import websockets
from websockets.legacy.server import WebSocketServerProtocol


async def show_time(websocket: WebSocketServerProtocol):
    client_id = websocket.id.hex[:4]
    print(f"Client connected! {client_id=}")
    try:
        n = 0
        while True:
            n += 1
            await asyncio.sleep(1)

            now = datetime.now().isoformat()
            if 10 < n < 15:
                message = f"[{n}] Call from customer at {now}"
            else:
                message = f"[{n}] {now}"

            print(f"[{client_id}] Sending message to ws client. {message=}")
            await websocket.send(message)

    except websockets.ConnectionClosedOK:
        print("Client disconnected")


async def main():
    async with websockets.serve(show_time, "localhost", 8765):
        print("websocket started. It will send msg once client is connected.")
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())
