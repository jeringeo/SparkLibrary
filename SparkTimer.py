from __future__ import division
import time
startTime = 0

def startClock(tag=None):
    global startTime
    if(tag!=None): print(tag)
    startTime = time.time()

def printElapsedTime(tag = None):
    if(tag==None): tag =''
    print(tag,' ',round((time.time()-startTime)*1000000)/1000000)

#add a function which gives cumulative time for a key, so that it can act as a profiler: