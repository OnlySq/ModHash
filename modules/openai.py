from utils.misc import prefix, openai_key
from utils.scripts import modules_help
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters, enums
from pyrogram.types import Message
import os, openai, requests
openai.api_key = openai_key

module_name = 'OpenAI'

alldraw = 0
allgpt = 0

def voicetext(client, message: Message):
    message.edit('🎤 Распознаём голосовое сообщение...')
    try:
        voice = client.download_media(message.reply_to_message.voice.file_id, './bin/hash/v2t/')
    except Exception as e:
        message.edit('<emoji id=5215680783863261658>❌</emoji> Отклонено: отсутствует голосовое сообщение')
    try:
        media_file = open(voice, 'rb')
        response = openai.Audio.transcribe(api_key=openai_key, model='whisper-1', file=media_file, prompt='')
        text = '🎤 Текст: '+response['text']
        message.edit(text)
    except:
        message.edit('<emoji id=5215680783863261658>❌</emoji> Не удалось перевести голос, попробуйте ещё раз')
    media_file.close()
    os.remove(voice)

def gpt(client: Client, message: Message):
    global allgpt
    if message.from_user.id == client.get_me().id:
        if message.text.split(' ',1)[1] == '+allgpt':
            allgpt = 1
            message.edit('<emoji id=5213128847439964513>✅</emoji> Режим "allgpt" включен\nВыключить: `!gpt -allgpt`',)
        elif message.text.split(' ',1)[1] == '-allgpt':
            allgpt = 0
            message.edit('<emoji id=5213128847439964513>✅</emoji> Режим "allgpt" выключен\nВключить: `!gpt +allgpt`')
        else:
            try:
                message.edit('<emoji id=5445243568903961265>🤖</emoji> ChatGPT 3.6 Turbo генерирует ответ...')
                engine="gpt-3.5-turbo-1106"
                prompt = message.text.split(' ',1)[1]
                completion = openai.ChatCompletion.create(model=engine, messages=[{"role": "user", "content": prompt}], temperature=0.9, max_tokens=3000)
                reply = completion.choices[0]["message"]["content"].replace("'", "`")
                reply = f'<emoji id=5445243568903961265>🤖</emoji>: {reply}\n\n<emoji id=5467825553463582772>❓</emoji>: {prompt}'
                #print('============REPLY============\n',reply,'\n/==========/REPLY/==========/')
                replymore4k =  [reply[i:i+3000] for i in range(0, len(reply), 3000)]
                #print('============REPLY4K============\n',replymore4k,'\n/==========/REPLY4K/==========/')
                if replymore4k[0] == reply:
                    message.edit(reply)
                else:
                    message.edit(replymore4k[0])
                    for chunk in replymore4k[1:]:
                        #print('============CHUNK============\n',chunk,'\n/==========/CHUNK/==========/')
                        client.send_message(message.chat.id, chunk)
            except Exception as e: message.edit(str(e)[:2000])
    else:
        if allgpt == 1:
            msgpt = client.send_message(message.chat.id, '<emoji id=5445243568903961265>🤖</emoji> ChatGPT 3.5 Turbo генерирует ответ...', reply_to_message_id=message.id)
            engine="gpt-3.5-turbo"
            prompt = message.text.split(' ',1)[1]
            completion = openai.ChatCompletion.create(model=engine, messages=[{"role": "user", "content": prompt}], temperature=0.9, max_tokens=3000)
            reply = completion.choices[0]["message"]["content"].replace("'", "```")
            reply = f'<emoji id=5445243568903961265>🤖</emoji>: {reply}\n\n[🚹 {message.from_user.first_name}](tg://user?id={message.from_user.id})<emoji id=5467825553463582772>❓</emoji>: {prompt}'
            replymore4k =  [reply[i:i+3000] for i in range(0, len(reply), 3000)]
            if len(replymore4k[0]) == len(reply):
                msgpt.edit(reply, parse_mode=enums.ParseMode.MARKDOWN)
            else:
                    message.edit(reply[0])
                    for chunk in reply[1:]:
                        client.send_message(message.chat.id, chunk, enums.ParseMode.MARKDOWN)
        else:
            client.send_message(message.chat.id, '<emoji id=5215680783863261658>❌</emoji> Режим общего GPT отключен.\nПопросите администратора включить эту функцию командой `!gpt +allgpt`')

def download_image(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

def draw(client: Client, message: Message):
    global alldraw
    if message.from_user.id == client.get_me().id:
        if message.text.split(' ',1)[1] == '+alldraw':
            alldraw = 1
            message.edit('<emoji id=5213128847439964513>✅</emoji> Режим "alldraw" включен\nВыключить: `!draw -alldraw`')
        elif message.text.split(' ',1)[1] == '-alldraw':
            alldraw = 0
            message.edit('<emoji id=5213128847439964513>✅</emoji> Режим "alldraw" выключен\nВключить: `!draw +alldraw`')
        else:
            try:
                prompt = message.text.split(' ',1)[1]
                message.edit('<emoji id=5215377245639549895>🖌️</emoji> DALL-E генерирует картинку...')
                response = openai.Image.create(prompt=prompt, n=1, size='1024x1024')
                image_url = response["data"][0]["url"]
                file_path = './bin/Mod/cache/photo_draw.jpg'
                download_image(image_url, file_path)
                message.delete()
                with open(file_path, 'rb') as photo:
                    client.send_photo(message.chat.id, photo, 'Made with [ModHash](https://t.me/telehashdev)\nPrompt: {}'.format(prompt))
            except Exception as e: message.edit(str(e)[:2000])
    else:
        if alldraw == 1:
            try:
                prompt = message.text.split(' ',1)[1]
                msgpt = client.send_message(message.chat.id, '<emoji id=5215377245639549895>🖌️</emoji> DALL-E генерирует картинку...', reply_to_message_id=message.id)
                response = openai.Image.create(prompt=prompt, n=1, size='1024x1024')
                image_url = response["data"][0]["url"]
                file_path = './bin/Mod/cache/photo_draw.jpg'
                download_image(image_url, file_path)
                msgpt.delete()
                with open(file_path, 'rb') as photo:
                    client.send_photo(message.chat.id, photo, 'Made with [ModHash](https://t.me/telehashdev)\nPrompt: {}'.format(prompt), reply_to_message_id=message.id)
            except Exception as e: message.edit(str(e)[:2000])
        else:
            client.send_message(message.chat.id, '<emoji id=5215680783863261658>❌</emoji> Режим общего DALL-E отключен.\nПопросите администратора включить эту функцию командой `!draw +alldraw`')

#MessageHandler(,filters.command('',prefix))
handlers = [
    MessageHandler(voicetext,filters.command('v2t',prefix)),
    MessageHandler(gpt,filters.command('gpt',prefix)),
    MessageHandler(draw,filters.command('draw',prefix))
]

modules_help[module_name] = {
    "v2t":"Voice to text with OpenAI",
    "gpt":"Use ChatGPT | +allgpt / -allgpt",
    'draw':"Use DALL-E from OpenAI"
}