import asyncio
from pyrogram import filters
from pyrogram.errors import FloodWait
from BrandrdXMusic.utils.database import get_assistant
from BrandrdXMusic import app
from BrandrdXMusic.utils.branded_ban import admin_filter

# Active chats tracker
SPAM_CHATS = set()


# Manual escape_markdown for clickable mentions
def escape_markdown(text: str) -> str:
    escape_chars = "_*[]()~`>#+-=|{}.!:"
    for char in escape_chars:
        text = text.replace(char, f"\\{char}")
    return text


@app.on_message(
    filters.command(["atag", "aall", "amention", "amentionall"], prefixes=["/", "@", ".", "#"])
    & admin_filter
)
async def atag_all_users(_, message):
    chat_id = message.chat.id

    if chat_id in SPAM_CHATS:
        return await message.reply_text(
            "⚠️ Tagging process already running!\nUse /acancel to stop."
        )

    userbot = await get_assistant(chat_id)
    if not userbot:
        return await message.reply_text("❌ Assistant not available in this chat!")

    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        return await message.reply_text(
            "❌ Usage: `/atag your text here` or reply to a message with `/atag`"
        )

    text = replied.text if replied else message.text.split(None, 1)[1]

    SPAM_CHATS.add(chat_id)
    usernum = 0
    usertxt = ""

    try:
        async for m in app.get_chat_members(chat_id):
            if chat_id not in SPAM_CHATS:
                break

            if m.user.is_bot or m.user.is_deleted:
                continue

            usernum += 1
            usertxt += f"[{escape_markdown(m.user.first_name)}](tg://user?id={m.user.id}) "

            if usernum == 14:
                try:
                    await userbot.send_message(
                        chat_id,
                        f"{text}\n\n{usertxt}",
                        disable_web_page_preview=True,
                        parse_mode="Markdown"
                    )
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""

        # Send remaining mentions
        if usertxt:
            try:
                await userbot.send_message(
                    chat_id,
                    f"{text}\n\n{usertxt}",
                    disable_web_page_preview=True,
                    parse_mode="Markdown"
                )
            except FloodWait as e:
                await asyncio.sleep(e.value)

    except Exception as e:
        print("Error in atag:", e)

    SPAM_CHATS.discard(chat_id)


@app.on_message(filters.command(["acancel", "astop"], prefixes=["/", "@", ".", "#"]) & admin_filter)
async def cancel_tagging(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        SPAM_CHATS.discard(chat_id)
        return await message.reply_text("✅ Tagging process stopped successfully!")

    else:
        return await message.reply_text("❌ No tagging process is currently running.")
