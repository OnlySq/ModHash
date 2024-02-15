from pyrogram import Client, filters
from pyrogram.types import Message
from utils.misc import prefix, userbot_name, userbot_version, icon, user
from utils.scripts import modules_help, pretty_print_dict, get_file_id
from utils.cfgmaster import cfg
from pyrogram.handlers import MessageHandler
import os, sys, importlib
from pathlib import Path
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
        file_id = get_file_id(message)
        await message.edit(f"File ID: {file_id}")
    elif message.command[1] == 'pem_id':
        await message.edit(f'Premium emoji (<emoji id={message.entities[0].custom_emoji_id}>{message.command[2]}</emoji>) id: `{message.entities[0].custom_emoji_id}`')

async def restart(client: Client, message: Message):
    for path in Path('modules').rglob('*.py'):
        try:
            del path
        except: print(path, 'no')

    await message.edit('<emoji id=5388849303982716989>❤️</emoji> ModHash restarting...')
    python = sys.executable
    os.execl(python, python, *sys.argv)

async def reload(client: Client, message: Message):
    importlib.reload(message.text.split()[1])

async def set(client: Client, message: Message):
    try:
        txt = message.text.split()
        cfg.write(txt[1],txt[2],txt[3])
        await message.edit(f'New value for {txt[1]} {txt[2]} : {txt[3]}')
    except:
        await message.edit(f'Error while writing new value ({txt[1]} {txt[2]} : {txt[3]})')

async def read(client: Client, message: Message):
    txt = message.text.split()
    cfg.read(txt[1],txt[2])

# MessageHandler(,filters.command('',prefix) & filters.me)
handlers = [
    MessageHandler(help, filters.command('help',prefix) & filters.me),
    MessageHandler(get,filters.command('get',prefix) & filters.me),
    MessageHandler(restart,filters.command('restart',prefix) & filters.me),
    MessageHandler(set,filters.command('set',prefix) & filters.me),
    MessageHandler(read,filters.command('read',prefix) & filters.me)
]

# "":"",
modules_help[module_name] = {
    "help [module]":"View all modules commands",
    'get [file_id/pem_id]':"Get _ of message",
    'restart':"Restart userbot",
    'set [sec] [key] [val]':"Set value to config",
    'read [sec] [key]':"Read value from config"
}
