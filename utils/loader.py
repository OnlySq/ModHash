import importlib

def import_module(module, client):
    try:
        module1 = importlib.import_module('modules.'+module)
        #print(f'Handlers of module "{module}":[{module.handlers}]')
        for handler in module1.handlers:
            client.add_handler(handler)
            #print(f'Added handler "{handler}"')
    except Exception as e:
        print(e)
        raise Exception(f'Module {module} can`t be loaded!')