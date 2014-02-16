import json
import urllib2
import time

def alvaro(key):
  # go through summary of stats
  # region
  region = 'na'
  # for each id, load the stats
  f = open("summoner_data.txt", "a")
  id = 14
  while id < 50:
    id += 1
    # /api/lol/{region}/v1.2/stats/by-summoner/{summonerId}/summary
    stats_url = 'https://prod.api.pvp.net/api/lol/'+ region + '/v1.2/stats/by-summoner/'+ str(id) +'/summary?api_key=' + key
    stats_info = json.load(urllib2.urlopen(stats_url))
    # print stats_info
    # formatted indents
    print json.dumps(stats_info, sort_keys=True, indent=2)
    f.write(str(stats_info))
    time.sleep(1)
  f.close()
key = "37af0e1b-7079-4ae0-bd7e-573d4ff4fe61"
alvaro(key)