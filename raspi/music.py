#!/usr/bin/python3

import json
import sys
import urllib.request
import time
import random
import os
from time import sleep

filebase = '/home/pi/listener-techthulu/sounds/'

def mpg123(file):
    os.system("mpg123 "+file)

def main():
  while(1==1):
    curstate="party"
    try:
        statusfile = open('/tmp/statusfile',mode="rt")
        curstate = statusfile.readline().rstrip("\n")
        statusfile.close()
    except OSError:
        curstate="party"

    curstate = curstate.replace('blue','R')
    curstate = curstate.replace('green','E')
    print("Current state is "+curstate+" playing song "+filebase+curstate+".mp3")
    mpg123(filebase+curstate+".mp3")
    time.sleep(1)


main()
