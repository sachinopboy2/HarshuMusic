from BrandrdXMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []

EMOJI = [ "🦋🦋🦋🦋🦋",
          "🧚🌸🧋🍬🫖",
          "🥀🌷🌹🌺💐",
          "🌸🌿💮🌱🌵",
          "❤️💚💙💜🖤",
          "💓💕💞💗💖",
          "🌸💐🌺🌹🦋",
          "🍔🦪🍛🍲🥗",
          "🍎🍓🍒🍑🌶️",
          "🧋🥤🧋🥛🍷",
          "🍬🍭🧁🎂🍡",
          "🍨🧉🍺☕🍻",
          "🥪🥧🍦🍥🍚",
          "🫖☕🍹🍷🥛",
          "☕🧃🍩🍦🍙",
          "🍁🌾💮🍂🌿",
          "🌨️🌥️⛈️🌩️🌧️",
          "🌷🏵️🌸🌺💐",
          "💮🌼🌻🍀🍁",
          "🧟🦸🦹🧙👸",
          "🧅🍠🥕🌽🥦",
          "🐷🐹🐭🐨🐻‍❄️",
          "🦋🐇🐀🐈🐈‍⬛",
          "🌼🌳🌲🌴🌵",
          "🥩🍋🍐🍈🍇",
          "🍴🍽️🔪🍶🥃",
          "🕌🏰🏩⛩️🏩",
          "🎉🎊🎈🎂🎀",
          "🪴🌵🌴🌳🌲",
          "🎄🎋🎍🎑🎎",
          "🦅🦜🕊️🦤🦢",
          "🦤🦩🦚🦃🦆",
          "🐬🦭🦈🐋🐳",
          "🐔🐟🐠🐡🦐",
          "🦩🦀🦑🐙🦪",
          "🐦🦂🕷️🕸️🐚",
          "🥪🍰🥧🍨🍨",
          " 🥬🍉🧁🧇",
        ]
        ####
        
