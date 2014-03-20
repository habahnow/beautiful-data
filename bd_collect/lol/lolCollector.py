# -*- coding: utf-8 -*-
"""
Created on Sat Mar 15 13:41:59 2014

@author: Eddie

this script downloads the 10000 files
"""

import urllib2
import time
import shutil

key = '37af0e1b-7079-4ae0-bd7e-573d4ff4fe61'
idMinCollectId = 14
idMaxCollectId= 35

def collectSummonerStats(key, minId, maxId):
  region = 'na'
  id = minId
  while id < maxId:
    id += 1
    #https://prod.api.pvp.net/api/lol/na/v1.2/stats/by-summoner/15/summary?api_key=37af0e1b-7079-4ae0-bd7e-573d4ff4fe61
    # /api/lol/{region}/v1.2/stats/by-summoner/{summonerId}/summary
    stats_url = 'https://prod.api.pvp.net/api/lol/'+ region + '/v1.2/stats/by-summoner/'+ str(id) +'/summary?api_key=' + key
    try:
        response = urllib2.urlopen(stats_url)
        f = open("../../bd_store/lol/summonerData/" + str(id), "w")
        shutil.copyfileobj(response, f)
        time.sleep(1)
        f.close()
    except IOError:
       print 'no stats associated; skipping id' + str(id)
def collectRecentGames(key, minId, maxId):
  #some of the calls to games return 404 errors if they have no games neccesitating error handling  
  region = 'na'
  id = minId
  while id < maxId:
    id += 1
    #https://prod.api.pvp.net/api/lol/na/v1.3/game/by-summoner/15/recent?api_key=e6d6726b-41fd-4ff8-b3ad-dd8354e75e97
    games_url = 'https://prod.api.pvp.net/api/lol/' + region + '/v1.3/game/by-summoner/' + str(id) + "/recent?api_key=" + key
    
    try: 
         #games_info = json.load(urllib2.urlopen(games_url))
         response = urllib2.urlopen(games_url)
         f = open("../../bd_store/lol/gameData/" + str(id), "w")
         shutil.copyfileobj(response, f)
         #f.write(str(games_info))
         #json.dump(games_info, f)
         time.sleep(1)
         f.close()
    except IOError:
       print 'no games associated; skipping id' + str(id)
       
#collectSummonerStats(key, idMinCollectId, idMaxCollectId)
#collectRecentGames(key, idMinCollectId, idMaxCollectId)

