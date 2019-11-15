#!/usr/bin/env python3
import os

dirname = os.path.dirname(os.path.abspath(__file__))

com_1 = f'chmod +x {dirname}/wkbya.py'
com_2 = f'chmod +x {dirname}/lib/wifijummer.py'
os.system(com_1)
os.system(com_2)