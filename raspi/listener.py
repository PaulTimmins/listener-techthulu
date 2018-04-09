#!/usr/bin/python3

import json
import sys
import urllib.request
import time

techURL = 'http://localhost:8081/module/status/json'

def techthulu():
    try:
       jsondata = urllib.request.urlopen(techURL).read().decode('utf-8')
       portalstate = json.loads(jsondata)
       if (portalstate['status']['controllingFaction'] == "0"):
            print("portal is neutral, do neutral stuff\n")
       if (portalstate['status']['controllingFaction'] == "1"):
            print("portal is ENL, do green stuff\n")
       if (portalstate['status']['controllingFaction'] == "2"):
            print("portal is RES, do blue stuff\n")
    except:
       print("retrieval from techthulu failed\n")

def main():
     try:
          controlfile = open('/tmp/controlfile',mode="rt")
          controldata = controlfile.readline().rstrip("\n")
     except OSError:
          controldata=''

     while (not controldata=='exit'):
          print(controldata+"\n")
          if (controldata == 'tech'):
               techthulu()
          time.sleep(10)
          try:
               controlfile = open('/tmp/controlfile',mode="rt")
               controldata = controlfile.readline().rstrip("\n")
          except OSError:
               controldata=''


main()
