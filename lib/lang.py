#Coded by ANOI

#Imports
from core.design import design
from core.color import color
from time import sleep
import readline
import sys
import os

readline.add_history
line = '----------------------------------'
linec = '####################################'

def select_language(homedir):
    os.system('clear')
    design()
    print(color.GREEN+linec)
    print(color.YELLOW+'\n\tSelect language:')
    print(color.RED+'\n[1] EN / ENGLISH')
    print(color.RED+'[2] RU / RUSSIAN')
    print(color.GREEN+'\n'+linec)
    try:
        lang = int(input(color.CYAN+color.UNDERL+'\nWKBYA'+color.ENDC+' > '))
        
        if lang == 1 or lang == 2:
            f = open(str(homedir+'/core/lang'), 'w')
            f.write(str(lang))
            f.close()

        else:
            os.system('clear')
            select_language(homedir)

    except ValueError:
        os.system('clear')
        select_language(homedir)
    
    except KeyboardInterrupt:
        print(color.YELLOW+'\n[*] Detected (CTRL + C)')
        sleep(1)
        print(color.RED+'[-] Exit')
        sys.exit()
