import asyncio
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter, ParseMode
from pyrogram.helpers import escape_markdown
from pyrogram.errors import FloodWait

from BrandrdXMusic.utils.database import get_assistant
from BrandrdXMusic import app
from BrandrdXMusic.utils.branded_ban import admin_filter

SPAM_CHATS = []


@app.on_message(
    filters.command(
        ["atag", "aall", "amention", "amentionall"], prefixes=["/", "@", ".", "#"]
    )
    & admin_filter
)
async def atag_all_useres(_, message):
    userbot = await get_assistant(message.chat.id)

    if message.chat.id in SPAM_CHATS:
        return await message.reply_text(
            "ᴛᴀɢɢɪɴɢ ᴘʀᴏᴄᴇss ᴀʟʀᴇᴀᴅʏ ʀᴜɴɴɪɴɢ!\nUse /acancel to stop."
        )

    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text(
            "**Usage:** `/aall your text here` or reply to a message with `/aall`"
        )
        return

    text = None
    if replied:
        text = replied.text
    else:
        text = message.text.split(None, 1)[1]

    SPAM_CHATS.append(message.chat.id)
    usernum = 0
    usertxt = ""

    async for m in app.get_chat_members(message.chat.id, filter=ChatMembersFilter.MEMBERS):
        if message.chat.id not in SPAM_CHATS:
            break
        if m.user.is_deleted:
            continue

        usernum += 1
        # Proper clickable mention
        usertxt += f"[{escape_markdown(m.user.first_name, version=2)}](tg://user?id={m.user.id}) "

        if usernum == 14:
            try:
                await userbot.send_message(
                    message.chat.id,
                    f"{text}\n\n{usertxt}",
                    disable_web_page_preview=True,
                    parse_mode=ParseMode.MARKDOWN
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
                message.chat.id,
                f"{text}\n\n{usertxt}",
                disable_web_page_preview=True,
                parse_mode=ParseMode.MARKDOWN
            )
        except FloodWait as e:
            await asyncio.sleep(e.value)

    try:
        SPAM_CHATS.remove(message.chat.id)
    except Exception:
        pass


@app.on_message(filters.command("acancel", prefixes=["/", "@", ".", "#"]) & admin_filter)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
        return await message.reply_text("✅ Tagging process stopped successfully!")

    else:
        return await message.reply_text("❌ No tagging process is currently running.")
