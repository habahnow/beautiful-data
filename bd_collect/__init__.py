# $Id$ -- initializer

import json
import urllib2
import time

#get stats by user id
#url = "https://prod.api.pvp.net/api/lol/na/v1.3/summoner/by-name/RiotSchmick?api_key=922e9aba-0917-477f-8ddd-392e716e70e6"

#get all champions:
championsUrl = "https://prod.api.pvp.net/api/lol/na/v1.1/champion?api_key=922e9aba-0917-477f-8ddd-392e716e70e6"
data = json.load(urllib2.urlopen(championsUrl))

#print data

f = open("champions.txt", "w")
f.write(str(data))
print "written to champions.txt"

x = 1
while x < 1000:
  x += 1 
  summoner_names_url = " https://prod.api.pvp.net/api/lol/na/v1.3/summoner/" + str(x) + "/name?api_key=e6d6726b-41fd-4ff8-b3ad-dd8354e75e97";
  data = json.load(urllib2.urlopen(summoner_names_url))
  print data
  if x % 10 == 0:
    time.sleep(10)