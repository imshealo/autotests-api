import asyncio
import websockets
from websockets import ServerConnection


async def echo(websocket: ServerConnection):
    async for message in websocket:
        response = (f"Получено сообщение пользователя: {message}\n"
                    f"{'-' * 60}")
        print(response)

        for _ in range(5):
            await websocket.send(response)


async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print(f"{'-' * 60}\n"
          "Websocket сервер запущен на ws://localhost:8765\n"
          f"{'-' * 60}")
    await server.wait_closed()


asyncio.run(main())
