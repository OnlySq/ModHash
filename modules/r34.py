from pyrogram import Client, filters
from pyrogram.types import Message, InputMediaPhoto
from utils.misc import prefix
from utils.scripts import modules_help, requirements
from pyrogram.handlers import MessageHandler

import random as r
import shutil
import os
import requests

module_name = 'Rule34'

# Code

async def typed_hentai_media(client: Client, message: Message):

    await message.delete()
    typex = message.text.split()[1]
    args = message.command
    try:
        if typex.capitalize() in h_tags:
            # Get NSFW by tag if exist
            response = requests.get(f'https://nsfw-api-p302.onrender.com/media/h/{typex.lower()}', stream=True)

            with open('r34.png', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
                out_file.close()

            await client.send_photo(message.chat.id, 'r34.png', 'By ModHash beta Rule34 module')
            os.remove('r34.png')

        elif '-img' in args:
            # Get NSFW by search
            sites = requests.get(f'https://nsfw-api-p302.onrender.com/h/image/search?q={typex.lower().replace(" ", "+")}').json()
            await client.send_photo(message.chat.id, sites[r.randint(0,len(sites))], 'By ModHash beta Rule34 module')
        
        elif '-vid' in args:
            sites = requests.get(f'https://nsfw-api-p302.onrender.com/h/video/search?q={typex.lower().replace(" ", "+")}').json()
            await client.send_video(message.chat.id, sites[r.randint(0,len(sites))], 'By ModHash beta Rule34 module')

        elif '-tags' in args:
            await client.send_message(message.chat.id, '`, `'.join(h_tags))
        
        elif '-ext-tags' in args:
            await client.send_message(message.chat.id, '`, `'.join(tags))
        
        else:
            await client.send_message(message.chat.id, f'No arguments or wrong type.\nTry to add `-img` or `-vid` to command or check tags with `{prefix}h -tags` for non-tagged command or `{prefix}h ext-tags` for tagged command')
    
    except:
        await client.send_message(message.chat.id, 'Tag error')



async def typed_real_media(client: Client, message: Message):

    await message.delete()

    typex = message.text.split()[1]
    args = message.command
    try:
        if typex.capitalize() in r_tags:
            # Get NSFW by tag if exist
            response = requests.get(f'https://nsfw-api-p302.onrender.com/media/r/{typex.lower()}', stream=True)

            with open('r34.png', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
                out_file.close()

            await client.send_photo(message.chat.id, 'r34.png', 'By ModHash beta Rule34 module')
            os.remove('r34.png')
        
        elif typex.capitalize() in tags:
            response = requests.get(f'https://nsfw-api-p302.onrender.com/r/image/{typex.lower()}', stream=True)

            with open('r34.png', 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)
                out_file.close()

            await client.send_photo(message.chat.id, 'r34.png', 'By ModHash beta Rule34 module')
            os.remove('r34.png')

        elif '-img' in args:
            # Get NSFW by search
            sites = requests.get(f'https://nsfw-api-p302.onrender.com/r/image/search?q={typex.lower().replace(" ", "+")}').json()
            await client.send_photo(message.chat.id, sites[r.randint(0,len(sites))], 'By ModHash beta Rule34 module')
        
        elif '-vid' in args:
            sites = requests.get(f'https://nsfw-api-p302.onrender.com/r/video/search?q={typex.lower().replace(" ", "+")}').json()
            await client.send_video(message.chat.id, sites[r.randint(0,len(sites))], 'By ModHash beta Rule34 module')

        elif '-tags' in args:
            await client.send_message(message.chat.id, '`, `'.join(r_tags))
        
        elif '-ext-tags' in args:
            await client.send_message(message.chat.id, '`, `'.join(tags))
        
        else:
            await client.send_message(message.chat.id, f'No arguments or wrong type.\nTry to add `-img` or `-vid` to command or check tags with `{prefix}h -tags` for non-tagged command or `{prefix}h ext-tags` for tagged command')
            
    except:
        await client.send_message(message.chat.id, 'Tag error')

# End of code

# MessageHandler(,filters.command('',prefix) & filters.me)
handlers = [
    MessageHandler(typed_hentai_media,filters.command('h',prefix) & filters.me),
    MessageHandler(typed_real_media,filters.command('r',prefix) & filters.me)
]

# "":"",
modules_help[module_name] = {
    "h":"Get hentai r34",
    "r":"Get real r34",
    "-vid":"Get video (arg)",
    "-img":"Get image (arg)",
    "-tags":"Get tags for non-arg (arg)",
    "-ext-tags":"Get tags for arged cmd (arg)"
}

requirements[module_name] = {}

## CONFIG ##

tags = [
    "Amateur",
    "Anal",
    "Anal-Gape",
    "Arab",
    "Argentina",
    "Asian",
    "Ass",
    "Ass-Licking",
    "Asshole",
    "Babe",
    "BBC",
    "BBW",
    "BDSM",
    "Big-Tits",
    "Beach",
    "Beautiful",
    "Big-Clit",
    "Big-Cock",
    "Big-Tits",
    "Bikini",
    "Blonde",
    "Blowjob",
    "Brazilian",
    "Ebony",
    "Facial",
    "Feet",
    "Anal",
    "Gangbang",
    "Gay",
    "Glasses",
    "Gloryhole",
    "Goth",
    "Granny",
    "Gym",
    "Hairy",
    "Handjob",
    "Hardcore",
    "High-Heels",
    "Homemade",
    "Indian",
    "Interracial",
    "Japanese",
    "Jeans",
    "Korean",
    "Pussy",
    "Ladyboy",
    "Latina",
    "Legs",
    "Brunette",
    "Bukkake",
    "Cameltoe",
    "Casting",
    "Chinese",
    "Chubby",
    "Colombian",
    "Cosplay",
    "Teen",
    "Cougar",
    "Cowgirl",
    "Creampie",
    "Cuckold",
    "Cum-In-Mouth",
    "Cum-In-Pussy",
    "Cumshot",
    "Curvy",
    "Cute",
    "Deepthroat",
    "Dildo",
    "Doggy-Style",
    "Double-Penetration",
    "Dress",
    "Tall",
    "Tattoo",
    "Teacher",
    "Teen",
    "Thai",
    "Thong",
    "Threesome",
    "Upskirt",
    "Venezuela",
    "Vintage",
    "Webcams",
    "White",
    "Wife",
    "Yoga",
    "Yoga-Pants",
    "Redhead",
    "Russian",
    "Saggy-Tits",
    "Sandals",
    "Schoolgirl",
    "Secretary",
    "Selfie",
    "Shemale",
    "Short-Hair",
    "Latina",
    "Shorts",
    "Shower",
    "Skinny",
    "Skirt",
    "Solo",
    "SSBBW",
    "Stockings",
    "Tall",
    "Tattoo",
    "Teacher",
    "Teen",
    "Thai",
    "Thong",
    "Threesome"
]

h_tags = [
    "Vanila",
    "Yaoi",
    "Yuri",
    "Bdsm",
    "Trap"
]

r_tags = [
    "Ass",
    "Boobs",
    "Pussy"
]