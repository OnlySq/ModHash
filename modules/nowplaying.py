import asyncio
from winsdk.windows.media.control import \
    GlobalSystemMediaTransportControlsSessionManager as MediaManager
from bs4 import BeautifulSoup
import requests
import urllib.request

from pyrogram import Client, filters
from pyrogram.types import Message
from utils.misc import prefix, cache_path
from utils.scripts import modules_help, requirements
from pyrogram.handlers import MessageHandler

module_name = 'NowPlaying'

# Code

async def get_media_info():
    
    sessions = await MediaManager.request_async()

    current_session = sessions.get_current_session()
    if current_session:
        info = await current_session.try_get_media_properties_async()
        mfrom = current_session.get_timeline_properties()
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
    
    urllib.request.urlretrieve(first_image, cache_path+'pic.png')

async def get_time_info():
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
        search_bing_images(current_media_info['artist'], current_media_info['title'])
        await client.send_photo(message.chat.id,cache_path+'pic.png',f'<emoji id=5212941939053175244>🎧</emoji> Сейчас играет:\n `{current_media_info["artist"]} - {current_media_info["title"]}`\n<emoji id=5980965624396910678>🔊</emoji> Источник: {str(await get_player_info()).replace(".", " ").title()}')
    except Exception as e:
        await client.send_message(message.chat.id, e)

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