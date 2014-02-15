# $Id$ -- initializer

import json
import urllib2
import time

def getInfo(id, key):
  limit = id + 10
  while id < limit:
    encoder = json.JSONEncoder()
    id += 1 
    summoner_names_url = " https://prod.api.pvp.net/api/lol/na/v1.3/summoner/" + str(id) + "/name?api_key=" + key;
    data = json.load(urllib2.urlopen(summoner_names_url))
    # print data
    i = 0
    answer = ''
    doPrint =  True
    for part in encoder.iterencode(data):
      if(i == 1 or i == 3):
        if("IS" in part):
          doPrint = False
        answer +=  part +  " "
      i += 1
    answer =  answer.replace('"', '')
    if doPrint:
      print answer
  return id



#get stats by user id
#url = "https://prod.api.pvp.net/api/lol/na/v1.3/summoner/by-name/RiotSchmick?api_key=922e9aba-0917-477f-8ddd-392e716e70e6"

#get all champions:
championsUrl = "https://prod.api.pvp.net/api/lol/na/v1.1/champion?api_key=922e9aba-0917-477f-8ddd-392e716e70e6"
data = json.load(urllib2.urlopen(championsUrl))

#print data

# f = open("champions.txt", "w")
# f.write(str(data))
# print "written to champions.txt"
#37af0e1b-7079-4ae0-bd7e-573d4ff4fe61
id = 1
key1 = "e6d6726b-41fd-4ff8-b3ad-dd8354e75e97"
key2 = "37af0e1b-7079-4ae0-bd7e-573d4ff4fe61" 
while id < 1000:
  start = time.time()
  id = getInfo(id, key1)
  id = getInfo(id, key2)
  end = time.time()
  elapsed_time = ( end - start)
  if (elapsed_time < 10):
    time.sleep(10 - elapsed_time + .1)


