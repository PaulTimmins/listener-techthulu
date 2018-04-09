#!/usr/bin/python3

import json
import sys
import urllib.request
import time

techURL = 'http://localhost:8081/module/status/json'
pollInterval = 10

def makeblue():
     print("portal is blue")

def makegreen():
     print("portal is green")

def makegray():
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


def main():
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

          print("sleeping for "+str(pollInterval)+" seconds\n")
          time.sleep(int(pollInterval))
          try:
               controlfile = open('/tmp/controlfile',mode="rt")
               controldata = controlfile.readline().rstrip("\n")
          except OSError:
               controldata=''


main()
