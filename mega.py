import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from telegraph import upload_file

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

[Mᴜᴛʏᴀʟᴀ Hᴀʀsʜɪᴛʜ](https://t.me/MutyalaHarshith)<b>"""

HELP_TEXT = """**💞 Hᴏᴡ ᴛᴏ Usᴇ 💞**
I ᴄᴀɴ ʜᴇʟᴘ ᴄᴀɴ Fᴇᴛᴄʜ ɪᴅ ᴏғ ʏᴏᴜ
Iᴅ ʜᴇʟᴘs ᴛᴏ ғɪɴᴅ ᴀɴʏ ᴏғ ʏᴏᴜ
Yᴏᴜ ᴄᴀɴ ᴀʟsᴏ ᴀᴅᴅ ᴛᴏ ɢʀᴏᴜᴘ

Cʟɪᴄᴋ /ɪɴғᴏ ᴏғ ᴛᴏ ɢᴇᴛ 👇👇
• Iᴅ & ɪɴғᴏ
• Usᴇʀɴᴀᴍᴇ ᴏғ ʏᴏᴜ
• Jsᴏɴ ғɪʟᴇs ᴏғ ʏᴏᴜʀsᴇʟғ
• Tᴏ ɢᴇᴛ sᴛɪᴄᴋᴇʀ ɪᴅ ᴀɴᴅ Uɴɪǫᴜᴇ ID


[Mᴜᴛʏᴀʟᴀ Hᴀʀsʜɪᴛʜ](https://t.me/MutyalaHarshith)
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

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="💞 Join", url=f"https://t.me/MutyalaHarshith")],
                                [InlineKeyboardButton(text="HoME", callback_data='home'),
                                 InlineKeyboardButton(text="about", callback_data='about'),
                                 InlineKeyboardButton(text="Group", url=f"http://t.me/MutyalaBoT?startgroup=true")]])

STRBUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="💞 Add Me To Group 💞", url=f"http://t.me/MutyalaBoT?startgroup=true")],
                                [InlineKeyboardButton(text="🥳 Channel", url=f"https://t.me/MutyalaHarshith),
                                 InlineKeyboardButton(text="🤪 Support", url=f"https://t.me/MHGCHAT)]])
                                [InlineKeyboardButton(text="😂 Help", callback_data='help'),
                                 InlineKeyboardButton(text="😜 About", callback_data='about')]])


@Bot.on_callback_query()
async def cb_handler(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT.format(update.from_user.mention),
            reply_markup=BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            reply_markup=BUTTONS,
            disable_web_page_preview=True
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            reply_markup=BUTTONS,
            disable_web_page_preview=True
        )
    else:
        await update.message.delete()


@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    await update.reply_photo(
        photo="https://telegra.ph/file/236794ce4bb2213eaae1e.jpg",
        caption=START_TEXT.format(update.from_user.mention),
        reply_markup=STRBUTTONS
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
**🤫 Your Profile Link :** {update.from_user.mention}
** Bio :** {update.from_user.mention}
** Lang code :** {update.from_user.language_code}
** Language :** {update.from_user.first_name} """
    
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



@Bot.on_message(filters.command("telegraph"))
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.reply("Reply to a supported media file")
        return
    if not (
        (replied.photo and replied.photo.file_size <= 5242880)
        or (replied.animation and replied.animation.file_size <= 5242880)
        or (
            replied.video
            and replied.video.file_name.endswith(".mp4")
            and replied.video.file_size <= 5242880
        )
        or (
            replied.document
            and replied.document.file_name.endswith(
                (".jpg", ".jpeg", ".png", ".gif", ".mp4"),
            )
            and replied.document.file_size <= 5242880
        )
    ):
        await message.reply("Not supported!")
        return
    download_location = await client.download_media(
        message=message.reply_to_message,
        file_name="root/downloads/",
    )
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.reply(message, text=document)
    else:
        await message.reply(
            f"**Uploaded To Telegraph!\n\n👉 https://telegra.ph{response[0]}**  [Your link](https://telegra.ph{response[0]}) ",
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)

   


print("✨✨ Start BoT By Created Mutyala Harshith ✨✨")
Bot.run()
