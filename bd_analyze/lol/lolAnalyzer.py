# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 23:45:05 2014

@author: Eddie
"""

import json 

key = '37af0e1b-7079-4ae0-bd7e-573d4ff4fe61'
idMinCollectId = 14
idMaxCollectId = 35

def printGamesJson(minId, maxId):
    id = minId
    while id < maxId:
        id += 1 
        try:
            f = open('../../bd_store/lol/gameData/' + str(id))
            data = json.load(f)
            print data
        except IOError:
            print 'no game file associated; skipping id' + str(id)

def printSummonersJson(minId, maxId):
    id = minId
    while id < maxId:
        id += 1 
        try:
            f = open('../../bd_store/lol/gameData/' + str(id))
            data = json.load(f)
            print data
        except IOError:
            print 'no game file associated; skipping id' + str(id)
            
            
def getRecentGameChampionIds(minId, maxId):
    championIds = []
    id = minId
    while id < maxId:
        id += 1 
        result =getRecentGameChampionIdsBySummonerId(id)
        if len(result) > 1:
            championIds.append(result)
    return championIds
def getRecentGameChampionIdsBySummonerId(summonerId):
       championIds = []
       try:
            f = open('../../bd_store/lol/gameData/' + str(summonerId))
            games = json.load(f)
            for game in games["games"]:
                championIds.append(game['championId'])
       except IOError:
            print 'no game file associated; skipping id' + str(summonerId)   
       return championIds
       
       
def getRecentSpellOneIds(minId, maxId):
    spellOneIds = []
    id = minId
    while id < maxId:
        id += 1 
        result = getRecentSpellOneIdsBySummonerId(id)
        if len(result) > 1:
            spellOneIds.append(result)
    return spellOneIds
def getRecentSpellOneIdsBySummonerId(summonerId):  
    spellOneIds = []
    try:
        f = open('../../bd_store/lol/gameData/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            spellOneIds.append(game['spell1'])
    except IOError:
        print 'no game file associated; skipping id' + str(summonerId)
    return spellOneIds
    
    
def getRecentSpellTwoIds(minId, maxId):
    spellTwoIds= []
    id = minId
    while id < maxId:
        id += 1 
        result = getRecentSpellTwoIdsBySummonerId(id)
        if len(result) > 1:
            spellTwoIds.append(result)
    return  spellTwoIds  
def getRecentSpellTwoIdsBySummonerId(summonerId):   
    spellTwoIds= []
    try:
        f = open('../../bd_store/lol/gameData/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            spellTwoIds.append(game['spell2'])
    except IOError:
        print 'no game file associated; skipping id' + str(summonerId)
    return  spellTwoIds
  
  
def getRecentGoldEarned(minId, maxId):
    recentGoldEarned= []
    id = minId
    while id < maxId:
        id += 1 
        result = getRecentGoldEarnedBySummonerId(id)
        if len(result) > 1:
            recentGoldEarned.append(result)
    return  recentGoldEarned
def getRecentGoldEarnedBySummonerId(summonerId):
    recentGoldEarned= []
    try:
        f = open('../../bd_store/lol/gameData/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentGoldEarned.append(stats['goldEarned'])
    except IOError:
        print 'no game file associated; skipping id' + str(summonerId)
    return  recentGoldEarned
    
    
def getRecentNumDeaths(minId, maxId):
    recentNumDeaths= []
    id = minId
    while id < maxId:
        id += 1 
        result = getRecentNumDeathsBySummonerId(id)
        if len(result) > 1:
            recentNumDeaths.append(result)
    return  recentNumDeaths   
def getRecentNumDeathsBySummonerId(summonerId):
    recentNumDeaths= []
    try:
        f = open('../../bd_store/lol/gameData/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentNumDeaths.append(stats['numDeaths'])
    except IOError:
        print 'no game file associated; skipping id' + str(summonerId)
    return  recentNumDeaths
    
    
def getRecentMinionsKilled(minId, maxId):
    recentMinionsKilled= []
    id = minId
    while id < maxId:
        id += 1 
        result = getRecentMinionsKilledBySummonerId(id)
        if len(result) > 1:
            recentMinionsKilled.append(result)
    return  recentMinionsKilled
def getRecentMinionsKilledBySummonerId(summonerId):
    recentMinionsKilled= []
    try:
        f = open('../../bd_store/lol/gameData/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentMinionsKilled.append(stats['minionsKilled'])
    except IOError:
        print 'no game file associated; skipping id' + str(summonerId)
    return  recentMinionsKilled
    
    
def getRecentgoldSpent(minId, maxId):
    recentGoldSpent= []
    id = minId
    while id < maxId:
        id += 1 
        result = getRecentGoldSpentBySummonerId(id)
        if len(result) > 1:
            recentGoldSpent.append(result)
    return  recentGoldSpent
def getRecentGoldSpentBySummonerId(summonerId):
    recentGoldSpent= []
    try:
        f = open('../../bd_store/lol/gameData/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentGoldSpent.append(stats['goldSpent'])
    except IOError:
        print 'no game file associated; skipping id' + str(summonerId)
    return  recentGoldSpent
    
    
def getRecentTotalDamageDealt(minId, maxId):
    recentTotalDamageDealt= []
    id = minId
    while id < maxId:
        id += 1 
        result = getRecentTotalDamageDealBySummonerId(id)
        if len(result) > 1:
            recentTotalDamageDealt.append(result)
    return  recentTotalDamageDealt
def getRecentTotalDamageDealBySummonerId(summonerId):
    recentTotalDamageDealt= []
    try:
        f = open('../../bd_store/lol/gameData/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentTotalDamageDealt.append(stats['totalDamageDealt'])
    except IOError:
        print 'no game file associated; skipping id' + str(summonerId)
    return  recentTotalDamageDealt
    

def getRecentTotalDamageTaken(minId, maxId):
    recentTotalDamageTaken= []
    id = minId
    while id < maxId:
        id += 1 
        result = getRecentTotalDamageTakenBySummonerId(id)
        if len(result) > 1:
            recentTotalDamageTaken.append(result)
    return  recentTotalDamageTaken
def getRecentTotalDamageTakenBySummonerId(summonerId):
    recentTotalDamageTaken= []
    try:
        f = open('../../bd_store/lol/gameData/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentTotalDamageTaken.append(stats['totalDamageTaken'])
    except IOError:
        print 'no game file associated; skipping id' + str(summonerId)
    return  recentTotalDamageTaken
    
    
def getRecentWins(minId, maxId):
    recentLargestKillingSprees= []
    id = minId
    while id < maxId:
        id += 1 
        result = getRecentWinsBySummonerId(id)
        if len(result) > 1:
            recentLargestKillingSprees.append(result)
    return  recentLargestKillingSprees
def getRecentWinsBySummonerId(summonerId):
    recentLargestKillingSprees= []
    try:
        f = open('../../bd_store/lol/gameData/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentLargestKillingSprees.append(stats['win'])
    except IOError:
        print 'no game file associated; skipping id' + str(summonerId)
    return  recentLargestKillingSprees
    
    
def getRecentTimesPlayed(minId, maxId):
    recentLargestKillingSprees= []
    id = minId
    while id < maxId:
        id += 1 
        result = getRecentTimesPlayedBySummonerId(id)
        if len(result) > 1:
            recentLargestKillingSprees.append(result)
    return  recentLargestKillingSprees
def getRecentTimesPlayedBySummonerId(summonerId):
    recentLargestKillingSprees= []
    try:
        f = open('../../bd_store/lol/gameData/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentLargestKillingSprees.append(stats['timePlayed'])
    except IOError:
        print 'no game file associated; skipping id' + str(summonerId)
    return  recentLargestKillingSprees
    
    
def getRecentSevenItems(minId, maxId):
    recentLargestKillingSprees= []
    id = minId
    while id < maxId:
        id += 1 
        result = getRecentSevenItemsBySummonerId(id)
        if len(result) > 1:
            recentLargestKillingSprees.append(result)
    return  recentLargestKillingSprees
def getRecentSevenItemsBySummonerId(summonerId):
    recentLargestKillingSprees= []
    try:
        f = open('../../bd_store/lol/gameData/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            try:
                item0 = stats['item0']
                recentLargestKillingSprees.append(item0)
            except:
                print 'no item 0'
            try:
                item1 = stats['item1']
                recentLargestKillingSprees.append(item1)
            except:
                print 'no item 1'
            try:
                item2 = stats['item2']
                recentLargestKillingSprees.append(item2)
            except:
                print 'no item 2'
            try:
                item3 = stats['item3']
                recentLargestKillingSprees.append(item3)
            except:
                print 'no item 3'
            try:
                item4 = stats['item4']
                recentLargestKillingSprees.append(item4)
            except:
                print 'no item 4'
            try:
                item5 = stats['item5']
                recentLargestKillingSprees.append(item5)
            except:
                print 'no item 5'
    except IOError:
        print 'no game file associated; skipping id' + str(summonerId)
    return  recentLargestKillingSprees
    
    
    
#printGames(key, idMinCollectId, idMaxCollectId)
#printSummoners(key, idMinCollectId, idMaxCollectId)
#print getRecentGameChampionIds(idMinCollectId, idMaxCollectId)
#print getRecentSpellOneIds(idMinCollectId, idMaxCollectId)
#print getRecentSpellTwoIds(idMinCollectId, idMaxCollectId)
#print getRecentGoldEarned(idMinCollectId, idMaxCollectId)
#print getRecentNumDeaths(idMinCollectId, idMaxCollectId)
#print getRecentMinionsKilled(idMinCollectId, idMaxCollectId)
#print getRecentgoldSpent(idMinCollectId, idMaxCollectId)
#print getRecentTotalDamageDealt(idMinCollectId, idMaxCollectId)
#print getRecentTotalDamageTaken(idMinCollectId, idMaxCollectId)
#print getRecentWins(idMinCollectId, idMaxCollectId)
#print getRecentTimesPlayed(idMinCollectId, idMaxCollectId)
#print getRecentSevenItems(idMinCollectId, idMaxCollectId)