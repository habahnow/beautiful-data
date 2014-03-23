"""
CS 454 Big Data
Eddie Arevalo
Alvaro Ortiz
Daniel Soto
"""

from urllib2 import urlopen, HTTPError, URLError
from json import load, dump
import numpy as np
from time import sleep

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
def collectGameDataRange(minId, maxId):
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
	         f = open("bd_store/lol/gameData/" + str(id), "w")
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
		except IOError, e:
			print e.args


			
