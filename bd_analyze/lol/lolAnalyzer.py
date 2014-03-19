# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 23:45:05 2014

@author: Eddie
"""

import json 

key = '37af0e1b-7079-4ae0-bd7e-573d4ff4fe61'
idMinCollectId = 14
idMaxCollectId = 25

def printGames(key, minId, maxId):
    id = minId
    while id < maxId:
        id += 1 
        try:
            f = open('../../bd_store/lol/gameData/' + str(id))
            data = json.load(f)
            print data
        except IOError:
            print 'no game file associated; skipping id' + str(id)

def printSummoners(key, minId, maxId):
    id = minId
    while id < maxId:
        id += 1 
        try:
            f = open('../../bd_store/lol/gameData/' + str(id))
            data = json.load(f)
            print data
        except IOError:
            print 'no game file associated; skipping id' + str(id)

def printRecentGameIds(key, minId, maxId):
    id = minId
    while id < maxId:
        id += 1 
        try:
            f = open('../../bd_store/lol/gameData/' + str(id))
            games = json.load(f)
            for game in games["games"]:
                print game['gameId']
        except IOError:
            print 'no game file associated; skipping id' + str(id)
            
#printGames(key, idMinCollectId, idMaxCollectId)
#printSummoners(key, idMinCollectId, idMaxCollectId)
printRecentGameIds(key, 14, 15)