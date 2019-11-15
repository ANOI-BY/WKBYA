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

def menu(lang, module, homedir):
    if lang == 'ENGLISH':
        os.system('clear')
        design()
        print(color.GREEN+linec)
        print(color.YELLOW+'\n\tSelect attack:')
        print(color.RED+'\n[1] ATTACK A')
        print('[2] ATTACK B')
        print('[3] ATTACK C')
        print('[4] ATTACK D')
        print('[5] ATTACK E')
        print(color.YELLOW+'\n[6] help')
        print('[7] Select language')
        print('[8] Select module')
        print('[9] Exit')
        print(color.GREEN+'\n'+linec)

        try:
            numofattack = int(input(color.CYAN+color.UNDERL+'\nWKBYA'+color.ENDC+' > '))
        except KeyboardInterrupt:
            print(color.YELLOW+'\n[*] Detected (CTRL + C)')
            sleep(1)
            print(color.RED+'[-] Exit')
            sys.exit()
        except ValueError:
            menu(lang,module,homedir)

        from lib.attack import attack

        if numofattack in range(1,6):
            attack(lang,module,numofattack,homedir)
        
        elif numofattack == 9:
            print(color.RED+'[-] Exit')
            sleep(1)
            sys.exit()
        elif numofattack == 7:
            from lib.lang import select_language
            select_language(homedir)
            lang = language(homedir)
            menu(lang,module,homedir)
        elif numofattack == 6:
            from lib.help import help_en
            help_en(lang, module, homedir)
        elif numofattack == 8:
            module = Modules(lang)
            menu(lang,module,homedir)

    elif lang == 'RUSSIAN':
        os.system('clear')
        design()
        print(color.GREEN+linec)
        print(color.YELLOW+'\n\tВыберите Атаку:')
        print(color.RED+'\n[1] ATTACK A')
        print('[2] ATTACK B')
        print('[3] ATTACK C')
        print('[4] ATTACK D')
        print('[5] ATTACK E')
        print(color.YELLOW+'\n[6] Помощь')
        print('[7] Сменить Язык')
        print('[8] Сменить Модуль')
        print('[9] Выход')
        print(color.GREEN+'\n'+linec)

        try:
            numofattack = int(input(color.CYAN+color.UNDERL+'\nWKBYA'+color.ENDC+' > '))
        except KeyboardInterrupt:
            print(color.YELLOW+'\n[*] Обнаруженно (CTRL + C)')
            sleep(1)
            print(color.RED+'[-] Выход')
            sys.exit()
        except ValueError:
            menu(lang,module,homedir)

        from lib.attack import attack

        if numofattack in range(1,6):
            attack(lang,module,numofattack,homedir)
        
        elif numofattack == 9:
            print(color.RED+'[-] Выход')
            sleep(1)
            sys.exit()
        elif numofattack == 7:
            from lib.lang import select_language
            select_language(homedir)
            lang = language(homedir)
            menu(lang,module,homedir)
        elif numofattack == 6:
            from lib.help import help_ru
            help_ru(lang, module, homedir)
        elif numofattack == 8:
            module = Modules(lang)
            menu(lang,module,homedir)

def language(homedir):
    with open(str(homedir+'/core/lang'), 'r') as f:
        numoflang = f.read()
    
    if numoflang == '1':
        lang = 'ENGLISH'
    elif numoflang == '2':
        lang = 'RUSSIAN'
    else:
        lang = 'UNKNOWN'

    return lang

def Modules(lang):
    from lib.module import menu

    module = menu(lang)
    return module