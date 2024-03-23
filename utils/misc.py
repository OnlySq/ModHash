'''
This a "misc" template for your code
To generate api ID and api HASH visit: https://core.telegram.org/api/obtaining_api_id
! This file is restricted to get original NoBan APIs

For help with code PM: @NoBanOnlyZXC

This file updated from "secret" file in Telehash
'''

from datetime import datetime
import os
data = os.getenv('LOCALAPPDATA')
from pyrogram.types import User

userbot_version = '1.033 Beta'
userbot_name = 'ModHash'
session_path = data+'\\Mod\\'
config_path = data+'\\Mod\\cache\\settings.ini'
cache_path = data+'\\Mod\\cache\\'
log_path = f'{data}\\Mod\\logs\\{str(datetime.now()).rsplit(".")[0].replace(" ","_").replace(":","_")}_log.txt'
wallet_path = data+'\\Mod\\wallet\\'
claimed_tokens_path = wallet_path+'tokens.crypto'
prefix = '!'
icon = 'https://private-user-images.githubusercontent.com/155289158/298374589-a1c81646-688d-410d-9d02-adef32ec1094.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MDU4MzIxMDAsIm5iZiI6MTcwNTgzMTgwMCwicGF0aCI6Ii8xNTUyODkxNTgvMjk4Mzc0NTg5LWExYzgxNjQ2LTY4OGQtNDEwZC05ZDAyLWFkZWYzMmVjMTA5NC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwMTIxJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDEyMVQxMDEwMDBaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1mZGRmNDQ2ZTEyMDU3YWExNjc0Yjc2NmE3YTlhYjMyNDBiZGZmZWMxM2Q1MWI4NjVjMWI2ZWM1NzlmOGE1YTg4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.9LkiuMbdVL5j2AfouDqv3fycCyk5pRHsxFc-JQsueCs'

api_id = 23441409
api_hash = "fc2ebed7751be9bc29171b0072b10fed"

dev = 5624858175
devd = '@NoBanOnlyZXC'
google_api_key = 'AIzaSyAqDp9SgWaMFonVrkrzGwXhRJ_rNajLDbg'
openai_key = ''
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

class user:
    account: str
    me: User