import winsdk.windows.storage.streams as streams
from winsdk.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager
from bs4 import BeautifulSoup
import requests, os
import urllib.request
import subprocess

from pyrogram import Client, filters
from pyrogram.types import Message
from utils.misc import prefix, cache_path
from utils.scripts import modules_help, requirements
from pyrogram.handlers import MessageHandler

module_name = 'NowPlaying'

THUMBNAIL_BUFFER_SIZE = 5 * 1024 * 1024

# Code

async def get_media_info():
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    if current_session:
        info = await current_session.try_get_media_properties_async()
        info_dict = {song_attr: info.__getattribute__(song_attr) for song_attr in dir(info) if song_attr[0] != '_'}
        info_dict['genres'] = list(info_dict['genres'])
        return info_dict

def search_bing_images(artist, title):
    url = "https://www.bing.com/images/search"
    params = {
        "q": f"песня {artist} - {title} обложка альбома"
    }
    response = requests.get(url, params=params)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    first_image = soup.find('img',{'class':'mimg'})['src']

    with open('bs.html','w+',encoding='utf8') as f:
        f.write(str(soup))
        f.close()
    
    urllib.request.urlretrieve(first_image, cache_path+'thumb.png')

async def get_time_info() -> str:
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    if current_session:
        info = current_session.get_timeline_properties()
        return info.end_time

async def get_player_info() -> str:
    sessions = await MediaManager.request_async()
    current_session = sessions.get_current_session()
    if current_session:
        id = current_session.source_app_user_model_id
        return str(id)

async def nowplaying(client: Client, message: Message):
    try:
        await message.delete()
        current_media_info = await get_media_info()
        os.system('python ./utils/WindowsNowPlaying.py')
        #search_bing_images(current_media_info['artist'], current_media_info['title'])
        await client.send_photo(message.chat.id,f"thumb.png".replace('/', '_').replace('\\', '_'),f'<emoji id=5212941939053175244>🎧</emoji> Сейчас играет:\n `{current_media_info["artist"]} - {current_media_info["title"]}`\n<emoji id=5980965624396910678>🔊</emoji> Источник: {str(await get_player_info()).replace(".", " ").title()}')
        os.remove(f"thumb.png".replace('/', '_').replace('\\', '_'))
    except ValueError:
        await client.send_message(message.chat.id,f'<emoji id=5212941939053175244>🎧</emoji> Сейчас играет:\n `{current_media_info["artist"]} - {current_media_info["title"]}`\n<emoji id=5980965624396910678>🔊</emoji> Источник: {str(await get_player_info()).replace(".", " ").title()}')
    except Exception as e:
        await client.send_message(message.chat.id, e)
        raise

# End of code

# MessageHandler(,filters.command('',prefix) & filters.me)
handlers = [
    MessageHandler(nowplaying,filters.command(['now','np'],prefix) & filters.me)
]

# "":"",
modules_help[module_name] = {
    'now/np':'Send music playing now'
}

requirements[module_name] = {
    
}