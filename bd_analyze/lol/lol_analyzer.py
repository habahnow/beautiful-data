# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 23:45:05 2014

@author: Eddie
"""

import json 
import numpy as np

key = '37af0e1b-7079-4ae0-bd7e-573d4ff4fe61'
idMinCollectId = 14
idMaxCollectId = 35

def printGamesJson(minId, maxId):
    id = minId
    while id < maxId:
        id += 1 
        try:
            f = open('../../bd_store/lol/game_data/' + str(id))
            data = json.load(f)
            print data
        except IOError:
            print 'no game file associated; skipping id' + str(id)

def printSummonersJson(minId, maxId):
    id = minId
    while id < maxId:
        id += 1 
        try:
            f = open('../../bd_store/lol/game_data/' + str(id))
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
            f = open('../../bd_store/lol/game_data/' + str(summonerId))
            games = json.load(f)
            for game in games["games"]:
                championIds.append(game['championId'])
       except IOError:
            pass  
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
        f = open('../../bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            spellOneIds.append(game['spell1'])
    except IOError:
        pass
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
        f = open('../../bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            spellTwoIds.append(game['spell2'])
    except IOError:
        pass
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
        f = open('../../bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentGoldEarned.append(stats['goldEarned'])
    except IOError:
        pass
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
        f = open('../../bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            try:
                recentNumDeaths.append(stats['numDeaths'])
            except: 
                pass            
    except IOError:
        pass
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
        f = open('../../bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentMinionsKilled.append(stats['minionsKilled'])
    except IOError:
        pass
    return  recentMinionsKilled
    
    
def getRecentGoldSpent(minId, maxId):
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
        f = open('../../bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentGoldSpent.append(stats['goldSpent'])
    except IOError:
        pass
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
        f = open('../../bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentTotalDamageDealt.append(stats['totalDamageDealt'])
    except IOError:
        pass
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
        f = open('../../bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentTotalDamageTaken.append(stats['totalDamageTaken'])
    except IOError:
        pass
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
        f = open('../../bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentLargestKillingSprees.append(stats['win'])
    except IOError:
        pass
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
        f = open('../../bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentLargestKillingSprees.append(stats['timePlayed'])
    except IOError:
        pass
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
        f = open('../../bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            try:
                item0 = stats['item0']
                recentLargestKillingSprees.append(item0)
            except:
                pass
            try:
                item1 = stats['item1']
                recentLargestKillingSprees.append(item1)
            except:
                pass
            try:
                item2 = stats['item2']
                recentLargestKillingSprees.append(item2)
            except:
                pass
            try:
                item3 = stats['item3']
                recentLargestKillingSprees.append(item3)
            except:
                pass
            try:
                item4 = stats['item4']
                recentLargestKillingSprees.append(item4)
            except:
                pass
            try:
                item5 = stats['item5']
                recentLargestKillingSprees.append(item5)
            except:
                pass
    except IOError:
        pass
    return  recentLargestKillingSprees
    
    
def getMaxDeaths():
    return np.min(getRecentNumDeaths(idMinCollectId, idMaxCollectId))

def getMinDeaths():
    return np.min(getRecentNumDeaths(idMinCollectId, idMaxCollectId))

def getAvgMinionsKilled():
    return np.average(getRecentMinionsKilled(idMinCollectId, idMaxCollectId))
    
def getAvgGoldSpent():
    return np.average(getRecentGoldSpent(idMinCollectId, idMaxCollectId))
    
def getMinGoldSpent():
    return np.min(getRecentGoldSpent(idMinCollectId, idMaxCollectId))
    
def getMaxGoldSpent():
    return np.max(getRecentGoldSpent(idMinCollectId, idMaxCollectId))
    
def getAvgGoldEarned():
    return np.average(getRecentGoldEarned(idMinCollectId, idMaxCollectId))
    
def getMaxGoldEarned():
    return np.max(getRecentGoldEarned(idMinCollectId, idMaxCollectId))

def getMinGoldEarned():
    return np.min(getRecentGoldEarned(idMinCollectId, idMaxCollectId))
    
def getAvgTotalDamageDealt():
    return np.average(getRecentTotalDamageDealt(idMinCollectId, idMaxCollectId))
    
def getMaxTotalDamageDealt():
    return np.max(getRecentTotalDamageDealt(idMinCollectId, idMaxCollectId))
    
def getMinTotalDamageDealt():
    return np.min(getRecentTotalDamageDealt(idMinCollectId, idMaxCollectId))
    
def getAvgTotalDamageTaken():
    return np.average(getRecentTotalDamageTaken(idMinCollectId, idMaxCollectId))
    
def getMaxTotalDamageTaken():
    return np.max(getRecentTotalDamageTaken(idMinCollectId, idMaxCollectId))
    
def getMinTotalDamageTaken():
    return np.min(getRecentTotalDamageTaken(idMinCollectId, idMaxCollectId))
    
def getAvgWins():
    return np.min(getRecentWins(idMinCollectId, idMaxCollectId))
    
def getAvgTimePlayed():
    return np.min(getRecentTimesPlayed(idMinCollectId, idMaxCollectId))
    
def getMaxTimePlayed():
    return np.max(getRecentTimesPlayed(idMinCollectId, idMaxCollectId))
    
def getMinTimePlayed():
    return np.min(getRecentTimesPlayed(idMinCollectId, idMaxCollectId))
    
def getSummonerAvgGoldEarnings():
    summonerAvgGoldEarnings = []
    results = getRecentGoldEarned(idMinCollectId, idMaxCollectId)
    for result in results:
        summonerAvgGoldEarnings.append(np.average(result))
    return summonerAvgGoldEarnings
    
def getSummonerAvgGoldSpendings():
    summonerAvgGoldSpendings = []
    results = getRecentGoldSpent(idMinCollectId, idMaxCollectId)
    for result in results:
        summonerAvgGoldSpendings.append(np.average(result))
    return summonerAvgGoldSpendings
    
def getSummonerAvgNumDeaths():
    summonerAvgNumDeaths = []
    results = getRecentNumDeaths(idMinCollectId, idMaxCollectId)
    for result in results:
        summonerAvgNumDeaths.append(round(np.average(result)))
    return summonerAvgNumDeaths
    
def getSummonerAvgMinionsKilled():
    summonerAvgMinionsKilled = []
    results = getRecentMinionsKilled(idMinCollectId, idMaxCollectId)
    for result in results:
        summonerAvgMinionsKilled.append(round(np.average(result)))
    return summonerAvgMinionsKilled
    
def getSummonerAvgTotalDamageDealt():
    summonerAvgTotalDamageDealt = []
    results = getRecentTotalDamageDealt(idMinCollectId, idMaxCollectId)
    for result in results:
        summonerAvgTotalDamageDealt.append(np.average(result))
    return summonerAvgTotalDamageDealt
    
def getSummonerAvgTotalDamageTaken():
    summonerAvgTotalDamageTaken = []
    results = getRecentTotalDamageTaken(idMinCollectId, idMaxCollectId)
    for result in results:
        summonerAvgTotalDamageTaken.append(np.average(result))
    return summonerAvgTotalDamageTaken
    
def getSummonerWinRatio():
    summonerAvgWins = []
    results = getRecentWins(idMinCollectId, idMaxCollectId)
    for result in results:
        summonerAvgWins.append(round(np.average(result), 2))
    return summonerAvgWins 
    
def getSummonerAvgTimePlayedInMinutes():
    summonerAvgTimePlayedInMinutes = []
    results = getRecentTimesPlayed(idMinCollectId, idMaxCollectId)
    for result in results:
        summonerAvgTimePlayedInMinutes.append(round(np.average(result), 3)/ 60.0)
    return summonerAvgTimePlayedInMinutes 
    
#printGamesJson(idMinCollectId, idMaxCollectId)
#printSummonersJson(idMinCollectId, idMaxCollectId)
#print getRecentGameChampionIds(idMinCollectId, idMaxCollectId)
#print getRecentSpellOneIds(idMinCollectId, idMaxCollectId)
#print getRecentSpellTwoIds(idMinCollectId, idMaxCollectId)
#print getRecentGoldEarned(idMinCollectId, idMaxCollectId)
#print getRecentNumDeaths(idMinCollectId, idMaxCollectId)
#print getRecentMinionsKilled(idMinCollectId, idMaxCollectId)
#print getRecentGoldSpent(idMinCollectId, idMaxCollectId)
#print getRecentTotalDamageDealt(idMinCollectId, idMaxCollectId)
#print getRecentTotalDamageTaken(idMinCollectId, idMaxCollectId)
#print getRecentWins(idMinCollectId, idMaxCollectId)
#print getRecentTimesPlayed(idMinCollectId, idMaxCollectId)
#print getRecentSevenItems(idMinCollectId, idMaxCollectId)
#print getSummonerAvgGoldEarnings()
#print getSummonerAvgGoldSpendings()
#print getSummonerAvgNumDeaths()
#print getSummonerAvgMinionsKilled()
#print getSummonerAvgTotalDamageDealt()
#print getSummonerAvgTotalDamageTaken()
#print getSummonerWinRatio()
#print getSummonerAvgTimePlayedInMinutes()

