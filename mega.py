import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Info Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

START_TEXT = """<b>𝙷𝚎𝚕𝚕𝚘 {}
I ᴀᴍ Iᴅ Fᴇᴛᴄʜ Bᴏᴛ ʙʏ Hᴀʀsʜɪᴛʜ
I ᴄᴀɴ sʜᴏᴡ ʏᴏᴜʀ ɪᴅ & ɪɴғᴏ
Fᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴄʟɪᴄᴋ /help

Mᴜᴛʏᴀʟᴀ Hᴀʀsʜɪᴛʜ<b>"""

HELP_TEXT = """**💞 Hᴏᴡ ᴛᴏ Usᴇ 💞**
I ᴄᴀɴ ʜᴇʟᴘ ᴄᴀɴ Fᴇᴛᴄʜ ɪᴅ ᴏғ ʏᴏᴜ
Iᴅ ʜᴇʟᴘs ᴛᴏ ғɪɴᴅ ᴀɴʏ ᴏғ ʏᴏᴜ
Yᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ

Cʟɪᴄᴋ /ɪɴғᴏ ᴏғ ᴛᴏ ɢᴇᴛ 👇👇
• Iᴅ & ɪɴғᴏ
• Usᴇʀɴᴀᴍᴇ ᴏғ ʏᴏᴜ
• Jsᴏɴ ғɪʟᴇs ᴏғ ʏᴏᴜʀsᴇʟғ
• Tᴏ ɢᴇᴛ sᴛɪᴄᴋᴇʀ ɪᴅ ᴀɴᴅ Uɴɪǫᴜᴇ ID


Mᴜᴛʏᴀʟᴀ Hᴀʀsʜɪᴛʜ
"""

ABOUT_TEXT = """**Aʙᴏᴜᴛ Yᴏᴜsᴇʟғ**
• **Bᴏᴛ ɴᴀᴍᴇ:** [MHɪNFᴏBᴏT](https://t.me/MutyalaBoT)
• **Cʀᴇᴀᴛᴏʀ :** [Mᴜᴛʏᴀʟᴀ Hᴀʀsʜɪᴛʜ](https://t.me/MutyalaHarshith)
• **GɪᴛHᴜʙ** : [Fᴏʟʟᴏᴡ](https://GitHub.com/MutyalaHarshith)
• **Sᴏᴜʀᴄᴇ** : [MHɪNFᴏBᴏT](https://github.com/TeleGraMaN/MHiNFoBoT)
• **Sᴜᴘᴘᴏʀᴛ** : [ᴍʜɢᴄʜᴀᴛ](https://t.me/MHGcHaT)
• **Lᴀɴɢᴜᴀɢᴇ :** [Pʏᴛʜᴏɴ 𝟹](https://python.org)
• **Lɪʙʀᴀʀʏ :** [Pʏʀᴏɢʀᴀᴍ ᴠ𝟷.𝟸.𝟶](https://pyrogram.org)
• **Sᴇʀᴠᴇʀ :** [Hᴇʀᴏᴋᴜ](https://heroku.com)"""

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="💞 Join", url=f"https://t.me/MutyalaHarshith"),
                                 InlineKeyboardButton(text="Support", url=f"https://t.me/MHGcHaT")],
                                [InlineKeyboardButton(text="Share BoT", url=f"https://t.me/share/url?url=https%3A//t.me/MutyalaBoT"),
                                 InlineKeyboardButton(text="Group", url=f"http://t.me/MutyalaBoT?startgroup=true")]])

@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    await update.reply_text(
        photo="https://telegra.ph/file/236794ce4bb2213eaae1e.jpg",
        caption=START_TEXT.format(update.from_user.mention),
        reply_markup=BUTTONS
    )


@Bot.on_message(filters.private & filters.command("help"))
async def help(bot, update):
    await update.reply_text(
        text=HELP_TEXT,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


@Bot.on_message(filters.private & filters.command("about"))
async def about(bot, update):
    await update.reply_text(
        text=ABOUT_TEXT,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


@Bot.on_message(filters.private & filters.command("mhinfo"))
async def info(bot, update):
    
    text = f"""--**Information from Harshith**--
**💞 First Name :** {update.from_user.first_name}
**😎 Your Second Name :** {update.from_user.last_name if update.from_user.last_name else 'None'}
**🥳 Your Username :** {update.from_user.username}
**😜 Your Telegram ID :** {update.from_user.id}
**🤫 Your Profile Link :** {update.from_user.mention}"""
    
    await update.reply_text(        
        text=text,
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )


@Bot.on_message(filters.private & filters.command("mhid"))
async def id(bot, update):
    await update.reply_text(        
        text=f"💞 **Your Telegram ID :** {update.from_user.id}",
        disable_web_page_preview=True,
        reply_markup=BUTTONS
    )

@Bot.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")


@Bot.on_message(filters.command(["json", 'mhjs', 'showjson']))
async def jsonify(_, message):
    the_real_message = None
    reply_to_id = None

    if message.reply_to_message:
        the_real_message = message.reply_to_message
    else:
        the_real_message = message
    try:
        pk = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝙲𝙻𝙾𝚂𝙴",
                        callback_data="close_data"
                    )
                ]
            ]
        )
        await message.reply_text(f"<code>{the_real_message}</code>", reply_markup=pk, quote=True)
    except Exception as e:
        with open("json.text", "w+", encoding="utf8") as out_file:
            out_file.write(str(the_real_message))
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝙲𝙻𝙾𝚂𝙴",
                        callback_data="close_data"
                    )
                ]
            ]
        )
        await message.reply_document(
            document="json.text",
            caption=str(e),
            disable_notification=True,
            quote=True,
            reply_markup=reply_markup
        )            
        os.remove("json.text")

print("Bot Started!!! Now Join on @MutyalaHarshith")
Bot.run()
