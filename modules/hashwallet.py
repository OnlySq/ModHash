from pyrogram import Client, filters
from pyrogram.types import Message, User
from utils.misc import prefix, dev
from utils.scripts import modules_help, requirements
from pyrogram.handlers import MessageHandler

import random
from utils import wallet

module_name = 'HashWallet 0.1'

# Code

async def balance(client: Client, message: Message):
    await message.edit(f'💲 Ваш баланс: `{wallet.wallet.balance}`**⨝**')

async def add_bal(client: Client, message: Message):
    wallet.add_balance(float(random.randint(1,100)))

async def give(client: Client, message: Message):
    split = message.text.split(' ',2)
    try:
        cli: User = await client.get_users(message.chat.id)
        to_ment = cli.mention()
        a = 0
    except:
        a = 1
        await message.edit('❎ Wallet give нельзя использовать в каналах')
    if a == 0:
        try:
            try:
                give: wallet.GiveInfo = wallet.register_give(message, float(split[1]), split[2])
            except:
                give: wallet.GiveInfo = wallet.register_give(message, float(split[1]))
            if not give.has_password:
                await message.edit(f'💲 Пользователь {message.from_user.mention()} отправил `{split[1]}` **⨝**\nПолучатель: {to_ment}\n```HashTicket\n{give.crypto}```')
            else:
                await message.edit(f'💲 Пользователь {message.from_user.mention()} отправил `{split[1]}` **⨝**\nПолучатель: {to_ment}\n```HashTicket\n{give.crypto}```\n\n🔐 Защищен паролем')
        except wallet.GiveError as e:
            await message.edit(f'Ошибка Wallet: {e}')

async def claim(client: Client, message: Message):
    if message.reply_to_message:
        wallet.claim_give(message)
        
    else:
        await message.edit('❎ Для получения **⨝** нужно ответить на сообщение с `HashToken`')

# End of code

# MessageHandler(,filters.command('',prefix))
handlers = [
    MessageHandler(balance,filters.command(['balance','bal','b'], prefix) & filters.me),
    MessageHandler(add_bal,filters.command('dev#ab',prefix) & filters.me & filters.user(dev)),
    MessageHandler(give,filters.command('give',prefix)& filters.me)
]

# "":"",
modules_help[module_name] = {
    'bal / balance / b':'Show your balance',
    'give [float] <pass>':'give your tokens to another user'
}

requirements[module_name] = {
    ''
}


'''
 /¯¯¯¯¯¯\  /¯¯¯¯¯¯\ 
|        \/        |
 \       I        /
   \    <3      /
     \   A    /
       \    /
         \/

'''