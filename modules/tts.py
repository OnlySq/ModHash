from pyrogram import Client, filters
from pyrogram.types import Message
from utils.misc import prefix, data
from utils.scripts import modules_help, requirements
from pyrogram.handlers import MessageHandler

import os
from gtts import gTTS

module_name: str = 'Text-To-Speech'

voicepath = data+'\\Mod\\output.mp3'

# Code

async def text_to_speech(client: Client, message: Message):
    rtt = 0
    try:
        text = message.text.split(maxsplit=1)[1]
        rtt = 0
    except:
        text = message.reply_to_message.text
        rtt = 1
    await message.edit('Подождите...')
    tts = gTTS(text, lang='ru', slow=False)
    tts.save(voicepath)
    await message.delete()
    if rtt == 0:
        await client.send_voice(chat_id=message.chat.id, voice=voicepath, caption="TTS with [ModHash](https://t.me/telehashdev)")
    elif rtt == 1:
        await client.send_voice(chat_id=message.chat.id, voice=voicepath, caption="TTS with [ModHash](https://t.me/telehashdev)", reply_to_message_id=message.reply_to_message.id)
    os.remove(voicepath)

# End of code

# MessageHandler(,filters.command('',prefix))
handlers = [
    MessageHandler(text_to_speech,filters.command('tts',prefix) & filters.me)
]

# "":"",
modules_help[module_name] = {
    'tts':'Text-to-speech command. Sends you a voice by ur text'
}

requirements[module_name] = {
    'gtts'
}