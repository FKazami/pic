import os

if 'pyperclip' not in os.popen('pip list').read():
    os.system('pip install pyperclip')
import pyperclip

file = input().strip()
pyperclip.copy('https://cdn.jsdelivr.net/gh/fei0319/pic/img/' + file)