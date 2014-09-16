'''
Created on Sep 16, 2014

@author: Debanjan Mahata
'''

from math import radians, cos, sin, asin, sqrt
from datetime import datetime
from nltk import FreqDist
import sys


def getDayDifference(time1, time2):
    """get the difference in days between two given datetime stamps"""
    dayDiff = time2-time1
    return dayDiff.days


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 

    # 6367 km is the radius of the Earth
    km = 6367 * c
    return km 


def getFreqDist(pylist):
    """method for counting the frequency of occurrences of elements in a given list
    Outputs a Python dictionary with the element names as keys and element counts as values"""
    return FreqDist(pylist)


def sortDictByValueAscending(pythonDict):
    """sorts a python dictionary in ascending order"""
    return sorted([(value,key)for (key, value) in pythonDict.items()])


def sortDictByValueDescending(pythonDict):
    """sorts a python dictionary in a descending order"""
    return sorted([(value,key)for (key, value) in pythonDict.items()])[::-1]


def outputForDict(outputFile,pyDict):
    """"method for writing to a given output file the information from a python dictionary with the entries being in the 
    following format
    pythonDictKey|correspondingValue 
    pythonDictKey|correspondingValue
    pythonDictKey|correspondingValue
    ........
    """
    sys.stdout = open(outputFile,"w")
    for item, freq in pyDict.iteritems():
        try:
            print(str(item)+"|"+str(freq))
        except:
            pass
        
def outputSortedDict(outputFile,sortedPyDict):
    """method for writing to a given output file the information from a python list consisting of the values of a sorted dictionary
    in the given format
    key|value
    key|value
    ....
    """
    sys.stdout = open(outputFile,"w")
    for entries in sortedPyDict:
        try:
            print(entries[1].encode("utf-8")+"|"+str(entries[0]))
        except:
            pass



