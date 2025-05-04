# Random-EX Moudle of HonorVision(TM) Random Rall Call
# Version 1.6.0.13
# Powered By the DJSC Team.

import os
import sys
import argparse
import random
import secrets
from time import sleep
import traceback

# Consts

MODE_REPETITION_ALLOWED = 0
MODE_REPETITION_FORBIDDEN = 1

# Parameter reading

parser = argparse.ArgumentParser(description="Description")
parser.add_argument("-mode", type=int, default=MODE_REPETITION_ALLOWED)
parser.add_argument("-config", type=str, default="unknown")
parser.add_argument("-max", type=int, default=1)
parser.add_argument("-cnt", type=int, default=1)
args = parser.parse_args()

# Initialization

lst = []
sr = random.SystemRandom()
whitelist = []
namelist = []
cfgpath = os.path.dirname(os.path.abspath(__file__))
if (os.path.exists(cfgpath + "\\config") == False):
    cfgpath = os.path.dirname(cfgpath)

try:
    with open(cfgpath + "\\config\\lists\\" + args.config + "\\names", 'r') as config_names:
        # print(config_names.read())
        for name in config_names.readlines():
            if (name != '\n'):
                namelist.append(name.strip('\n'))
        # namelist = config_names.read().split('\n')
        # print(namelist)
except:
    traceback.print_exc()      

def randint(mode, max, cnt):
    for i in range(cnt):
        # sleep(random.SystemRandom().randint(0, 100) / 1200)
        num = sr.randint(1, max)
        if (mode == MODE_REPETITION_FORBIDDEN):
            while (num in lst) or (namelist[num - 1] == '-'):
                # sleep(secrets.randbelow(100) / 1000)
                num = sr.randint(1, max)
        else:
            while (namelist[num - 1] == '-'):
                num = sr.randint(1, max)
        lst.append(num)
        print(num)
        # sleep(random.randint(0, 100) / 1600)

if (__name__ == "__main__"):
    if (args.max == 1):
        randint(args.mode, len(namelist), args.cnt)
    else:
        randint(args.mode, args.max, args.cnt)
    # randint(MODE_REPETITION_FORBIDDEN, 50, 50)
    # print(lst)
