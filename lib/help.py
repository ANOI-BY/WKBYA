#Coded by ANOI

from core.color import color
from time import sleep
import sys
import os

linec = '####################################'

def help_en(lang, module, homedir):
    os.system('clear')
    print(color.GREEN+linec)
    print(color.YELLOW+'\n\t HELP')
    print(color.ENDC+'[{}] Attack A: Sends authentication frames to all APs found in range. Too many clients can freeze or reset several APs. '.format(color.RED+str(1)+color.ENDC))
    print('[{}] Attack B: Sends beacon frames to show fake APs at clients. This can sometimes crash network scanners and even drivers!'.format(color.RED+str(2)+color.ENDC))
    print('[{}] Attack C: Reworked WiFi-jammer (Crash all networks around you)'.format(color.RED+str(3)+color.ENDC))
    print('[{}] Attack D: Sends deauthentication and disassociation packets to stations based on data traffic to disconnect all clients from an AP.'.format(color.RED+str(4)+color.ENDC))
    print('[{}] Attack E: Crashes the certain WiFi network'.format(color.RED+str(5)+color.ENDC))
    print(color.YELLOW+'\n[9] EXIT')
    print(color.GREEN+'\n'+linec)
    try:
        num = int(input(color.CYAN+color.UNDERL+'\nWKBYA'+color.ENDC+' > '))
    except KeyboardInterrupt:
        print(color.YELLOW+'\n[*] Detected (CTRL + C)')
        sleep(1)
        print(color.RED+'[-] Exit')
        sys.exit()
    if num == 9:
        from lib.menu import menu
        menu(lang, module, homedir)

def help_ru(lang,module,homedir):
    os.system('clear')
    print(color.GREEN+linec)
    print(color.YELLOW+'\n\t Помощь')
    print(color.ENDC+'[{}] Атака A: Отправляет фреймы аутентификации всем ТД найденным в диапазоне доступности. Слишком много клиентов может привести к зависанию или перезагрузке ТД. '.format(color.RED+str(1)+color.ENDC))
    print('[{}] Атака B: Отправляет фреймы маяков для создания видимости присутствия множества Точек Доступа. Это иногда может вывести из строя сканеры сети и драйверы!'.format(color.RED+str(2)+color.ENDC))
    print('[{}] Атака C: Переделанный скрипт WIFI-jammer (Глушит все WIFI точки в радиусе вашего WIFI адаптера)'.format(color.RED+str(3)+color.ENDC))
    print('[{}] Атака D: Отправляет пакеты деаутентификации и деассоциации станциям на основе трафика данных для отключения всех клиентов от ТД.'.format(color.RED+str(4)+color.ENDC))
    print('[{}] Атака E: Глушит определенную точку WIFI'.format(color.RED+str(5)+color.ENDC))
    print(color.YELLOW+'\n[9] EXIT')
    print(color.GREEN+'\n'+linec)
    try:
        num = int(input(color.CYAN+color.UNDERL+'\nWKBYA'+color.ENDC+' > '))
    except KeyboardInterrupt:
        print(color.YELLOW+'\n[*] Обнаруженно (CTRL + C)')
        sleep(1)
        print(color.RED+'[-] Выход')
        sys.exit()    
    if num == 9:
        from lib.menu import menu
        menu(lang, module, homedir)    