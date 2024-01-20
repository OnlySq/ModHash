import os, time
from .misc import tag, folders, session_path
import msvcrt

def get_input() -> int:
    if msvcrt.kbhit():
        key = msvcrt.getch().decode()
        return key

def pretty_print_dict(dictionary, is_parent=True, indent=0, string=""):
    for i, (key, value) in enumerate(dictionary.items()):
        if isinstance(value, dict):
            if i == len(dictionary) - 1:
                if is_parent:
                    string += f"{'║ ' * indent}{'╠═' + '═' * indent}╦═ {key} ↓\n"
                else:
                    string += f"{'║ ' * indent}{'╚═' + '═' * indent}╦═ {key} ↓\n"
                string = pretty_print_dict(value, False, indent + 1, string)
            else:
                string += f"{' ' * indent}{'╠═' + '═' * indent}╦═ {key} ↓\n"
                string = pretty_print_dict(value, False, indent + 1, string)
        else:
            if i == len(dictionary) - 1:
                if is_parent:
                    string += f"{'║ ' * indent}{'╚═' + '═' * indent} {key} → {value}\n"
                else:
                    string += f"{'║ ' * indent}{'╚═' + '═' * indent} {key} → {value}\n"
            else:
                string += f"{'║ ' * indent}{'╠═' + '═' * indent} {key} → {value}\n"

    return string

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
            print(tag.session+'Выберите аккаунт:\n:: 0 > Создать новый')

            for entry in account_list:
                if not entry.name.startswith('.') and entry.is_file() and entry.name.rsplit(".")[1] == 'session':
                    count += 1
                    accounts.append(entry.name.split(".")[0])
                    print('::', count, '>', accounts[count])
        if accounts != ['new']:
            while True:
                try:
                    if msvcrt.kbhit():
                        key = msvcrt.getch().decode()
                        if key in ''.join(str(x) for x in range(len(accounts))):
                            break
                except: continue
            account = accounts[int(key)]
            os.system('cls')
            if account == 'new':
                account = input(tag.session+'Введите имя для новой сессии\n:: ')
            return account
        else:
            os.system('cls')
            return input(tag.session+'Сохраненных сессий не найдено.\nВведите имя для новой сессии\n:: ')
        
modules_help = {}
requirements = {}