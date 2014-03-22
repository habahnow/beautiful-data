# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 16:35:46 2014

@author: Eddie
"""
#import lol_analyzer

#import lol_analyzer

#import os
#import sys
#sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))
#from sortings import config

#from bd_analyze import lol_analyzer
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def summonerAvgTimePlayedInMinutesHistogram(summonerAvgTimePlayed, avgTimePlayed, maxTimePlayed):
    hist, bins = np.histogram(summonerAvgTimePlayed, bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Minutes Played per Game ' )
    plt.gca().set_position((.1, .3, .8, .6))
    plt.figtext(.1, .1, "Average Time Played per Game: " + str(round(avgTimePlayed / 60)) + "minutes\nMax Time Played per Game: " +  str(maxTimePlayed/ 60) + 'minutes')
    plt.ylabel('Number of Games')
    plt.xlabel('Game Time (Minutes)')
    plt.show()

def summonerAvgMinionsKilledHistogram(summonerAvgMinionsKilled, avgMinionsKilled, maxMinionsKilled):
    #hist, bins = np.histogram(lol_analyzer.getSummonerAvgMinionsKilled(), bins=50)\hist, bins = np.histogram(lol_analyzer.getSummonerAvgMinionsKilled(), bins=50)
    hist, bins = np.histogram(summonerAvgMinionsKilled, bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Minions Killed Per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    #plt.figtext(.1, .1, "Average Minions Killed per Game: " + str(round(lol_analyzer.getAvgMinionsKilled())) + "\nMax Minions Killed: " +  str(lol_analyzer.getMaxMinionsKilled()))
    plt.figtext(.1, .1, "Average Minions Killed per Game: " + str(round(avgMinionsKilled)) + "\nMax Minions Killed: " +  str(maxMinionsKilled))
    plt.ylabel('Number of Games')
    plt.xlabel('Minions Killed')
    plt.show()
    
def summonerAvgGoldEarningsHistogram(summonerAvgGoldEarnings, avgGoldEarned, maxGoldEarned):
    #hist, bins = np.histogram(lol_analyzer.getSummonerAvgGoldEarnings(), bins=50)
    hist, bins = np.histogram(summonerAvgGoldEarnings, bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Gold Earnings per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    #plt.figtext(.1, .1, "Average Gold Earnings per Game: " + str(round(lol_analyzer.getAvgGoldEarned())) + "\nMax Gold Earning: " +  str(lol_analyzer.getMaxGoldEarned()))
    plt.figtext(.1, .1, "Average Gold Earnings per Game: " + str(round(avgGoldEarned)) + "\nMax Gold Earning: " +  str(maxGoldEarned))
    plt.ylabel('Number of Games')
    plt.xlabel('Gold Earned')
    plt.show()

def summonerAvgGoldSpendingsHistogram(summonerAvgGoldSpendings, avgGoldSpent, maxGoldSpent):
    print avgGoldSpent
    print maxGoldSpent
    # hist, bins = np.histogram(lol_analyzer.getSummonerAvgGoldSpendings(), bins=50)
    hist, bins = np.histogram(summonerAvgGoldSpendings, bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Gold Spendings per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    #plt.figtext(.1, .1, "Average Gold Spendings per Game: " + str(round(lol_analyzer.getAvgGoldSpent())) + "\nMax Gold Spending: " +  str(lol_analyzer.getMaxGoldSpent()))
    plt.figtext(.1, .1, "Average Gold Spendings per Game: " + str(round(avgGoldSpent)) + "\nMax Gold Spending: " +  str(maxGoldSpent))
    plt.ylabel('Number of Games')
    plt.xlabel('Gold Spent')
    plt.show()
    
def summonerAvgNumDeathsHistogram(summonerAvgNumDeaths, avgDeaths, maxDeaths):
    #hist, bins = np.histogram(lol_analyzer.getSummonerAvgNumDeaths(), bins=50)
    hist, bins = np.histogram(summonerAvgNumDeaths, bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Number of Deaths per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    #plt.figtext(.1, .1, "Average Number of Deaths per Game: " + str(round(lol_analyzer.getAvgDeaths())) + "\nMax Deaths: " +  str(lol_analyzer.getMaxDeaths()))
    plt.figtext(.1, .1, "Average Number of Deaths per Game: " + str(round(avgDeaths)) + "\nMax Deaths: " +  str(maxDeaths))
    plt.ylabel('Number of Games')
    plt.xlabel('Number of Deaths')
    plt.show()
    
def summonerAvgTotalDamageDealtHistogram(summonerAvgTotalDamageDealt, avgTotalDamageDealt, maxTotalDamageDealt):
    avgTotalDamageDealtThousanths = []
    #for total in lol_analyzer.getSummonerAvgTotalDamageDealt():
    for total in summonerAvgTotalDamageDealt:
        avgTotalDamageDealtThousanths.append(total / 1000)
    hist, bins = np.histogram(avgTotalDamageDealtThousanths, bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Total Damage Dealt per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    #plt.figtext(.1, .1, "Average Total Damage Dealt per Game: " + str(round(lol_analyzer.getAvgTotalDamageDealt())) + "\nMax Total Damage Dealt: " +  str(lol_analyzer.getMaxTotalDamageDealt()))
    plt.figtext(.1, .1, "Average Total Damage Dealt per Game: " + str(round(avgTotalDamageDealt)) + "\nMax Total Damage Dealt: " +  str(maxTotalDamageDealt))
    plt.ylabel('Number of Games')
    plt.xlabel('Total Damage Dealt in Thousands')
    plt.show()

def summonerAvgTotalDamageTakenHistogram(summonerAvgTotalDamageTaken, avgTotalDamageTaken, maxTotalDamageTaken):
    avgTotalDamageDealtThousanths = []
    #for total in lol_analyzer.getSummonerAvgTotalDamageTaken():
    for total in summonerAvgTotalDamageTaken:
        avgTotalDamageDealtThousanths.append(total / 1000)
    hist, bins = np.histogram(avgTotalDamageDealtThousanths, bins=50)
    width = 0.7 * (bins[1] - bins[0])
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', width=width)
    plt.title('Average Total Damage Taken Per Game')
    plt.gca().set_position((.1, .3, .8, .6))
    plt.figtext(.1, .1, "Average Total Damage Taken Per Game: " + str(round(avgTotalDamageTaken)) + "\nMax Total Damage Taken: " +  str(maxTotalDamageTaken))
    plt.ylabel('Number of Games')
    plt.xlabel('Total Damage Taken in Thousands')
    plt.show()

def scatter_plot(string_x , string_y):
    x = []
    y = []
    if string_x == "minions killed":
         x = lol_analyzer.getRecentMinionsKilled(15, 26)
         y = lol_analyzer.getRecentGoldEarned(15, 26)
         plt.scatter(x, y)
         plt.show()

def calculate_cost(X, Y, Theta):
    cost = 0.0 
    dimX = X.shape  
    N = dimX[0] #get number of rows
    predictions = (np.dot(X,Theta) - Y.reshape(dimX[0], 1))**2
    cost = predictions.sum() * (1/(2.0 * N))
    return cost

def gradient_descent(x,  Y, Theta, alpha, num_iters):
    N = len(x) #get number of rows
    T = len(Theta)
    Y = np.array(Y)

    for i in range(num_iters):
        Theta1 = np.array(Theta)
        predictions = x.dot(Theta1)
        errors_x1 = (predictions - Y.reshape(N,1)) * np.reshape(x[:, 0], (N, 1))
        errors_x2 = (predictions - Y.reshape(N,1)) * np.reshape(x[:, 1], (N, 1))
        Theta1[0] = Theta1[0] - alpha * (1.0 / N) * errors_x1.sum()
        Theta1[1] = Theta1[1] - alpha * (1.0 / N) * errors_x2.sum()
    return Theta1 
  
def begin_gradient(x, y, num_iters):
    scale_down = .02
    x_norm = (x - np.mean(x))/np.std(x)
    theta = np.zeros((2,1))
    x_norm = np.c_[np.ones(len(x)), x]
    y = np.array(y)
    theta = gradient_descent(x_norm, y, theta, .01, num_iters)
    m = theta[1]
    b = theta[0]
    #reducing because of feature scaling
    b -= np.mean(x)/np.std(x) * m
    m = m/np.std(x)
    yl = (np.polyval([m,b], x)) * scale_down
    yl += -min(yl)
    plt.plot(x, yl)
    plt.scatter(x, y)
    plt.show()
# x = lol_analyzer.getRecentTimesPlayed(15,800)
# y = lol_analyzer.getRecentGoldEarned(15, 800)
# # plt.scatter(x,y)
# # plt.show()
# begin_gradient(x, y, 1000)
# =======
 
def damageTakenDealtBarGraph(summonerAvgTotalDamageDealt, summonerAvgTotalDamageTaken):
    avgTotalDamageDealtThousanths = []
    #for total in lol_analyzer.getSummonerAvgTotalDamageDealt():
    for total in summonerAvgTotalDamageDealt:
        avgTotalDamageDealtThousanths.append(total / 1000)
    avgTotalDamageTakenThousanths = []
    
    #for total in lol_analyzer.getSummonerAvgTotalDamageTaken():
    for total in summonerAvgTotalDamageTaken:
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
 
def goldSpentEarnedBarGraph(summonerAvgGoldEarnings, summonerAvgGoldSpendings):
    
    #means_gold_earned = lol_analyzer.getSummonerAvgGoldEarnings()
    means_gold_earned = summonerAvgGoldEarnings
    #means_gold_spent = lol_analyzer.getSummonerAvgGoldSpendings()
    means_gold_spent = summonerAvgGoldSpendings
    
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
#####

def plotScatterMaxDamagevAvgTotalDamage(derp, dert, tan):
    x = derp
    y = dert

    T = tan

    plt.scatter(x, y,c = T, alpha=0.5)
    plt.xlabel('Max Damage Dealt')
    plt.ylabel('Avg Total Damage Dealt')

    plt.show()

#goldSpentEarnedBarGraph()
#damageTakenDealtBarGraph()
#summonerAvgTimePlayedInMinutesHistogram()
#summonerAvgMinionsKilledHistogram()
#summonerAvgGoldEarningsHistogram()
#summonerAvgGoldSpendingsHistogram()
x = lol_analyzer.getRecentTimesPlayed(15,800)
y = lol_analyzer.getRecentGoldEarned(15, 800)
# plt.scatter(x,y)
# plt.show()
begin_gradient(x, y, 1000)
#summonerAvgNumDeathsHistogram()
#summonerAvgTotalDamageDealtHistogram()
#summonerAvgTotalDamageTakenHistogram()

