import datetime
from .misc import log_path

class write:
    def warn(module, message) -> None:
        with open(log_path, 'a+', encoding="utf-8") as f:
            f.write(f'\n[ WARN | {str(datetime.datetime.now()).rsplit(".")[0]} | {module} ] >> {message}')
            f.close()

    def info(module, message) -> None:
        with open(log_path, 'a+', encoding="utf-8") as f:
            f.write(f'\n[ INFO | {str(datetime.datetime.now()).rsplit(".")[0]} | {module} ] >> {message}')
            f.close()

    def warning(module, message) -> None:
        with open(log_path, 'a+', encoding="utf-8") as f:
            f.write(f'\n[ WARNING | {str(datetime.datetime.now()).rsplit(".")[0]} | {module} ] >> {message}')
            f.close()

    def error(module, message) -> None:
        with open(log_path, 'a+', encoding="utf-8") as f:
            f.write(f'\n[ ERROR | {str(datetime.datetime.now()).rsplit(".")[0]} | {module} ] >> {message}')
            f.close()