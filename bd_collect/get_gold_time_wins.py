
import json
import urllib2
import time
from sklearn import linear_model

f = open("active_summoners.txt" , "r")
valid_ids = []
for line in f:
  valid_ids.append(int(line.split()[0]))
f.close()
# print valid_ids
# print valid_ids[len(valid_ids) - 1] + valid_ids[len(valid_ids) - 2]
# for i in valid_ids:
#   print i

x = []
y  = []
for i in valid_ids:
  # key1 = "e6d6726b-41fd-4ff8-b3ad-dd8354e75e97"
  key1 = "37af0e1b-7079-4ae0-bd7e-573d4ff4fe61"
  game_type = "https://prod.api.pvp.net/api/lol/na/v1.3/game/by-summoner/" + str(i) + "/recent?api_key=" + key1
  start = time.time()
  print i
  if i > 20:
    break
  try:
    data = json.load(urllib2.urlopen(game_type))
    end = time.time()
    time.sleep(1.5)
    # print data["games"][0].keys()
    for part in data["games"]:
      if "MATCHED_GAME" in part[ u'gameType'] and "CLASSIC" in part[u'gameMode']:
        stats = part[u'stats']
        time_played = stats[u'timePlayed']
        gold_spent = stats[u'goldSpent']
        # print gold_spent , " time_played: " , time_played
        x.append(gold_spent)
        y.append(time_played)
        # print part[u'stats']
        # print type(part[u'stats'])
      # if "NORMAL" in part[u'subtype'] or  "RANKED_SOLO_5X5" in part[u'subtype'] or "RANKED_PREMADE_5x5 " in part[u'subtype'] \
      #  or  "RANKED_TEAM_5x5" in part[u'subtype']:
        print "wok"
  except urllib2.HTTPError, e: 
    print "omg"
print x


regr = linear_model.LinearRegression()

regr.fit(x, y)
print regr.intercept_

# py.xlabel("iterations")
# pl.ylabel("Cost")
# pl.plot(Resu)
  # for line in part.split("\n"):
  #   if "gameType" in line and "MATCHED_GAME" in line:
  #     print line # print part # print data["games"] = "game_type"