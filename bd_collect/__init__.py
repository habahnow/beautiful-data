# $Id$ -- initializer

import json
import urllib2
import time
import os.path

#get id and username while pasing out the data so that it only displays the id then a space, and the username
#ignores usersmanes that start with a capitol IS
def getInfo(id, key, f):
  limit = id + 9
  while id < limit:
    encoder = json.JSONEncoder()
    summoner_names_url = " https://prod.api.pvp.net/api/lol/na/v1.3/summoner/" + str(id) + "/name?api_key=" + key
    id += 1 
    data = json.load(urllib2.urlopen(summoner_names_url))
    # print data
    i = 0
    answer = ''
    doPrint =  True
    # json is iterated into parts. { , "1", :, "username", } being the 4 parts of any call.
    for part in encoder.iterencode(data):
      # print str(i) , " " , str(part)
      part = part.replace('"', '')
      if i == 1 or i == 3:
        # if the username starts with IS then the user does not work anymore
        if part.startswith("IS") and len(part) > 8: 
          doPrint = False
        answer +=  part +  " "
      i += 1
    if doPrint:
      answer += "\n"
      # print answer
      f.write(str(answer))
  return id

# incorrect = False
# username = ""
# while not incorrect:
#   username = input("Enter name, either daniel , alvaro, or eddie")
#   if "daniel" in username or "alvaro" in username or "eddie" in username:
#     incorrect = True
# incorrect = False



id  = 1
print "populating active summoners.txt with active players\n"
if os.path.isfile("active_summoners.txt"):
  f = open("active_summoners.txt", "r")
  for line in f:
    id = int(line.split()[0])
  f.close()
  key1 = "e6d6726b-41fd-4ff8-b3ad-dd8354e75e97" #daniel's key
# key2 = "37af0e1b-7079-4ae0-bd7e-573d4ff4fe61" #alvaro's key
# key3 = "922e9aba-0917-477f-8ddd-392e716e70e6" #eddie's key
  while True:
    print "do not press ctrl + c now or some changes to active_summoners.txt may not be saved\n"
    f = open("active_summoners.txt", "a")
    start = time.time()
    id = getInfo(id, key1, f)
    # id = getInfo(id, key2)
    # id = getInfo(id, key3)
    end = time.time()
    elapsed_time = ( end - start)
    f.close()
    print "press ctrl + c to exit program now to safely exit program and save changes\n"
    if (elapsed_time < 10):
      time.sleep(10 - elapsed_time + 1)

else:
  key1 = "e6d6726b-41fd-4ff8-b3ad-dd8354e75e97" #daniel's key
# key2 = "37af0e1b-7079-4ae0-bd7e-573d4ff4fe61" #alvaro's key
# key3 = "922e9aba-0917-477f-8ddd-392e716e70e6" #eddie's key
  while True:
    print "do not press ctrl + c now or some changes to active_summoners.txt may not be saved\n"
    f = open("active_summoners.txt", "w")
    start = time.time()
    id = getInfo(id, key1, f)
    # id = getInfo(id, key2)
    # id = getInfo(id, key3)
    end = time.time()
    elapsed_time = ( end - start)
    f.close()
    print "press ctrl + c to exit program now to safely exit program and save changes\n"
    if (elapsed_time < 10):
      time.sleep(10 - elapsed_time + 1)





