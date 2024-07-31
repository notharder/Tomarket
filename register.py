from hydrogram import Client
import asyncio

app_id = 13875777
api_hash = '28bac7e8ca985a86f48aadc28b1b3916'
sesi = input("enter number:")

async def register_sessions():
    app = Client(name=sesi, api_id=app_id, api_hash=api_hash, workdir="sessions/")
    await app.start()
    await app.stop()

asyncio.run(register_sessions())