import os, time
from .misc import tag, folders, session_path

class start:
    
    def init() -> None:
        for folder in folders:
            print(tag.folder+'Создаю папку '+folder)
            try:
                os.mkdir(folder)
            except:
                print(tag.folder+'Не удалось создать '+folder+', возможно папка уже существует')
                continue
        #os.system('cls')

    def user() -> str:
        accounts = ['new']
        count = 0
        print(tag.session+'Поиск аккаунтов...')
        time.sleep(.8)
        os.system('cls')

        with os.scandir(session_path) as account_list:
            print(tag.session+'Выберите аккаунт:')

            for entry in account_list:
                if not entry.name.startswith('.') and entry.is_file() and entry.name.rsplit(".")[1] == 'session':
                    count += 1
                    accounts.append(entry.name.split(".")[0])
                    print('::', count, accounts[count])
        if accounts != ['new']:
            account = accounts[int(input(':: '))]
            os.system('cls')
            if account == 'new':
                account = input(tag.session+'Введите имя для новой сессии\n:: ')
            return account
        else:
            os.system('cls')
            return input(tag.session+'Сохраненных сессий не найдено.\nВведите имя для новой сессии\n:: ')
        
modules_help = {}
requirements = {}