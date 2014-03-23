"""
CS 454 Big Data
Eddie Arevalo
Alvaro Ortiz
Daniel Soto
"""

import json 
import numpy as np

key = '37af0e1b-7079-4ae0-bd7e-573d4ff4fe61'
idMinCollectId = 14
idMaxCollectId = 40000

def printGamesJson(minId, maxId):
    id = minId
    while id < maxId:
        id += 1 
        try:
            #f = open('../bd_store/lol/game_data/' + str(id))
            f = open('bd_store/lol/game_data/' + str(id))
            data = json.load(f)
            print data
        except IOError:
            print 'no game file associated; skipping id' + str(id)

def printSummonersJson(minId, maxId):
    id = minId
    while id < maxId:
        id += 1 
        try:
            f = open('bd_store/lol/game_data/' + str(id))
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
            f = open('bd_store/lol/game_data/' + str(summonerId))
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
        f = open('bd_store/lol/game_data/' + str(summonerId))
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
        f = open('bd_store/lol/game_data/' + str(summonerId))
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
            recentGoldEarned = recentGoldEarned + result
    return  recentGoldEarned
def getRecentGoldEarnedBySummonerId(summonerId):
    recentGoldEarned= []
    try:
        f = open('bd_store/lol/game_data/' + str(summonerId))
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
        f = open('bd_store/lol/game_data/' + str(summonerId))
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
        f = open('bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            try:
                recentMinionsKilled.append(stats['minionsKilled'])
            except:
                pass          
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
        f = open('bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            try:
                recentGoldSpent.append(stats['goldSpent'])
            except:
                pass
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
        f = open('bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            try:
                recentTotalDamageDealt.append(stats['totalDamageDealt'])
            except:
                pass
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
        f = open('bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            try:
                recentTotalDamageTaken.append(stats['totalDamageTaken'])
            except:
                pass
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
        f = open('bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            recentLargestKillingSprees.append(stats['win'])
    except IOError:
        pass
    return  recentLargestKillingSprees
    
    
def getRecentTimesPlayed(minId, maxId):
    recent_times_played_list= []
    id = minId
    while id < maxId:
        id += 1 
        result = getRecentTimesPlayedBySummonerId(id)
        if len(result) > 1:
            recent_times_played_list = recent_times_played_list + result

    answer = np.array(recent_times_played_list)
    return recent_times_played_list
def getRecentTimesPlayedBySummonerId(summonerId):
    getRecentTimesPlayedBySummonerId= []
    try:
        f = open('bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            stats =  game['stats']
            getRecentTimesPlayedBySummonerId.append(stats['timePlayed'])
    except IOError:
        pass
    return  getRecentTimesPlayedBySummonerId
    
def getRecentDatesPlayed(minId, maxId):
    recentDatesPlayed= []
    id = minId
    while id < maxId:
        id += 1 
        result = getRecentDatesPlayedBySummonerId(id)
        if len(result) > 1:
            recentDatesPlayed.append(result)
    return  recentDatesPlayed
def getRecentDatesPlayedBySummonerId(summonerId):
    recentDatesPlayed= []
    try:
        f = open('bd_store/lol/game_data/' + str(summonerId))
        games = json.load(f)
        for game in games["games"]:
            recentDatesPlayed.append(game['createDate'])          
    except IOError:
        pass
    return  recentDatesPlayed
    
    
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
        f = open('bd_store/lol/game_data/' + str(summonerId))
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
    numDeaths = []
    for death in getRecentNumDeaths(idMinCollectId, idMaxCollectId):
        numDeaths.append(np.max(death))
    return np.max(numDeaths)

def getMinDeaths():
    numDeaths = []
    for death in getRecentNumDeaths(idMinCollectId, idMaxCollectId):
        numDeaths.append(np.min(death))
    return np.min(numDeaths)
    
def getAvgDeaths():
    numDeaths = []
    for death in getRecentNumDeaths(idMinCollectId, idMaxCollectId):
        numDeaths.append(np.average(death))
    return round(np.average(numDeaths))

def getAvgMinionsKilled():
    elements = []
    for element in getRecentMinionsKilled(idMinCollectId, idMaxCollectId):
        elements.append(np.average(element))
    return round(np.average(elements))

def getMaxMinionsKilled():
    elements = []
    for element in getRecentMinionsKilled(idMinCollectId, idMaxCollectId):
        elements.append(np.max(element))
    return round(np.max(elements))
    
def getAvgGoldSpent():
    elements = []
    for element in getRecentGoldSpent(idMinCollectId, idMaxCollectId):
        elements.append(np.average(element))
    return round(np.average(elements))
    
def getMinGoldSpent():
    elements = []
    for element in getRecentGoldSpent(idMinCollectId, idMaxCollectId):
        elements.append(np.min(element))
    return round(np.min(elements))
    
def getMaxGoldSpent():
    elements = []
    for element in getRecentGoldSpent(idMinCollectId, idMaxCollectId):
        elements.append(np.max(element))
    return round(np.max(elements))
    
def getAvgGoldEarned():
    elements = []
    for element in getRecentGoldEarned(idMinCollectId, idMaxCollectId):
        elements.append(np.average(element))
    return round(np.average(elements))
    
def getMaxGoldEarned():
    elements = []
    for element in getRecentGoldEarned(idMinCollectId, idMaxCollectId):
        elements.append(np.max(element))
    return round(np.max(elements))

def getMinGoldEarned():
    elements = []
    for element in getRecentGoldEarned(idMinCollectId, idMaxCollectId):
        elements.append(np.min(element))
    return round(np.min(elements))
    
def getAvgTotalDamageDealt():
    elements = []
    for element in getRecentTotalDamageDealt(idMinCollectId, idMaxCollectId):
        elements.append(np.average(element))
    return round(np.average(elements))
    
def getMaxTotalDamageDealt():
    elements = []
    for element in getRecentTotalDamageDealt(idMinCollectId, idMaxCollectId):
        elements.append(np.max(element))
    return round(np.max(elements))
    
def getMinTotalDamageDealt():
    elements = []
    for element in getRecentTotalDamageDealt(idMinCollectId, idMaxCollectId):
        elements.append(np.min(element))
    return round(np.min(elements))
    
def getAvgTotalDamageTaken():
    elements = []
    for element in getRecentTotalDamageTaken(idMinCollectId, idMaxCollectId):
        elements.append(np.average(element))
    return round(np.average(elements))
    
def getMaxTotalDamageTaken():
    elements = []
    for element in getRecentTotalDamageTaken(idMinCollectId, idMaxCollectId):
        elements.append(np.max(element))
    return round(np.max(elements))
    
def getMinTotalDamageTaken():
    elements = []
    for element in getRecentTotalDamageTaken(idMinCollectId, idMaxCollectId):
        elements.append(np.min(element))
    return round(np.min(elements))
    
def getAvgTimePlayed():
    elements = []
    for element in getRecentTimesPlayed(idMinCollectId, idMaxCollectId):
        elements.append(np.average(element))
    get = np.array(elements)
    return round(np.average(elements))
    
def getMaxTimePlayed():
    elements = []
    for element in getRecentTimesPlayed(idMinCollectId, idMaxCollectId):
        elements.append(np.max(element))
    return round(np.max(elements))
    
def getMinTimePlayed():
    elements = []
    for element in getRecentTimesPlayed(idMinCollectId, idMaxCollectId):
        elements.append(np.min(element))
    return round(np.min(elements))
    
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
        summonerAvgTimePlayedInMinutes.append(round(np.average(result) /  60.0))
    return summonerAvgTimePlayedInMinutes 
# maxDamage    
def getSummonerMaxDamageDealt():
    summonerMaxDamage = []
    results = getRecentTotalDamageDealt(idMinCollectId, idMaxCollectId)
    for result in results:
        maxe = max(np.array(result))
        summonerMaxDamage.append(maxe)
    return summonerMaxDamage
def getArcTan(x, y):
    return np.arctan2(y, x)

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
#print getRecentDatesPlayed(idMinCollectId, idMaxCollectId)
#print getRecentSevenItems(idMinCollectId, idMaxCollectId)
#print getMaxDeaths()
#print getMinDeaths()
#print getAvgDeaths()
#print getAvgMinionsKilled()
#print getMaxMinionsKilled()
#print getAvgGoldSpent()
#print getMinGoldSpent()
#print getMaxGoldSpent()
#print getAvgGoldEarned()
#print getMinGoldEarned()
#print getMaxGoldEarned()
#print getAvgTotalDamageDealt()
#print getMinTotalDamageDealt()
#print getMaxTotalDamageDealt()
#print getAvgTotalDamageTaken()
#print getMinTotalDamageTaken()
#print getMaxTotalDamageTaken()
# getAvgTimePlayed()
#print getMinTimePlayed()
# print getMaxTimePlayed()
#print getSummonerAvgTimePlayedInMinutes()
#print getSummonerAvgMinionsKilled()
#print getSummonerAvgGoldEarnings()
#print getSummonerAvgGoldSpendings()
#print getSummonerAvgNumDeaths()
#print getSummonerAvgTotalDamageDealt()
#print getSummonerAvgTotalDamageTaken()
#print getSummonerWinRatio()