SHAYRI = [
    "🌸**तुम्हारी मुस्कान मेरे दिन की सबसे खूबसूरत शुरुआत है।**🌸\n\n**🥀Tumhari muskaan mere din ki sabse khoobsurat shuruaat hai.🥀**",
    "🌸**तेरे ख्यालों में खो जाना मेरी सबसे बड़ी आदत है।**🌸\n\n**🥀Tere khayalon me kho jana meri sabse badi aadat hai.🥀**",
    "🌸**तुम मेरी हर तन्हाई में साथ होते हो।**🌸\n\n**🥀Tum meri har tanhai me saath hote ho.🥀**",
    "🌸**तेरे बिना मेरी दुनिया सुनसान लगती है।**🌸\n\n**🥀Tere bina meri duniya sunsaan lagti hai.🥀**",
    "🌸**तुम मेरे दिल की सबसे प्यारी याद हो।**🌸\n\n**🥀Tum mere dil ki sabse pyari yaad ho.🥀**",
    "🌸**तेरी हर बात मेरे दिल को छू जाती है।**🌸\n\n**🥀Teri har baat mere dil ko chu jati hai.🥀**",
    "🌸**तुमसे मिलने के बाद सब कुछ सुंदर लगने लगा।**🌸\n\n**🥀Tumse milne ke baad sab kuch sundar lagne laga.🥀**",
    "🌸**तेरी हँसी मेरे लिए सबसे बड़ी खुशी है।**🌸\n\n**🥀Teri hansi mere liye sabse badi khushi hai.🥀**",
    "🌸**तुम मेरे दिल का सबसे कीमती खजाना हो।**🌸\n\n**🥀Tum mere dil ka sabse keemti khazana ho.🥀**",
    "🌸**तुम्हारे साथ बिताया हर पल मेरी जिंदगी का अनमोल हिस्सा है।**🌸\n\n**🥀Tumhare saath bitaya har pal meri zindagi ka anmol hissa hai.🥀**",
    "🌸**तुम मेरे सपनों की सबसे खूबसूरत तस्वीर हो।**🌸\n\n**🥀Tum mere sapno ki sabse khoobsurat tasveer ho.🥀**",
    "🌸**तेरी यादें मेरे दिल में हमेशा जीवित रहती हैं।**🌸\n\n**🥀Teri yaadein mere dil me hamesha jeevit rehti hain.🥀**",
    "🌸**तेरी आवाज़ सुनकर मेरा दिल खिल उठता है।**🌸\n\n**🥀Teri awaaz sunkar mera dil khil uthta hai.🥀**",
    "🌸**तुम मेरी दुनिया की सबसे बड़ी खुशी हो।**🌸\n\n**🥀Tum meri duniya ki sabse badi khushi ho.🥀**",
    "🌸**तेरा हाथ मेरे हाथ में हो तो हर डर गायब हो जाता है।**🌸\n\n**🥀Tera haath mere haath me ho to har dar gayab ho jata hai.🥀**",
    "🌸**तुम मेरी तन्हाई की सबसे प्यारी दोस्ती हो।**🌸\n\n**🥀Tum meri tanhai ki sabse pyari dosti ho.🥀**",
    "🌸**तेरी आँखों में मैंने अपना आसमान देखा है।**🌸\n\n**🥀Teri aankhon me maine apna aasman dekha hai.🥀**",
    "🌸**तुम मेरी जिंदगी का सबसे खूबसूरत एहसास हो।**🌸\n\n**🥀Tum meri zindagi ka sabse khoobsurat ehsaas ho.🥀**",
    "🌸**तेरे बिना मेरी रातें अधूरी हैं।**🌸\n\n**🥀Tere bina meri raatein adhuri hain.🥀**",
    "🌸**तुम मेरे हर दिन की सबसे प्यारी शुरुआत हो।**🌸\n\n**🥀Tum mere har din ki sabse pyari shuruaat ho.🥀**",
    "🌸**तेरे ख्यालों में खो जाना मेरी आदत बन गई है।**🌸\n\n**🥀Tere khayalon me kho jana meri aadat ban gayi hai.🥀**",
    "🌸**तुम मेरे दिल की धड़कन हो।**🌸\n\n**🥀Tum mere dil ki dhadkan ho.🥀**",
    "🌸**तेरी मुस्कान मेरे लिए सबसे बड़ी ताकत है।**🌸\n\n**🥀Teri muskaan mere liye sabse badi taqat hai.🥀**",
    "🌸**तुम मेरे हर दुःख में साथ हो।**🌸\n\n**🥀Tum mere har dukh me saath ho.🥀**",
    "🌸**तेरी मोहब्बत मेरे लिए सबसे बड़ा तोहफ़ा है।**🌸\n\n**🥀Teri mohabbat mere liye sabse bada tohfa hai.🥀**",
    "🌸**तुम मेरी जिंदगी का सबसे हसीन हिस्सा हो।**🌸\n\n**🥀Tum meri zindagi ka sabse haseen hissa ho.🥀**",
    "🌸**तेरे बिना सब कुछ अधूरा लगता है।**🌸\n\n**🥀Tere bina sab kuch adhura lagta hai.🥀**",
    "🌸**तुम मेरी हर खुशी का कारण हो।**🌸\n\n**🥀Tum meri har khushi ka kaaran ho.🥀**",
    "🌸**तेरी यादें मेरे दिल को सुकून देती हैं।**🌸\n\n**🥀Teri yaadein mere dil ko sukoon deti hain.🥀**",
    "🌸**तुम मेरी हर सुबह की सबसे प्यारी शुरुआत हो।**🌸\n\n**🥀Tum meri har subah ki sabse pyari shuruaat ho.🥀**",
    "🌸**तेरे साथ हर पल मेरे लिए खास है।**🌸\n\n**🥀Tere saath har pal mere liye khaas hai.🥀**",
    "🌸**तुम मेरी हर तन्हाई को रोशन कर देते हो।**🌸\n\n**🥀Tum meri har tanhai ko roshan kar dete ho.🥀**",
    "🌸**तुम मेरी सबसे बड़ी खुशी हो।**🌸\n\n**🥀Tum meri sabse badi khushi ho.🥀**",
    "🌸**तेरे बिना मेरा दिल खाली सा लगता है।**🌸\n\n**🥀Tere bina mera dil khaali sa lagta hai.🥀**",
    "🌸**तुम मेरी जिंदगी की सबसे हसीन याद हो।**🌸\n\n**🥀Tum meri zindagi ki sabse haseen yaad ho.🥀**",
    "🌸**तेरी मोहब्बत मेरे लिए अनमोल है।**🌸\n\n**🥀Teri mohabbat mere liye anmol hai.🥀**",
    "🌸**तुम मेरी दुनिया को खूबसूरत बनाते हो।**🌸\n\n**🥀Tum meri duniya ko khoobsurat banate ho.🥀**",
    "🌸**तेरी नज़रों में मैंने अपनी खुशियाँ देखी हैं।**🌸\n\n**🥀Teri nazron me maine apni khushiyan dekhi hain.🥀**",
    "🌸**तुम मेरी हर दुआ में शामिल हो।**🌸\n\n**🥀Tum meri har dua me shamil ho.🥀**",
    "🌸**तेरे साथ बिताया हर पल मेरे लिए यादगार है।**🌸\n\n**🥀Tere saath bitaya har pal mere liye yaadgar hai.🥀**",
    "🌸**तुम मेरी जिंदगी का सबसे कीमती एहसास हो।**🌸\n\n**🥀Tum meri zindagi ka sabse keemti ehsaas ho.🥀**",
    "🌸**तेरी हँसी मेरे दिल को खुश कर देती है।**🌸\n\n**🥀Teri hansi mere dil ko khush kar deti hai.🥀**",
    "🌸**तुम मेरे लिए सबसे अनमोल हो।**🌸\n\n**🥀Tum mere liye sabse anmol ho.🥀**",
    "🌸**तेरी यादें मुझे हर पल मुस्कुराती हैं।**🌸\n\n**🥀Teri yaadein mujhe har pal muskurati hain.🥀**",
    "🌸**तुम मेरे दिल की सबसे प्यारी धड़कन हो।**🌸\n\n**🥀Tum mere dil ki sabse pyari dhadkan ho.🥀**",
    "🌸**तेरे बिना मेरी तन्हाई अधूरी है।**🌸\n\n**🥀Tere bina meri tanhai adhuri hai.🥀**",
    "🌸**तुम मेरे लिए सबसे खास इंसान हो।**🌸\n\n**🥀Tum mere liye sabse khaas insaan ho.🥀**",
    "🌸**तेरी हर बात मेरे दिल को छू जाती है।**🌸\n\n**🥀Teri har baat mere dil ko chu jati hai.🥀**",
    "🌸**तुम मेरी जिंदगी का सबसे हसीन अहसास हो।**🌸\n\n**🥀Tum meri zindagi ka sabse haseen ehsaas ho.🥀**",
    "🌸**तेरे बिना मेरी दुनिया बेरंग है।**🌸\n\n**🥀Tere bina meri duniya berang hai.🥀**"
]
# Command
    


