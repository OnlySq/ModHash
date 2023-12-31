# import openai, sys, os, random, requests, time, collections, itertools, winreg, struct, platform, datetime, windows_tools, asyncio
import asyncio, sys
async def pipinstall(module):
    await asyncio.create_subprocess_exec(
            sys.executable,
            "-m",
            "pip",
            "install",
            "-U",
            module,
        )
    
try: import openai
except: pipinstall('openai')
try: import random
except: pipinstall('random')
try: import requests
except: pipinstall('requests')
try: import winreg
except: pipinstall('winreg')
try: import struct
except: pipinstall('struct')
try: import platform
except: pipinstall('platform')
try: import datetime
except: pipinstall('datetime')
try: import windows_tools
except: pipinstall('windows_tools')
try: import pyrogram
except: pipinstall('pyrogram')
try: import tgcrypto
except: pipinstall('tgcrypto')
try: import pathlib
except: pipinstall('pathlib')
try: import typing
except: pipinstall('typing')
try: import importlib
except: pipinstall('importlib')

#try: import
#except: pipinstall('')