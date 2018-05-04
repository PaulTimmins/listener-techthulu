#!/usr/bin/python3

import json
import sys
import urllib.request
import time
import random
from gpiozero import LED
from time import sleep



#techURL = 'http://localhost:8081/module/status/json'
techURL = 'http://192.168.0.199:8081/module/status/json'
pollInterval = 10
blueout = LED(2)
greenout = LED(3)

def makeblue():
     blueout.on()
     greenout.off()
     print("portal is blue")

def makegreen():
     blueout.off()
     greenout.on()
     print("portal is green")

def makegray():
     blueout.off()
     greenout.off()
     print("portal is gray")

def techthulu():
    try:
       print("retrieving from techthulu "+techURL)
       jsondata = urllib.request.urlopen(techURL).read().decode('utf-8')
       portalstate = json.loads(jsondata)
       if (portalstate['status']['controllingFaction'] == "0"):
            makegray() 
       if (portalstate['status']['controllingFaction'] == "1"):
            makegreen()
       if (portalstate['status']['controllingFaction'] == "2"):
            makeblue()
       print("retrieval complete")
    except:
       print("retrieval from techthulu failed")

def forceblue():
     makeblue()    

def forcegreen():
     makegreen()

def forceneutral():
     makegray()

def party():
     print("party mode!")
     if (random.randint(1,2) > 1):
         makegreen()
     else:
         makeblue()


def main():
     curstate = "neutral"
     try:
          controlfile = open('/tmp/controlfile',mode="rt")
          controldata = controlfile.readline().rstrip("\n")
     except OSError:
          controldata=''

     while (not controldata=='exit'):
          print(controldata)
          if (controldata == 'tech'):
               techthulu()
          if (controldata == 'forceblue'):
               forceblue()
          if (controldata == 'forcegreen'):
               forcegreen()
          if (controldata == 'forceneutral'):
               forceneutral()
          if (controldata == 'party'):
               party()

          print("sleeping for "+str(pollInterval)+" seconds\n")
          time.sleep(int(pollInterval))
          try:
               controlfile = open('/tmp/controlfile',mode="rt")
               controldata = controlfile.readline().rstrip("\n")
          except OSError:
               controldata=''


main()
