import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


Bot = Client(
    "Info Bot",
    bot_token=os.environ.get("BOT_TOKEN"),
    api_id=int(os.environ.get("API_ID")),
    api_hash=os.environ.get("API_HASH")
)

START_TEXT = """<b>Hello {}
I am a Simple Telegram Info Bot, Click /help for more information<b>"""

HELP_TEXT = """💞 How to Use Me Harshith
• Send Me a file and reply by /mhinfo
• Send any Media to take its Details
• Reply /mhinfo to a Message to take Message Details
• Use /mhinfo Command to take your Details
• Use /mhid in Group or Channel to get Unique Telegram ID"""

ABOUT_TEXT = """--**About You From MHiNFoBoT**--
- **Bot :** `Info Bot`
- **Creator :** [Harshith](https://t.me/MutyalaHarshith)
- **Deploy OwN :** [Tutorial]()
- **Join :** [MHGcHaT](https://t.me/MHGcHaT)
- **Language :** [Python3](https://python.org)
- **Library :** [Pyrogram v1.2.0](https://pyrogram.org)
- **Server :** [Okteto](https://heroku.com)"""

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton(text="💞 Join", url=f"https://t.me/MutyalaHarshith")]])

@Bot.on_message(filters.private & filters.command("start"))
async def start(bot, update):
    await update.reply_text(
        text=START_TEXT.format(update.from_user.mention),
        disable_web_page_preview=True,
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
