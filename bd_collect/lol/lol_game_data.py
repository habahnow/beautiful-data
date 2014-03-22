from urllib2 import urlopen, HTTPError, URLError
from json import load, dump
import numpy as np
from time import sleep
import lol_items as it

key = '37af0e1b-7079-4ae0-bd7e-573d4ff4fe61'

# keys
"""
96098619-ca31-4f65-a958-f3ca476a5899
fc4b3d86-980f-4f6a-809e-2a08e4ff23ba
66343224-0d43-4d60-a3a4-b23924dca063
4c74b93f-712c-45f6-9e29-d988f1b38fea
fb9131ad-1482-4d6d-952a-d97b9a7450f3

a33b41f5-3bdd-4eb6-bad4-db7e58d1e318
ff1b861d-77e7-4367-aa88-7229f27f0405
0cc519d6-5e7b-4ac0-98cf-fb5ce311ab19
bfac29fd-a69a-4434-b8a1-e40a57fe145f
f2176cca-baf7-4a25-b004-2003198c4931

"""

def getKey(iterr):
	# not including Eddie, Danie, or Alvaro key
	list_keys = ['96098619-ca31-4f65-a958-f3ca476a5899',
'fc4b3d86-980f-4f6a-809e-2a08e4ff23ba',
'66343224-0d43-4d60-a3a4-b23924dca063',
'4c74b93f-712c-45f6-9e29-d988f1b38fea',
'fb9131ad-1482-4d6d-952a-d97b9a7450f3',

'a33b41f5-3bdd-4eb6-bad4-db7e58d1e318',
'ff1b861d-77e7-4367-aa88-7229f27f0405',
'0cc519d6-5e7b-4ac0-98cf-fb5ce311ab19',
'bfac29fd-a69a-4434-b8a1-e40a57fe145f',
'f2176cca-baf7-4a25-b004-2003198c4931']
	for i in range(len(list_keys)):
		print list_keys[iterr%10]
		return list_keys[iterr%10]
		


# Eddie's code for Min/Max call
def collectGameDataRange(key, minId, maxId):
	#some of the calls to games return 404 errors if they have no games neccesitating error handling  
	region = 'na'
	id = minId
	while id < maxId:
		id += 1
		genkey = getKey(id)
    	# https://prod.api.pvp.net/api/lol/na/v1.3/game/by-summoner/2/recent?api_key=e6d6726b-41fd-4ff8-b3ad-dd8354e75e97
		url = 'https://prod.api.pvp.net/api/lol/' + region + '/v1.3/game/by-summoner/' + str(id) + "/recent?api_key="
		url = url + genkey
		
		try: 
	         response = urlopen(url)
	         json_obj = load(response)
	         print id, " is valid ID"
	         f = open("../../bd_store/lol/gameData/" + str(id), "w")
	         dump(json_obj, f)
	         sleep(0.1)
	         f.close()
		except HTTPError, e:
			print e.code
			# code is not valid go back and check another id
			sleep(0.1)
			continue
		except URLError, e:
			print e.args
def collectRecentGameData(key, numberGames):
	# base url + api key param
	region = 'na'
	for i in range(numberGames):
		url = 'https://prod.api.pvp.net/api/lol/' + region + '/v1.3/game/by-summoner/'+ str(i) +'/recent?api_key='
		# this is where the key is inserted; deleted due to aggreement policy

		url = url + key
		# print url
		# https://prod.api.pvp.net/api/lol/na/v1.3/game/by-summoner/0/recent?api_key=37af0e1b-7079-4ae0-bd7e-573d4ff4fe61
		try:
			response = urlopen(url)
			json_obj = load(response)
			print i, " is valid ID"
			# parse our story
			#f1 = open("../../bd_store/lol/gameData/recent_game_bysummoner.txt", "rb")
			f = open("../../bd_store/lol/gameData/" + str(i), "w")
			dump(json_obj, f)
			sleep(1.2)
			f.close()
		except HTTPError, e:
			print e.code
			# code is not valid go back and check another id
			sleep(1)
			continue
		except URLError, e:
			print e.args
	print "Only VALID recent game data has been saved to files by Id.."
# gets the recent game data for ids
# collectRecentGameData(key, 3000)


# retrieve data from file by summonerId
def recentGameData(summonerId):
	try:
		f = open("../../bd_store/lol/gameData/" + str(summonerId))
		game = load(f)
	except IOError:
		print 'No file with name'
	return game


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
    items = []
    try:
        f = open('../../bd_store/lol/gameData/' + str(summonerId))
        games = load(f)
        for game in games["games"]:
            stats =  game['stats']
            try:
                items.append(stats['item0'])
            except:
                print 'no item 0'
            try:
                items.append(stats['item1'])
            except:
                print 'no item 1'
            try:
                items.append(stats['item2'])
            except:
                print 'no item 2'
            try:
                items.append(stats['item3'])
            except:
                print 'no item 3'
            try:
                items.append(stats['item4'])
            except:
                print 'no item 4'
            try:
                items.append(stats['item5'])
            except:
                print 'no item 5'
            try:
                items.append(stats['item6'])
            except:
                print 'no item 6'
    except IOError:
        print 'no game file associated; skipping id' + str(summonerId)
    return  items

"""
itemsData = it.getItemsData()
print itemsData['data']['3157']['name']
for i in range(5):
	items = getRecentSevenItemsBySummonerId(i)
	for item in items:
		print 'ID:', str(i) , item


# call & print
x = recentGameData(15000)

for game in x["games"]:
	print game["gameId"], game["championId"]
# items['data'][str(id)]['name']
# collectGameDataRange(key, 30000, 50000)
# so far 15,000 files have been saved

"""
# got values from 100,000, 150,000
# collectGameDataRange(key, 100000, 105000)



