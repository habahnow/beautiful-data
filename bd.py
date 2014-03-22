#!/usr/bin/python

import argparse
from collections import defaultdict
from bd_visualize import lol_visualize
from bd_analyze import lol_analyzer



debug = False

def parseArguments():
    parser = argparse.ArgumentParser(usage='%(prog)s [options]',
                                     description='bd application')

    parser.add_argument('--debug', action='store_true', default=False)

    parser.add_argument('-m', '--min-area', dest='minArea', type=float, default=2.0,
                        help='specify the minimum area threshold')
    parser.add_argument('-l', '--lol')

    return parser.parse_args()

if __name__ == "__main__":

    config = defaultdict(list)
    args = parseArguments()
    debug = args.debug
    
#    lol_visualize.summonerAvgTimePlayedInMinutesHistogram(lol_analyzer.getSummonerAvgTimePlayedInMinutes(), lol_analyzer.getAvgTimePlayed(), lol_analyzer.getMaxTimePlayed())
#    lol_visualize.summonerAvgMinionsKilledHistogram(lol_analyzer.getSummonerAvgMinionsKilled(), lol_analyzer.getAvgMinionsKilled(), lol_analyzer.getMaxMinionsKilled())
#    lol_visualize.summonerAvgGoldEarningsHistogram(lol_analyzer.getSummonerAvgGoldEarnings(), lol_analyzer.getAvgGoldEarned(), lol_analyzer.getMaxGoldEarned())
#    lol_visualize.summonerAvgGoldSpendingsHistogram(lol_analyzer.getSummonerAvgGoldSpendings(), lol_analyzer.getAvgGoldSpent(), lol_analyzer.getMaxGoldSpent())
#    lol_visualize.summonerAvgNumDeathsHistogram(lol_analyzer.getSummonerAvgNumDeaths(), lol_analyzer.getAvgDeaths(), lol_analyzer.getMaxDeaths())
#    lol_visualize.summonerAvgTotalDamageDealtHistogram(lol_analyzer.getSummonerAvgTotalDamageDealt(), lol_analyzer.getAvgTotalDamageDealt(), lol_analyzer.getMaxTotalDamageDealt())
#    lol_visualize.summonerAvgTotalDamageTakenHistogram(lol_analyzer.getSummonerAvgTotalDamageTaken(), lol_analyzer.getAvgTotalDamageTaken(), lol_analyzer.getMaxTotalDamageTaken())
#    lol_visualize.damageTakenDealtBarGraph(lol_analyzer.getSummonerAvgTotalDamageDealt(), lol_analyzer.getSummonerAvgTotalDamageTaken())
#    lol_visualize.goldSpentEarnedBarGraph(lol_analyzer.getSummonerAvgGoldEarnings(), lol_analyzer.getSummonerAvgGoldSpendings())
