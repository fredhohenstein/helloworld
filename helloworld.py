# import boto3
# import pygame
# from pygame.locals import *

import time, sys, random
from time import sleep
import os  
import shutil

print("Hello World versie10!")
print("Sleeping for 5 seconds")
time.sleep(5)


cwd = os.getcwd()
print(cwd)


print("Sleeping for 2 seconds")
time.sleep(2)

with open("version", "r") as f:
    shutil.copyfileobj(f, sys.stdout)
