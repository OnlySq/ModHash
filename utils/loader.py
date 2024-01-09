import importlib
from .scripts import requirements
from . import log

def import_module(module, client) -> None:
    try:
        module1 = importlib.import_module('modules.'+module)
        #print(f'Handlers of module "{module}":[{module.handlers}]')
        for handler in module1.handlers:
            client.add_handler(handler)
            #print(f'Added handler "{handler}"')
    except Exception as e:
        log.write.warning(f'Import.{module}',e)
        raise