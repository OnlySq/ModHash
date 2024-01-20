from pyrogram import Client, filters
from pyrogram.types import Message
from utils.misc import prefix, userbot_name, userbot_version, icon, user
from utils.scripts import modules_help, pretty_print_dict
from pyrogram.handlers import MessageHandler
module_name = 'System'

async def help(client: Client, message: Message):
    try:
        if message.command[1] != None:
            if message.command[1] == 'list':
                await message.edit(f'`╔ Core\n{pretty_print_dict(modules_help)}`\n\nДля вывода помощи по определенному модулю запросите {prefix}help [модуль]')
            else:
                await message.edit(f'`╔ {message.command[1]}\n{pretty_print_dict(modules_help[message.command[1]])}`')
    except:
        await message.delete()
        await client.send_photo(message.chat.id,
                                icon,
                                f'<emoji id=5332598203206349551>🌟</emoji> **{userbot_name}**\n{"=-"*10}=\n<emoji id=5213214428958306222>🛠️</emoji> Версия: `{userbot_version}`\n<emoji id=5352979721401419161>⭐</emoji> Premium: {"Активен" if user.me.is_premium else "Неактивен"}\n{"=-"*10}=\n<emoji id=5213297128553590938>▶️</emoji> Помощь по всем модулям: `{prefix}help list`\n<emoji id=5213297128553590938>▶️</emoji> Помощь по модулю: `{prefix}help [модуль]`\n{"=-"*10}=\n<emoji id=5213333038775151099>🧑‍💻</emoji> Developer: @NoBanOnlyZXC'
                                )

async def get(client: Client, message: Message):
    if message.command[1] == 'file_id':
        reply = message.reply_to_message
        if reply is not None:
            if reply.audio:
                file_id = reply.audio.file_id
            elif reply.document:
                file_id = reply.document.file_id
            elif reply.photo:
                file_id = reply.photo.file_id
            elif reply.sticker:
                file_id = reply.sticker.file_id
            elif reply.video:
                file_id = reply.video.file_id
            elif reply.animation:
                file_id = reply.animation.file_id
            elif reply.voice:
                file_id = reply.voice.file_id
            elif reply.video_note:
                file_id = reply.video_note.file_id
            else:
                file_id = None
        else:
            file_id = None
        await message.edit(f"File ID: {file_id}")
    elif message.command[1] == 'pem_id':
        await message.edit(f'Premium emoji (<emoji id={message.entities[0].custom_emoji_id}>{message.command[2]}</emoji>) id: `{message.entities[0].custom_emoji_id}`')

# MessageHandler(,filters.command('',prefix) & filters.me)
handlers = [
    MessageHandler(help, filters.command('help',prefix) & filters.me),
    MessageHandler(get,filters.command('get',prefix) & filters.me)
]

# "":"",
modules_help[module_name] = {
    "help [module]":"View all modules commands"
}