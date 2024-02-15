![mod](https://github.com/NoBanOnlyZXC/ModHash/assets/155289158/a1c81646-688d-410d-9d02-adef32ec1094)
# ModHash
ModHash это ядро для кастомных подключаемых модулей, написан на `pyrogram`.

# Установка
1. [Скачать](https://github.com/NoBanOnlyZXC/ModHash/releases/latest) архив `ModHash` и `Python` (при первой установке) 
2. Установить `Python 3.11.7` (есть в разделе релизов), обязательно галочку на `PATH`
3. Распаковать `ModHash` в любое место
4. Запустить `install_reqs.bat`
5. Запустить `start.bat`

# Функционал
Базовый функционал обеспечивают встроенные модули, на данный момент (1.032 beta) их 10

Базовые команды:
```copy
╔ Core
╠═╦═ Animations ↓
║ ╠══ type → Type text sim-by-sim
║ ╠══ stupid → Stupid animation
║ ╠══ bombs → Bombing animation
║ ╠══ earth → Fun animation try yourself to know more
║ ╠══ heart → Fun animation try yourself to know more
║ ╠══ think → Fun animation try yourself to know more
║ ╠══ smoon → Fun animation try yourself to know more
║ ╚══ tmoon → Fun animation try yourself to know more
╠═╦═ Calculator ↓
║ ╠══ calc [expression]* → solve a math problem
║ ╠══ + → addition
║ ╠══ – → subtraction
║ ╠══ * → multiplication
║ ╠══ / → division
║ ╚══ ** → degree
╠═╦═ HashWallet ↓
║ ╠══ bal / balance / b → Show your balance
║ ╠══ give [float]  → Give your tokens to another user
║ ╚══ claim (reply to ticket) → Claim tokens
╠═╦═ NowPlaying ↓
║ ╚══ now/np → Send music playing now
╠═╦═ Old ↓
║ ╠══ hearts → Old Telehash animation
║ ╠══ rib → Ribbon animation (May 9)
║ ╠══ roll → Roll from x to y (!roll x y)
║ ╠══ try → Try your question
║ ╠══ . → Resend replied message
║ ╚══ prus → Perfect your message with this!
╠═╦═ OpenAI ↓
║ ╠══ v2t → Voice to text with OpenAI
║ ╠══ gpt → Use ChatGPT | +allgpt / -allgpt
║ ╚══ draw → Use DALL-E from OpenAI
╠═╦═ QrCode ↓
║ ╚══ qr [text] → Create QR and send it
╠═╦═ Rule34 ↓
║ ╠══ h → Get hentai r34
║ ╠══ r → Get real r34
║ ╠══ -vid → Get video (arg)
║ ╠══ -img → Get image (arg)
║ ╠══ -tags → Get tags for non-arg (arg)
║ ╚══ -ext-tags → Get tags for arged cmd (arg)
╠═╦═ System ↓
║ ╠══ help [module] → View all modules commands
║ ╠══ get [file_id/pem_id] → Get _ of message
║ ╠══ restart → Restart userbot
║ ╠══ set [sec] [key] [val] → Set value to config
║ ╚══ read [sec] [key] → Read value from config
╠═╦═ Text-To-Speech ↓
║ ╚══ tts → Text-to-speech command. Sends you a voice by ur text
```

# Модули
Вы можете сами писать свои модули и встраивать в юзербот, для этого есть папка `modules`
Для начала можно использовать `Template.py`:

```python
from pyrogram import Client, filters
from pyrogram.types import Message
from utils.misc import prefix
from utils.scripts import modules_help, requirements
from pyrogram.handlers import MessageHandler

module_name = ''

# Code

async def name(client: Client, message: Message):
    i = 0

# End of code

# MessageHandler(,filters.command('',prefix) & filters.me)
handlers = [

]

# "":"",
modules_help[module_name] = {

}

requirements[module_name] = {
    
}
```
