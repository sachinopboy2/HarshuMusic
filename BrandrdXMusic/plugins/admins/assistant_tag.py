import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from BrandrdXMusic.utils.database import get_assistant
from BrandrdXMusic import app
from BrandrdXMusic.utils.branded_ban import admin_filter

# अब set रखा है (list की जगह)
SPAM_CHATS = set()


@app.on_message(
    filters.command(["atag", "aall", "amention", "amentionall"], prefixes=["/", "@", ".", "#"])
    & admin_filter
)
async def atag_all_users(_, message):
    chat_id = message.chat.id

    # अगर पहले से चालू है तो दोबारा allow मत करो
    if chat_id in SPAM_CHATS:
        return await message.reply_text(
            "⚠️ Tagging process already running!\n\nUse /acancel to stop it."
        )

    # Assistant (userbot) लो
    userbot = await get_assistant(chat_id)

    # अगर text नहीं दिया और reply भी नहीं किया तो error
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        return await message.reply_text(
            "❌ Please give some text to tag all!\n\nExample: `/atag Hello friends`"
        )

    # chat को active tagging में डालो
    SPAM_CHATS.add(chat_id)

    # अगर किसी message को reply किया है
    if replied:
        text = replied.text
    else:
        text = message.text.split(None, 1)[1]

    usernum = 0
    usertxt = ""

    try:
        async for m in app.get_chat_members(chat_id):
            if chat_id not in SPAM_CHATS:  # अगर बीच में cancel हो गया
                break

            if m.user.is_bot:  # बॉट को skip करो
                continue

            usernum += 1
            usertxt += f"[{m.user.first_name}](tg://user?id={m.user.id}) "

            if usernum == 14:  # हर 14 members पर message भेजो
                try:
                    await userbot.send_message(
                        chat_id,
                        f"{text}\n\n{usertxt}",
                        disable_web_page_preview=True,
                    )
                except FloodWait as e:
                    await asyncio.sleep(e.value)

                await asyncio.sleep(2)  # sleep ताकि flood न हो
                usernum = 0
                usertxt = ""

    except FloodWait as e:
        await asyncio.sleep(e.value)

    # काम पूरा होने के बाद remove
    SPAM_CHATS.discard(chat_id)


@app.on_message(filters.command(["acancel", "astop"], prefixes=["/", ".", "@", "#"]) & admin_filter)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        SPAM_CHATS.discard(chat_id)
        return await message.reply_text("✅ Tagging process stopped successfully!")
    else:
        return await message.reply_text("❌ No tagging process is running here.")
