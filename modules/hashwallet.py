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
    await message.edit(f'<emoji id=5370685990367141494>💲</emoji> Ваш баланс: `{wallet.wallet.balance}`**⨝**')

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
        await message.edit('<emoji id=5215680783863261658>❌</emoji> Wallet give нельзя использовать в каналах')
    if a == 0:
        try:
            try:
                give: wallet.GiveInfo = wallet.register_give(message, float(split[1]), split[2])
            except:
                give: wallet.GiveInfo = wallet.register_give(message, float(split[1]))
            await message.edit(f'<emoji id=5370685990367141494>💲</emoji> Чек: `{split[1]}` **⨝**\nСоздал: {message.from_user.mention()} ({give.new_balance} **⨝**)\nПолучатель: {to_ment}\n```HashTicket\n#{give.crypto}```')
        except wallet.GiveError as e:
            await message.edit(f'Ошибка Wallet: {e}')

async def claim(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit('<emoji id=5215680783863261658>❌</emoji> Для получения **⨝** нужно ответить на сообщение с `HashToken`')
    else:
        try:
            claim: wallet.ClaimInfo = wallet.claim_give(message)
            await message.edit(f'<emoji id=5370685990367141494>💲</emoji> Чек от {claim.claim_from} на `{claim.claim_value}` **⨝** получен.\n[ `{claim.old_balance}` **⨝** -> `{claim.new_balance}` **⨝** ]')
        except wallet.ClaimError as exc:
            await message.edit(f'<emoji id=5215680783863261658>❌</emoji> При получении **⨝** возникла ошибка: {exc}')

# End of code

# MessageHandler(, filters.command('', prefix) & filters.me)
handlers = [
    MessageHandler(balance,filters.command(['balance','bal','b'], prefix) & filters.me),
    MessageHandler(add_bal,filters.command('dev#ab', prefix) & filters.me & filters.user(dev)),
    MessageHandler(give,filters.command('give', prefix) & filters.me),
    MessageHandler(claim,filters.command('claim', prefix) & filters.me)
]

# "":"",
modules_help[module_name] = {
    'bal / balance / b':'Show your balance',
    'give [float] <pass>':'give your tokens to another user'
}

requirements[module_name] = {
    ''
}