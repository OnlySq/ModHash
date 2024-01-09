from pyrogram import Client, filters
from pyrogram.types import Message
from utils.misc import prefix
from utils.scripts import modules_help
from pyrogram.handlers import MessageHandler

module_name = 'System'

async def help(client: Client, message: Message):
    await message.edit(str(modules_help))

# MessageHandler(,filters.command('',prefix))
handlers = [
    MessageHandler(help, filters.command('help',prefix))
]

# "":"",
modules_help[module_name] = {
    "help":"View all modules commands"
}