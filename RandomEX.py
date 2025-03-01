# Random-EX Moudle of HonorVision(TM) Random Rall Call
# Powered By the DJSC Team.

import sys
import argparse
import random
import secrets
from time import sleep

# Consts

MODE_REPETITION_ALLOWED = 0
MODE_REPETITION_FORBIDDEN = 1

# Parameter reading

parser = argparse.ArgumentParser(description="Description")
parser.add_argument("-mode", type=int, default=MODE_REPETITION_ALLOWED)
parser.add_argument("-max", type=int, default=50)
parser.add_argument("-cnt", type=int, default=1)
args = parser.parse_args()

# Initialization

lst = []
sr = random.SystemRandom()

def randint(mode, max, cnt):
    for i in range(cnt):
        # sleep(random.SystemRandom().randint(0, 100) / 1200)
        num = sr.randint(1, max)
        if (mode == MODE_REPETITION_FORBIDDEN and num in lst):
            while (num in lst):
                sleep(secrets.randbelow(100) / 1000)
                num = sr.randint(1, max)
        lst.append(num)
        print(num)
        # sleep(random.randint(0, 100) / 1600)

if (__name__ == "__main__"):
    randint(args.mode, args.max, args.cnt)
    # randint(MODE_REPETITION_FORBIDDEN, 50, 50)
    # print(lst)
