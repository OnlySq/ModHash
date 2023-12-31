from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
from utils.misc import prefix
from utils.scripts import modules_help
from pyrogram.handlers import MessageHandler
from collections import deque

module_name = 'Animations'

async def type(client: Client, message: Message):
    input_text = message.text.split("!type ", maxsplit=1)[1]
    temp_text = input_text
    edited_text = ""
    typing_symbol = "I"

    while edited_text != input_text:
        try:
            await message.edit(edited_text + typing_symbol)
            await asyncio.sleep(0.03)
            edited_text = edited_text + temp_text[0]
            temp_text = temp_text[1:]
            await message.edit(edited_text)
            await asyncio.sleep(0.03)
        except:
            pass

async def stupid(client: Client, message: Message):
    animation_interval = 0.5
    animation_ttl = range(0, 14)
    await message.edit_text("stupid boy")
    animation_chars = [
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n🧠         (^_^)🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n🧠       (^_^)  🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n🧠     (^_^)    🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n🧠   (^_^)      🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n🧠 (^_^)        🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n🧠< (^_^ <)         🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n(> ^_^)>🧠         🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n  (> ^_^)>🧠       🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n    (> ^_^)>🧠     🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n      (> ^_^)>🧠   🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n        (> ^_^)>🧠 🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n          (> ^_^)>🧠🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n           (> ^_^)>🗑",
        "<b>YOUR BRAIN</b> ➡️ 🧠\n\n           < (^_^ <)🗑",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await message.edit_text(animation_chars[i % 14])

async def bombs(client: Client, message: Message):

    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n")
    await asyncio.sleep(1)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n")
    await asyncio.sleep(0.5)
    await message.edit_text("▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n")

async def earth(client: Client, message: Message):
    deq = deque(list("🌏🌍🌎🌎🌍🌏🌍🌎"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit_text(".".join(deq))
        deq.rotate(1)

async def think(client: Client, message: Message):
    deq = deque(list("🤔🧐🤔🧐🤔🧐"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit_text(".".join(deq))
        deq.rotate(1)

async def lmao(client: Client, message: Message):
    deq = deque(list("😂🤣😂🤣😂🤣"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit_text("".join(deq))
        deq.rotate(1)

async def heart(client: Client, message: Message):
    deq = deque(list("❤️🧡💛💚💙💜🖤"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit_text("".join(deq))
        deq.rotate(1)

async def moon(client: Client, message: Message):
    deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖‍"))
    for _ in range(48):
        await asyncio.sleep(0.1)
        await message.edit_text(".".join(deq))
        deq.rotate(1)

async def smoon(client: Client, message: Message):
    animation_interval = 0.2
    animation_ttl = range(101)
    animation_chars = [
        "🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗",
        "🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘",
        "🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑",
        "🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒",
        "🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓\n🌗🌗🌗🌗🌗\n🌓🌓🌓🌓🌓",
        "🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔\n🌘🌘🌘🌘🌘\n🌔🌔🌔🌔🌔",
        "🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕\n🌑🌑🌑🌑🌑\n🌕🌕🌕🌕🌕",
        "🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖\n🌒🌒🌒🌒🌒\n🌖🌖🌖🌖🌖",
    ]

    await message.edit_text("smoon...")
    await asyncio.sleep(3)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit_text(animation_chars[i % 8])

async def tmoon(client: Client, message: Message):
    animation_interval = 0.2
    animation_ttl = range(96)
    animation_chars = [
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
        "🌗",
        "🌘",
        "🌑",
        "🌒",
        "🌓",
        "🌔",
        "🌕",
        "🌖",
    ]

    await message.edit_text("tmoon...")
    await asyncio.sleep(3)
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await message.edit_text(animation_chars[i % 32])

modules_help[module_name] = {
    "type": "Type text sim-by-sim",
    "stupid": "Stupid animation",
    "bombs": "Bombing animation",
    "earth": "Earth animation",
    "heart": "Fun animation try yourself to know more",
    "think": "Fun animation try yourself to know more",
    "earth": "Fun animation try yourself to know more",
    "earth": "Fun animation try yourself to know more",
    "smoon": "Fun animation try yourself to know more",
    "tmoon": "Fun animation try yourself to know more"
}

h_type = MessageHandler(type,filters.command('type',prefix))
h_stupid = MessageHandler(stupid,filters.command('stupid',prefix))
h_bombs = MessageHandler(bombs,filters.command('bombs',prefix))
h_earth = MessageHandler(earth,filters.command('earth',prefix))
h_heart = MessageHandler(heart,filters.command('heart',prefix))
h_think = MessageHandler(think,filters.command('think',prefix))
h_earth = MessageHandler(earth,filters.command('earth',prefix))
h_smoon = MessageHandler(smoon,filters.command('smoon',prefix))
h_tmoon = MessageHandler(tmoon,filters.command('tmoon',prefix))

# h_ = MessageHandler(,filters.command('',prefix))
# handlers = []
handlers = [h_type, h_stupid, h_bombs, h_earth, h_heart, h_think, h_earth, h_smoon, h_tmoon]