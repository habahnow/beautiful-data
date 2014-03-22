#!/usr/bin/python

import argparse
from collections import defaultdict
from bd_visualize import lol_visualize
from bd_analyze import lol_analyzer
from bd_collect import lol_collector
import numpy as np


debug = False

def parseArguments():
    parser = argparse.ArgumentParser(usage='%(prog)s [options]', description='bd application')

    parser.add_argument('--debug', action='store_true', default=False)
    parser.add_argument('-m', '--min-area', dest='minArea', type=float, default=2.0, help='specify the minimum area threshold')
    parser.add_argument('-l', '--lol')
    parser.add_argument('-r', '--read', default='')
    parser.add_argument('-n', '--min', default=0)
    parser.add_argument('-o', '--max', default=10)
    return parser.parse_args()

if __name__ == "__main__":

    config = defaultdict(list)
    args = parseArguments()
    debug = args.debug
    
    if args.lol == 'TimePlayedHistogram':
        lol_visualize.summonerAvgTimePlayedInMinutesHistogram(lol_analyzer.getSummonerAvgTimePlayedInMinutes(), lol_analyzer.getAvgTimePlayed(), lol_analyzer.getMaxTimePlayed())
    elif args.lol == 'AvgMinionKilledHistogram':
        lol_visualize.summonerAvgMinionsKilledHistogram(lol_analyzer.getSummonerAvgMinionsKilled(), lol_analyzer.getAvgMinionsKilled(), lol_analyzer.getMaxMinionsKilled())
    elif args.lol == 'AvgGoldEarnedHistogram':
        lol_visualize.summonerAvgGoldEarningsHistogram(lol_analyzer.getSummonerAvgGoldEarnings(), lol_analyzer.getAvgGoldEarned(), lol_analyzer.getMaxGoldEarned())
    elif args.lol == 'AvgGoldSpendingHistogram':
        lol_visualize.summonerAvgGoldSpendingsHistogram(lol_analyzer.getSummonerAvgGoldSpendings(), lol_analyzer.getAvgGoldSpent(), lol_analyzer.getMaxGoldSpent())
    elif args.lol == 'AvgNumDeathHistogram':
        lol_visualize.summonerAvgNumDeathsHistogram(lol_analyzer.getSummonerAvgNumDeaths(), lol_analyzer.getAvgDeaths(), lol_analyzer.getMaxDeaths())
    elif args.lol == 'AvgTotalDamageDealtHistogram':
        lol_visualize.summonerAvgTotalDamageDealtHistogram(lol_analyzer.getSummonerAvgTotalDamageDealt(), lol_analyzer.getAvgTotalDamageDealt(), lol_analyzer.getMaxTotalDamageDealt())
    elif args.lol == 'AvgTotalDamageTakenHistogram':
        lol_visualize.summonerAvgTotalDamageTakenHistogram(lol_analyzer.getSummonerAvgTotalDamageTaken(), lol_analyzer.getAvgTotalDamageTaken(), lol_analyzer.getMaxTotalDamageTaken())
    elif args.lol == 'DamageTakenDealtBar':
        lol_visualize.damageTakenDealtBarGraph(lol_analyzer.getSummonerAvgTotalDamageDealt(), lol_analyzer.getSummonerAvgTotalDamageTaken())
    elif args.lol == 'GoldSpentEarnedBar':
        lol_visualize.goldSpentEarnedBarGraph(lol_analyzer.getSummonerAvgGoldEarnings(), lol_analyzer.getSummonerAvgGoldSpendings())
    elif args.lol == 'DamageScatterPlot':
        lol_visualize.plotScatterMaxDamagevAvgTotalDamage(lol_analyzer.getSummonerMaxDamageDealt(), lol_analyzer.getSummonerAvgTotalDamageDealt(), lol_analyzer.getArcTan(lol_analyzer.getSummonerMaxDamageDealt(), lol_analyzer.getSummonerAvgTotalDamageDealt()))
    elif args.lol == 'GradFunctionGraph':
        lol_visualize.begin_gradient(lol_analyzer.getRecentTimesPlayed(15, 200), lol_analyzer.getRecentGoldEarned(15, 200) , 1000)
    else:
        print 'No such graph exist !'

    # for writing new files
    # use -n for min, -o for max, -r non '' value
    if args.read == '':
        print 'Not reading data'
    else:
        if int(args.min) < int(args.max):
            lol_collector.collectGameDataRange(int(args.min), int(args.max))
            print 'Collected data from %s to %s' % (args.min, args.max)
        else:
            print 'Boo!'



