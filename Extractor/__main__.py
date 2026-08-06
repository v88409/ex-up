import os
import asyncio
import importlib
import threading
from pyrogram import idle
from Extractor.modules import ALL_MODULES
from web import web_app

loop = asyncio.get_event_loop()


async def sumit_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("Extractor.modules." + all_module)

    print("» ʙᴏᴛ ᴅᴇᴘʟᴏʏ sᴜᴄᴄᴇssғᴜʟʟʏ ✨ 🎉")
    await idle()
    print("» ɢᴏᴏᴅ ʙʏᴇ ! sᴛᴏᴘᴘɪɴɢ ʙᴏᴛ.")


def run_web():
    web_app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))


if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()
    loop.run_until_complete(sumit_boot())
