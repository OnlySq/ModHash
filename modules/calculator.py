from pyrogram import Client, filters
from pyrogram.types import Message
from utils.misc import prefix
from utils.scripts import modules_help, requirements
from pyrogram.handlers import MessageHandler

import asyncio

module_name = 'Calculator'

# Code

async def calc(_, message: Message):
    if len(message.command) <= 1:
        return
    args = " ".join(message.command[1:])
    try:
        result = str(eval(args))

        if len(result) > 4096:
            i = 0
            for x in range(0, len(result), 4096):
                if i == 0:
                    await message.edit(
                        f"<code>{args}<code><b>=</b><code>{result[x:x + 4000]}</code>"
                    )
                else:
                    await message.reply(
                        f"<code>{result[x:x + 4096]}</code>"
                    )
                i += 1
                await asyncio.sleep(0.18)
        else:
            await message.edit(
                f"<code>{args}<code><b>=</b><code>{result}</code>"
            )
    except Exception as e:
        await message.edit(f"<i>{args}=</i><b>=</b><code>{e}</code>")


# End of code

# MessageHandler(,filters.command('',prefix) & filters.me)
handlers = [
    MessageHandler(calc,filters.command('calc',prefix) & filters.me)
]

# "":"",
modules_help[module_name] = {
    "calc [expression]*": "solve a math problem",
    "+":"addition",
    "–":"subtraction",
    "*":"multiplication",
    "/":"division",
    "**":"degree",
}

requirements[module_name] = {
    
}