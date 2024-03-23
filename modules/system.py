from pyrogram import Client, filters
from pyrogram.types import Message
from utils.misc import prefix, userbot_name, userbot_version, icon, user, success_modules, success_modules_list, failed_modules, failed_modules_list
from utils.scripts import modules_help, pretty_print_dict, get_file_id
from utils.cfgmaster import cfg
from pyrogram.handlers import MessageHandler
import os, sys, importlib, re
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
        temp = ''+f'{success_modules} {failed_modules}'
        if not success_modules == 0:
            temp = temp+f'\n<emoji id=5213470220030585409>⚙️</emoji> Загружено {success_modules} модулей:\n{success_modules_list}'
        if not failed_modules == 0:
            temp = temp+f'\n<emoji id=5213470220030585409>⚙️</emoji> Не загружено {failed_modules} модулей:\n{failed_modules_list}'
        await client.send_photo(message.chat.id,
                                icon,
f'''<emoji id=5332598203206349551>🌟</emoji> **{userbot_name}**
{"=-"*10}=
<emoji id=5213214428958306222>🛠️</emoji> Версия: `{userbot_version}`
<emoji id=5352979721401419161>⭐</emoji> Premium: {"Активен" if user.me.is_premium else "Неактивен"}{temp}
{"=-"*10}=
<emoji id=5213297128553590938>▶️</emoji> Помощь по всем модулям: `{prefix}help list`
<emoji id=5213297128553590938>▶️</emoji> Помощь по модулю: `{prefix}help [модуль]`\n{"=-"*10}=
<emoji id=5213333038775151099>🧑‍💻</emoji> Developer: @NoBanOnlyZXC'''
                                )

async def get(client: Client, message: Message):
    if message.command[1] == 'file_id':
        file_id = get_file_id(message)
        await message.edit(f"File ID: {file_id}")
    elif message.command[1] == 'pem_id':
        await message.edit(f'Premium emoji (<emoji id={message.entities[0].custom_emoji_id}>{message.command[2]}</emoji>) id: `{message.entities[0].custom_emoji_id}`')
    elif message.command[1] == 'all':
        await message.edit(str(message.reply_to_message)[:4000])
        print(message.reply_to_message)
    elif message.command[1] == 'rml':
        await message.edit('Links from buttons:')
        for links in message.reply_to_message.reply_markup.inline_keyboard[0]:
            await client.send_message(message.chat.id, '@'+str(links.url.rsplit('/',1)[1]))
        matches = re.findall(r'@\w+', message.reply_to_message.text)
        if matches:
            await client.send_message(message.chat.id, 'Links from text:')
            for match in matches:
                await client.send_message(message.chat.id, match)

async def restart(client: Client, message: Message):
    for path in Path('modules').rglob('*.py'):
        try:
            del path
        except: print(path, 'no')

    await message.edit('<emoji id=5388849303982716989>⚡</emoji> ModHash перезапускается...')
    python = sys.executable
    if '-noacc' in message.text:
        os.execl(python, python, *sys.argv)
    else:
        os.execl(python, python, *sys.argv, 'restart', user.account)

async def reload(client: Client, message: Message):
    importlib.reload(message.text.split()[1])
    await message.edit(f'<emoji id=5388849303982716989>⚡</emoji> Module {message.text.split()[1]} reloaded')

async def set(client: Client, message: Message):
    try:
        txt = message.text.split()
        if len(txt) < 3:
            txt = ['settings',txt[1],txt[2]]
        cfg.write(txt[1],txt[2],txt[3])
        await message.edit(f'Новое значение в {txt[1]} {txt[2]}: {txt[3]}')
    except Exception as e:
        await message.edit(f'Не получилось изменить значение ({txt[1]} {txt[2]} : {txt[3]})\n{e}')

async def read(client: Client, message: Message):
    txt = message.text.split()
    try:
        await message.edit(f'Значение в блоке {txt[2]} раздела {txt[1]}: {cfg.read(txt[1],txt[2])}')
    except:
        await message.edit(f'Значение в блоке {txt[2]} раздела settings: {cfg.read("settings",txt[2])}')
        
async def dell(client: Client, message: Message):
    _, mode, module = message.text.split()
    if mode == 'module':
        if module+'.py' in Path('modules').rglob('*.py'):
            os.remove(f'./modules/{module}.py')
            await message.edit(f'<emoji id=5388849303982716989>⚡</emoji> Модуль {module} удален')
            message = await client.send_message(message.chat.id, '<emoji id=5388849303982716989>⚡</emoji> Wait...')
            await restart(client, message)
        else:
            await message.edit(f'<emoji id=5215680783863261658>❌</emoji> Не найден модуль {module}')

async def cfglist(client: Client, message: Message):
    if len(message.text.split()) > 1:
        sec = message.text.split()[1]
        ssec = sec
        listit = ''
        for s in cfg.list(sec):
            listit += ' → '.join(s)+'\n'
    else:
        sec = None
        ssec = 'all sections'
        listit = ' '.join(cfg.sections())
    await message.edit(f'Значения секции `{ssec}`:\n{listit}')


# MessageHandler(,filters.command('',prefix) & filters.me)
handlers = [
    MessageHandler(help, filters.command('help',prefix) & filters.me),
    MessageHandler(get,filters.command('get',prefix) & filters.me),
    MessageHandler(restart,filters.command('restart',prefix) & filters.me),
    MessageHandler(set,filters.command('set',prefix) & filters.me),
    MessageHandler(read,filters.command('read',prefix) & filters.me),
    MessageHandler(dell,filters.command('del',prefix) & filters.me),
    MessageHandler(cfglist,filters.command(['cl','cfglist'],prefix) & filters.me)
]

# "":"",
modules_help[module_name] = {
    "help [module]":"View all modules commands",
    'get [file_id/pem_id/rml/all]':"Get _ of message",
    'restart':"Restart userbot",
    'set [sec] [key] [val]':"Set value to config",
    'read [sec] [key]':"Read value from config"
}
