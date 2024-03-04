import asyncio
from pyrogram import Client, filters

API_ID = 00000000
API_HASH = ""

app = Client("my_account", API_ID, API_HASH)

@app.on_message(filters.channel & (filters.text | filters.photo))
async def main(client, message):
    post = await app.get_discussion_message(message.chat.id, message.id)
    await post.reply("Крутяк!")
    print(client, message)

app.run()
