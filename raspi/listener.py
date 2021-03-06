#!/usr/bin/python3

import json
import sys
import urllib.request
import time
import random
from gpiozero import LED
from time import sleep


#wigwam is test server, listener.local is onsite techthulu - comment out the local to get the test server
#techURL = 'http://operation-wigwam.ingress.com:8080/v1/test-info'
techURL = 'http://listener.local:8080/v1/info'
pollInterval = 10
blueout = LED(2)
greenout = LED(3)
redout = LED(4)
pinkout = LED(5)
#LED(4).on()
#LED(5).on()
LED(6).on()
#LED(7).on()
LED(8).on()
LED(9).on()
LED(10).on()
LED(11).on()
LED(12).on()
LED(13).on()
LED(14).on()
LED(15).on()
LED(16).on()



def makeblue(level=8):
     blueout.on()
     greenout.off()
     redout.on()
     pinkout.on()
     print("portal is blue")
     statusfile = open('/tmp/statusfile',mode="w") 
     statusfile.write("blue"+str(level)+"\n")
     statusfile.close()

def makegreen(level=8):
     blueout.off()
     greenout.on()
     pinkout.on()
     redout.on()
     print("portal is green")
     statusfile = open('/tmp/statusfile',mode="w")
     statusfile.write("green"+str(level)+"\n")
     statusfile.close()

def makegray(level=0):
     blueout.off()
     greenout.off()
     for i in range(5): 
       pinkout.on()
       redout.on()
       time.sleep(int(1))
       pinkout.off()
       redout.off()
       time.sleep(int(1)) 

     print("portal is gray")
     statusfile = open('/tmp/statusfile',mode="w")
     statusfile.write("gray\n")
     statusfile.close()

def techthulu():
    try:
       print("retrieving from techthulu "+techURL)
       jsondata = urllib.request.urlopen(techURL).read().decode('utf-8')
       portalstate = json.loads(jsondata)
       if (portalstate['result']['controllingFaction'] == "Neutral"):
            makegray(portalstate['result']['level']) 
       if (portalstate['result']['controllingFaction'] == "Enlightened"):
            makegreen(portalstate['result']['level'])
       if (portalstate['result']['controllingFaction'] == "Resistance"):
            makeblue(portalstate['result']['level'])
       print("retrieval complete")
    except:
       print("retrieval from techthulu failed")
       controldata='party'
       party()

def forceblue():
     makeblue()    

def forcegreen():
     makegreen()

def forceneutral():
     makegray()

def party():
     print("party mode!")
     state = random.randint(0,2)
     print("party mode random state is: "+str(state))
     if (state == 2):
         makegreen(random.randint(1,8))
     if (state == 1):
         makeblue(random.randint(1,8))
     if (state == 0):
         makegray()

def main():
     curstate = "neutral"
     try:
          controlfile = open('/tmp/controlfile',mode="rt")
          controldata = controlfile.readline().rstrip("\n")
     except OSError:
          controldata='tech'

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
               controldata='tech'


main()
