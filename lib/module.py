#Coded by ANOI

#Imports
from core.design import design
from core.color import color
from time import sleep
import subprocess
import readline
import sys
import os

readline.add_history
line = '----------------------------------'
linec = '####################################'

############################

def menu(lang):
    if lang == 'ENGLISH':
        os.system('clear')
        design()
        print(color.GREEN+linec)
        print(color.YELLOW+'\n\tSelect your module:\n')
        modules = (subprocess.check_output('iw dev | grep wlan', shell=True)).decode().replace('\tInterface', '').split()
        
        for i, module in enumerate(modules):
            print(color.RED+'\t[{}] {}'.format(i, module))
        
        print(color.GREEN+'\n'+linec)

        try:
            numofmodule = int(input(color.CYAN+color.UNDERL+'\nWKBYA'+color.ENDC+' > '))
        except KeyboardInterrupt:
            print(color.YELLOW+'\n[*] Detected (CTRL + C)')
            sleep(1)
            print(color.RED+'[-] Exit')
            sys.exit()

        module = modules[numofmodule]        
        return module

    elif lang == 'RUSSIAN':
        os.system('clear')
        design()
        print(color.GREEN+linec)
        print(color.YELLOW+'\n\tВыберите Модуль:\n')
        modules = (subprocess.check_output('iw dev | grep wlan', shell=True)).decode().replace('\tInterface', '').split()
        
        for i, module in enumerate(modules):
            print(color.RED+'\t[{}] {}'.format(i, module))
        
        print(color.GREEN+'\n'+linec)

        try:
            numofmodule = int(input(color.CYAN+color.UNDERL+'\nWKBYA'+color.ENDC+' > '))
        except KeyboardInterrupt:
            print(color.YELLOW+'\n[*] Обнаруженно (CTRL + C)')
            sleep(1)
            print(color.RED+'[-] Выход')
            sys.exit()

        module = modules[numofmodule]        
        return module