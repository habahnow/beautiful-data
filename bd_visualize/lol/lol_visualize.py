# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 16:35:46 2014

@author: Eddie
"""
import sys
sys.path.append('../../bd_analyze/lol/')
import lol_analyzer
import matplotlib.pyplot as plt
import numpy as np

def summonerAvgTimePlayedInMinutesHistogram():
    hist, bins = np.histogram(lol_analyzer.getSummonerAvgTimePlayedInMinutes(), bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Minutes Played Per Game ' )
    plt.gca().set_position((.1, .3, .8, .6))
    plt.figtext(.1, .1, "Average Time Played Per Game: " + str(round(lol_analyzer.getAvgTimePlayed() / 60)) + "minutes\nMax Time Played Per Game: " +  str(lol_analyzer.getMaxTimePlayed()/ 60) + 'minutes')
    plt.ylabel('Number of Games')
    plt.xlabel('Game Time (Minutes)')
    plt.show()

def summonerAvgMinionsKilledHistogram():
    hist, bins = np.histogram(lol_analyzer.getSummonerAvgMinionsKilled(), bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Minions Killed Per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    plt.figtext(.1, .1, "Average Minions Killed Per Game: " + str(round(lol_analyzer.getAvgMinionsKilled())) + "\nMax Minions Killed: " +  str(lol_analyzer.getMaxMinionsKilled()))
    plt.ylabel('Number of Games')
    plt.xlabel('Minions Killed')
    plt.show()
    
def summonerAvgGoldEarningsHistogram():
    hist, bins = np.histogram(lol_analyzer.getSummonerAvgGoldEarnings(), bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Gold Earnings Per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    plt.figtext(.1, .1, "Average Gold Earnings Per Game: " + str(round(lol_analyzer.getAvgGoldEarned())) + "\nMax Gold Earning: " +  str(lol_analyzer.getMaxGoldEarned()))
    plt.ylabel('Number of Games')
    plt.xlabel('Gold Earned')
    plt.show()
    
def summonerAvgGoldSpendingsHistogram():
    hist, bins = np.histogram(lol_analyzer.getSummonerAvgGoldSpendings(), bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Gold Spendings Per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    plt.figtext(.1, .1, "Average Gold Spendings Per Game: " + str(round(lol_analyzer.getAvgGoldSpent())) + "\nMax Gold Spending: " +  str(lol_analyzer.getMaxGoldSpent()))
    plt.ylabel('Number of Games')
    plt.xlabel('Gold Spent')
    plt.show()
    
def summonerAvgNumDeathsHistogram():
    hist, bins = np.histogram(lol_analyzer.getSummonerAvgNumDeaths(), bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Number of Deaths Per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    plt.figtext(.1, .1, "Average Number of Deaths Per Game: " + str(round(lol_analyzer.getAvgDeaths())) + "\nMax Deaths: " +  str(lol_analyzer.getMaxDeaths()))
    plt.ylabel('Number of Games')
    plt.xlabel('Number of Deaths')
    plt.show()
    
def summonerAvgTotalDamageDealtHistogram():
    avgTotalDamageDealtThousanths = []
    for total in lol_analyzer.getSummonerAvgTotalDamageDealt():
        avgTotalDamageDealtThousanths.append(total / 1000)
    hist, bins = np.histogram(avgTotalDamageDealtThousanths, bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Total Damage Dealt Per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    plt.figtext(.1, .1, "Average Total Damage Dealt Per Game: " + str(round(lol_analyzer.getAvgTotalDamageDealt())) + "\nMax Total Damage Dealt: " +  str(lol_analyzer.getMaxTotalDamageDealt()))
    plt.ylabel('Number of Games')
    plt.xlabel('Total Damage Dealt in Thousands')
    plt.show()
    
def summonerAvgTotalDamageTakenHistogram():
    avgTotalDamageDealtThousanths = []
    for total in lol_analyzer.getSummonerAvgTotalDamageTaken():
        avgTotalDamageDealtThousanths.append(total / 1000)
    hist, bins = np.histogram(avgTotalDamageDealtThousanths, bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Total Damage Taken Per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    plt.figtext(.1, .1, "Average Total Damage Taken Per Game: " + str(round(lol_analyzer.getAvgTotalDamageTaken())) + "\nMax Total Damage Taken: " +  str(lol_analyzer.getMaxTotalDamageTaken()))
    plt.ylabel('Number of Games')
    plt.xlabel('Total Damage Taken in Thousands')
    plt.show()
    

#summonerAvgTimePlayedInMinutesHistogram()
#summonerAvgMinionsKilledHistogram()
#summonerAvgGoldEarningsHistogram()
#summonerAvgGoldSpendingsHistogram()
#summonerAvgNumDeathsHistogram()
#summonerAvgTotalDamageDealtHistogram()
#summonerAvgTotalDamageTakenHistogram()