@app.on_message(filters.command(["shayari" ], prefixes=["/", "@", "#"]))
async def mentionall(client, message):
    chat_id = message.chat.id
    if message.chat.type == ChatType.PRIVATE:
        return await message.reply("𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 𝐎𝐧𝐥𝐲 𝐅𝐨𝐫 𝐆𝐫𝐨𝐮𝐩𝐬.")

    is_admin = False
    try:
        participant = await client.get_chat_member(chat_id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 . ")

    if message.reply_to_message and message.text:
        return await message.reply("/shayaril  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ")
    elif message.text:
        mode = "text_on_cmd"
        msg = message.text
    elif message.reply_to_message:
        mode = "text_on_reply"
        msg = message.reply_to_message
        if not msg:
            return await message.reply("/shayari  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ...")
    else:
        return await message.reply("/shayari  𝐓𝐲𝐩𝐞 𝐋𝐢𝐤𝐞 𝐓𝐡𝐢𝐬 / 𝐑𝐞𝐩𝐥𝐲 𝐀𝐧𝐲 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 𝐍𝐞𝐱𝐭 𝐓𝐢𝐦𝐞 ..")
    if chat_id in spam_chats:
        return await message.reply("𝐏𝐥𝐞𝐚𝐬𝐞 𝐀𝐭 𝐅𝐢𝐫𝐬𝐭 𝐒𝐭𝐨𝐩 𝐑𝐮𝐧𝐧𝐢𝐧𝐠 𝐏𝐫𝐨𝐜𝐞𝐬𝐬 ...")
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.get_chat_members(chat_id):
        if not chat_id in spam_chats:
            break
        if usr.user.is_bot:
            continue
        usrnum += 1
        usrtxt += "<a href='tg://user?id={}'>{}</a>".format(usr.user.id, usr.user.first_name)

        if usrnum == 1:
            if mode == "text_on_cmd":
                txt = f"{usrtxt} {random.choice(SHAYRI)}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(f"[{random.choice(EMOJI)}](tg://user?id={usr.user.id})")
            await asyncio.sleep(4)
            usrnum = 0
            usrtxt = ""
    try:
        spam_chats.remove(chat_id)
    except:
        pass


#

@app.on_message(filters.command(["cancelshayari", "shayarioff"]))
async def cancel_spam(client, message):
    if not message.chat.id in spam_chats:
        return await message.reply("𝐂𝐮𝐫𝐫𝐞𝐧𝐭𝐥𝐲 𝐈'𝐦 𝐍𝐨𝐭 ..")
    is_admin = False
    try:
        participant = await client.get_chat_member(message.chat.id, message.from_user.id)
    except UserNotParticipant:
        is_admin = False
    else:
        if participant.status in (
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ):
            is_admin = True
    if not is_admin:
        return await message.reply("𝐘𝐨𝐮 𝐀𝐫𝐞 𝐍𝐨𝐭 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐛𝐲, 𝐎𝐧𝐥𝐲 𝐀𝐝𝐦𝐢𝐧𝐬 𝐂𝐚𝐧 𝐓𝐚𝐠 𝐌𝐞𝐦𝐛𝐞𝐫𝐬.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("👣 𝐁𝐑𝐀𝐍𝐃𝐄𝐃 𝐒𝐇𝐀𝐘𝐀𝐑𝐈 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐒𝐓𝐎𝐏𝐏𝐄𝐃 💗")
