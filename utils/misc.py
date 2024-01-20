'''
This a "misc" template for your code
To generate api ID and api HASH visit
https://core.telegram.org/api/obtaining_api_id
This file is restricted to get original NoBan APIs
For help with code PM: @NoBanOnlyZXC
This file updated from "secret" file in Telehash
'''
from datetime import datetime
import os
data = os.getenv('LOCALAPPDATA')
from pyrogram.types import User

userbot_version = '1.02 DEV'
userbot_name = 'ModHash'
session_path = data+'\\Mod\\'
config_path = data+'\\Mod\\cache\\settings.ini'
cache_path = data+'\\Mod\\cache\\'
log_path = f'{data}\\Mod\\logs\\{str(datetime.now()).rsplit(".")[0].replace(" ","_").replace(":","_")}_log.txt'
wallet_path = data+'\\Mod\\wallet\\'
claimed_tokens_path = wallet_path+'tokens.crypto'
prefix = '!'
icon = '.\\utils\\mod.png'

api_id = 23441409
api_hash = "fc2ebed7751be9bc29171b0072b10fed"

dev = 5624858175
devd = '@NoBanOnlyZXC'

openai_key =  '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'
openweather_key = 'e2fed831b5dae85a421f0a31eb2784e6'
ninja_api = 'wnI6EPljWjcuYV2QJxsb6A==YeQ98fSj9fDXDf5M'

class tag:
    session = '[ Session ] '
    folder = '[ Folders ] '
    wallet = '[ Wallet ] '

folders = [
    data+'\\',
    data+'\\Mod',
    data+'\\Mod\\cache',
    data+'\\Mod\\logs',
    data+'\\Mod\\wallet'
    ]

commands_stats = {
    "success": 0,
    "failure": 0
}

class user:
    me: User