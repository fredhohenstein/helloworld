# import boto3
# import pygame
# from pygame.locals import *

import time, sys, random
from time import sleep
import os  
import shutil
from math import factorial
from decimal import Decimal, getcontext

def calc(n):
    t= Decimal(0)
    pi = Decimal(0)
    deno= Decimal(0)

    for k in range(n):
        t = ((-1)**k)*(factorial(6*k))*(13591409+545140134*k)
        deno = factorial(3*k)*(factorial(k)**3)*(640320**(3*k))
        pi += Decimal(t)/Decimal(deno)
    pi = pi * Decimal(12) / Decimal(640320 ** Decimal(1.5))
    pi = 1/pi
    return pi


print("Hello World!")
with open("d:\\runpyprograms\\helloworld\\version", "r") as f:
    shutil.copyfileobj(f, sys.stdout)

print("Sleeping for 5 seconds")
time.sleep(5)

cwd = os.getcwd()
print("Current directory", cwd)
print(sys.path)
print(os.environ)

print("Sleeping for 2 seconds")
time.sleep(2)

# Chudnovsky algorithm for figuring out pi
getcontext().prec=100
n=5
print calc(n)
