# import boto3
# import pygame
# from pygame.locals import *

import time, sys, random
from time import sleep
import os  
import shutil


print("Hello World! voor Luuk Krijen en Fred")
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
