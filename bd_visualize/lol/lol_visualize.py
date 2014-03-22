
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
from mpl_toolkits.mplot3d import Axes3D

def summonerAvgTimePlayedInMinutesHistogram():
    hist, bins = np.histogram(lol_analyzer.getSummonerAvgTimePlayedInMinutes(), bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Minutes Played per Game ' )
    plt.gca().set_position((.1, .3, .8, .6))
    plt.figtext(.1, .1, "Average Time Played per Game: " + str(round(lol_analyzer.getAvgTimePlayed() / 60)) + "minutes\nMax Time Played per Game: " +  str(lol_analyzer.getMaxTimePlayed()/ 60) + 'minutes')
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
    plt.figtext(.1, .1, "Average Minions Killed per Game: " + str(round(lol_analyzer.getAvgMinionsKilled())) + "\nMax Minions Killed: " +  str(lol_analyzer.getMaxMinionsKilled()))
    plt.ylabel('Number of Games')
    plt.xlabel('Minions Killed')
    plt.show()
    
def summonerAvgGoldEarningsHistogram():
    hist, bins = np.histogram(lol_analyzer.getSummonerAvgGoldEarnings(), bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Gold Earnings per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    plt.figtext(.1, .1, "Average Gold Earnings per Game: " + str(round(lol_analyzer.getAvgGoldEarned())) + "\nMax Gold Earning: " +  str(lol_analyzer.getMaxGoldEarned()))
    plt.ylabel('Number of Games')
    plt.xlabel('Gold Earned')
    plt.show()
    
def summonerAvgGoldSpendingsHistogram():
    hist, bins = np.histogram(lol_analyzer.getSummonerAvgGoldSpendings(), bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Gold Spendings per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    plt.figtext(.1, .1, "Average Gold Spendings per Game: " + str(round(lol_analyzer.getAvgGoldSpent())) + "\nMax Gold Spending: " +  str(lol_analyzer.getMaxGoldSpent()))
    plt.ylabel('Number of Games')
    plt.xlabel('Gold Spent')
    plt.show()
    
def summonerAvgNumDeathsHistogram():
    hist, bins = np.histogram(lol_analyzer.getSummonerAvgNumDeaths(), bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Number of Deaths per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    plt.figtext(.1, .1, "Average Number of Deaths per Game: " + str(round(lol_analyzer.getAvgDeaths())) + "\nMax Deaths: " +  str(lol_analyzer.getMaxDeaths()))
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
    plt.title('Average Total Damage Dealt per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    plt.figtext(.1, .1, "Average Total Damage Dealt per Game: " + str(round(lol_analyzer.getAvgTotalDamageDealt())) + "\nMax Total Damage Dealt: " +  str(lol_analyzer.getMaxTotalDamageDealt()))
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
    
def damageTakenDealtBarGraph():
    avgTotalDamageDealtThousanths = []
    for total in lol_analyzer.getSummonerAvgTotalDamageDealt():
        avgTotalDamageDealtThousanths.append(total / 1000)
    avgTotalDamageTakenThousanths = []
    
    for total in lol_analyzer.getSummonerAvgTotalDamageTaken():
        avgTotalDamageTakenThousanths.append(total / 1000)
    
    means_damage_dealt = avgTotalDamageDealtThousanths
    means_damage_taken = avgTotalDamageTakenThousanths
    
    if (np.size(means_damage_dealt) > np.size(means_damage_taken)):
        means_damage_dealt = means_damage_dealt[0:np.size(means_damage_taken)]
    if (np.size(means_damage_dealt) > np.size(means_damage_taken)):
        means_damage_dealt = means_damage_dealt[0:np.size(means_damage_taken)]
        
    
    
    n_groups = np.size(means_damage_dealt)
    
    fig, ax = plt.subplots()
    
    index = np.arange(n_groups)
    bar_width = 0.35
    
    error_config = {'ecolor': '0.3'}
    
    rects1 = plt.bar(index, means_damage_dealt, bar_width,
                     color='b',
                     error_kw=error_config,
                     label='Dealt')
    
    rects2 = plt.bar(index + bar_width, means_damage_taken, bar_width,
                     color='r',
                     error_kw=error_config,
                     label='Taken')
    
    plt.xlabel('Summoner ID')
    plt.ylabel('Damage in Thousands')
    plt.title('Damage Dealt and Taken')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
def goldSpentEarnedBarGraph():
    
    means_gold_earned = lol_analyzer.getSummonerAvgGoldEarnings()
    means_gold_spent = lol_analyzer.getSummonerAvgGoldSpendings()
    
    if (np.size(means_gold_earned) > np.size(means_gold_spent)):
        means_gold_earned = means_gold_earned[0:np.size(means_gold_spent)]
    if (np.size(means_gold_spent) > np.size(means_gold_earned)):
        means_gold_spent = means_gold_spent[0:np.size(means_gold_earned)]
    n_groups = np.size(means_gold_earned)
    fig, ax = plt.subplots()
    
    index = np.arange(n_groups)
    bar_width = 0.35
    
    error_config = {'ecolor': '0.3'}
    
    rects1 = plt.bar(index, means_gold_earned, bar_width,
                     color='b',
                     error_kw=error_config,
                     label='Earned')
    
    rects2 = plt.bar(index + bar_width, means_gold_spent, bar_width,
                     color='r',
                     error_kw=error_config,
                     label='Spent')
    
    plt.xlabel('Summoner ID')
    plt.ylabel('Damage in Thousands')
    plt.title('Gold Earned and Spent')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

#goldSpentEarnedBarGraph()
#damageTakenDealtBarGraph()
#summonerAvgTimePlayedInMinutesHistogram()
#summonerAvgMinionsKilledHistogram()
#summonerAvgGoldEarningsHistogram()
#summonerAvgGoldSpendingsHistogram()
#summonerAvgNumDeathsHistogram()
#summonerAvgTotalDamageDealtHistogram()
#summonerAvgTotalDamageTakenHistogram()

