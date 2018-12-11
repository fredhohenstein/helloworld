# import boto3
# import pygame
# from pygame.locals import *

import time, sys, random
from time import sleep
import os  
import shutil

print("Hello World versie6!")
print("Sleeping for 5 seconds")
time.sleep(5)

with open("version", "r") as f:
    shutil.copyfileobj(f, sys.stdout)

print("Sleeping for 2 seconds")
time.sleep(2)
