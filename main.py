from utils import default_imports
import logging
import platform
from datetime import datetime
startTime = datetime.now()    
from pathlib import Path
import os
from pyrogram import Client, idle
from utils import misc, default_imports, cfgmaster
from utils.scripts import start
from utils.loader import import_module

script_path = os.path.dirname(os.path.realpath(__file__))
if script_path != os.getcwd():
    os.chdir(script_path)

start.init()

app = Client(
    name = start.user(),
    api_id = misc.api_id,
    api_hash = misc.api_hash,
    app_version = misc.userbot_version,
    device_model = misc.userbot_name,
    system_version = platform.version() + " " + platform.machine(),
    workdir = misc.session_path
)

async def main():
    logging.basicConfig(level=logging.WARNING, format='%(asctime)s | %(message)s')
    #try:
    await cfgmaster.start(app)
    await app.start()
    #except Exception as e:
     #   print(e)
      #  await asyncio.sleep(2)
       # exit()
    
    success_modules = 0
    failed_modules = 0
    success_modules_list = []
    failed_modules_list = []

    for path in Path('modules').rglob('*.py'):
        try:
            import_module(path.stem, app)
        except Exception as e:
            failed_modules += 1
            failed_modules_list.append(path.stem)
        else:
            success_modules += 1
            success_modules_list.append(path.stem)
    if success_modules:
        print(f'Загружено {success_modules} модулей.\n\tСписок: {" ".join(success_modules_list)}')
    if failed_modules:
        print(f'Не удалось загрузить {failed_modules} модулей.\n\tСписок: {" ".join(failed_modules_list)}')
    
    print(f"{misc.userbot_name} {misc.userbot_version} запущен.")
    await idle()
    await app.stop()

if __name__ == "__main__":
    app.run(main())