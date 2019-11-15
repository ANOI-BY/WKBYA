#!/usr/bin/env python3
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

############################

homedir = os.path.dirname(os.path.abspath(__file__))

############################

if os.path.isfile(str(homedir+'/core/lang')) == False:
    from lib.lang import select_language

    select_language(homedir)
else:
    pass

############################

def language():
    with open(str(homedir+'/core/lang'), 'r') as f:
        numoflang = f.read()
    
    if numoflang == '1':
        lang = 'ENGLISH'
    elif numoflang == '2':
        lang = 'RUSSIAN'
    else:
        lang = 'UNKNOWN'

    return lang

lang = language()

#############################

def Modules():
    from lib.module import menu

    module = menu(lang)
    return module
module = Modules()

#############################

def menu():
    from lib.menu import menu

    menu(lang, module, homedir)
menu()