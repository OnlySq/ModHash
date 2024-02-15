from pyrogram import Client, filters
from pyrogram.types import Message
from utils.misc import prefix, data
from utils.scripts import modules_help
from pyrogram.handlers import MessageHandler
from utils import log

import qrcode

module_name = 'QrCode'

qrpath = data+'\\Mod\\cache\\qr.png'

# Code

async def rphoto(client: Client, message: Message):
    try:
        content = message.text.split(' ',1)[1]
        await message.delete()

        qc = qrcode.make(content, box_size=20, border=1)
        qc.save(qrpath)
        await client.send_photo(message.chat.id, qrpath, 'Made with <emoji id=5215377245639549895>✅</emoji>[ModHash](https://t.me/telehashdev)')
        log.write.info('QRCode',f'Created qrcode with content "{content}"')
    except Exception as e:
        log.write.error('QRCode','QRCode error: '+str(e))
        await client.send_message(message.chat.id, 'QRCode error: '+str(e))

# End of code

# MessageHandler(,filters.command('',prefix))
handlers = [
    MessageHandler(rphoto,filters.command('qr',prefix))
]

# "":"",
modules_help[module_name] = {
    "qr [text]":"Create QR and send it"
}