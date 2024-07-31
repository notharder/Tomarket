import os
import glob
import asyncio
from urllib.parse import unquote
from pyrogram import Client
from pyrogram.raw.functions.messages import RequestWebView

# Define your Telegram API credentials
api_id = 29059866
api_hash = "98a6f543241b1ece2e6f7f94ab829ae9"

# Function to get session names
def get_session_names() -> list[str]:
    session_names = glob.glob('sessions/*.session')
    session_names = [os.path.splitext(os.path.basename(file))[0] for file in session_names]
    return session_names

# Function to get Telegram data
async def get_tgdata(sesi):
    app = Client(
        name=sesi,
        api_id=api_id,
        api_hash=api_hash,
        workdir="sessions/"
    )
    await app.connect()
    peer = await app.resolve_peer('Tomarket_ai_bot')
    webview = await app.invoke(RequestWebView(
        peer=peer,
        bot=peer,
        from_bot_menu=False,
        platform='Android',
        url='https://mini-app.tomarket.ai/'
    ))
    query_id = webview.url.split("#tgWebAppData=")[1].split("&tgWebAppVersion=")[0]
    query_id_decoded = unquote(query_id)
    await app.disconnect()
    return query_id_decoded

# Function to fill data.txt
async def fill_data_txt():
    print("Filling data.txt with query_ids...")
    with open('data.txt', 'w') as file:
        for sesi in get_session_names():
            query_id = await get_tgdata(sesi)
            print(f"Adding query_id for session {sesi}")
            file.write(query_id + "\n")
            await asyncio.sleep(2)
    print("data.txt has been filled successfully")

# Run the fill_data_txt function
if __name__ == "__main__":
    asyncio.run(fill_data_txt())
