# $Id$ -- initializer

import json
import urllib2

#get stats by user id
#url = "https://prod.api.pvp.net/api/lol/na/v1.3/summoner/by-name/RiotSchmick?api_key=922e9aba-0917-477f-8ddd-392e716e70e6"

#get all champions:
championsUrl = "https://prod.api.pvp.net/api/lol/na/v1.1/champion?api_key=922e9aba-0917-477f-8ddd-392e716e70e6"
data = json.load(urllib2.urlopen(championsUrl))

print data

f = open("champions.txt", "w")
f.write(str(data))
print "written to champions.txt"

