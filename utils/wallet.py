import cryptocode as cc
from pyrogram.types import Message
from .misc import user, wallet_path
from . import log

wallet_file = wallet_path+f'wallet_{user.me.id}.crypto'

class GiveError(Exception):
    pass

class GiveInfo:
    crypto: str
    has_password: bool = False
    crypto_password: str

class wallet:
    cryptokey = f'{str(user.me.phone_number)}{str(user.me.id)}'
    balance: float # ⨝

def read_balance() -> float:
    try:
        with open(wallet_file, 'r', encoding="utf-8") as f:
            cry = f.read()
            bal = cc.decrypt(str(cry), wallet.cryptokey)
            log.write.info('Wallet',f'User balance now: {bal} ⨝')
            f.close()
            if bal != '':
                return bal
            else:
                raise
    except:
        print('Creating new wallet for you')
        with open(wallet_file, 'w+', encoding="utf-8") as f:
            cry = cc.encrypt(str(float(10)), wallet.cryptokey)
            f.write(cry)
            f.close()
            log.write.info('Wallet',f'Created new wallet for user {user.me.id} / {user.me.phone_number} with 10.0 ⨝')
            return float(10)
        
def add_balance(val: float) -> str:
    bal = wallet.balance =+ val
    with open(wallet_file, 'w', encoding="utf-8") as f:
        f.write(cc.encrypt(str(bal), wallet.cryptokey))
        f.close()
    return str(bal)

def register_give(message: Message, val: float, password: str = None) -> GiveInfo:
    from_user = str(message.from_user.id)
    to_user = str(message.chat.id)

    if val > wallet.balance:
        raise GiveError(f"Can't create give, value ({val} **⨝**) > wallet balance ({wallet.balance} **⨝**)")
    else:
        if password:
            GiveInfo.has_password = True
            GiveInfo.crypto_password = cc.encrypt(password, str(to_user+from_user))
            GiveInfo.crypto = cc.encrypt(str(val), password, from_user)
        else:
            GiveInfo.has_password = False
            GiveInfo.crypto_password = str(to_user+from_user)
            GiveInfo.crypto = cc.encrypt(str(val), str(to_user+from_user))
        with open(wallet_file, 'w', encoding="utf-8") as f:
            wallet.balance -= val
            cry = cc.encrypt(str(wallet.balance), wallet.cryptokey)
            f.write(cry)
            f.close()
            log.write.info('Wallet',f'Created new GIVE token: from {from_user} to {to_user}, value: {val} ⨝, new balance: {wallet.balance}')

        return GiveInfo
    
def claim_give(message: Message, password: str = None):



wallet.balance = read_balance() # ⨝