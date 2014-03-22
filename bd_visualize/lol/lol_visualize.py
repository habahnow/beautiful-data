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

def scatter_plot(string_x , string_y):
    x = []
    y = []
    if string_x == "minions killed":
         x = lol_analyzer.getRecentMinionsKilled(15, 26)
         y = lol_analyzer.getRecentGoldEarned(15, 26)
         print len(x)
         print range(15,26)
         plt.scatter(x, y)
         plt.show()

def calculate_cost(X, Y, Theta):
    cost = 0.0 #You must return the correct value for cost
    #add y-intercept term with a column of ones
    dimX = X.shape #get dimensions of X as a tuple (rows, columns) 
    N = dimX[0] #get number of rows
    # X = np.c_[np.ones(N), X]#add column of ones at beginning to accommodate theta0
    #X is now a ~392x2 while Theta is 2x1
    #error is cause here
    predictions = (np.dot(X,Theta) - Y.reshape(dimX[0], 1))**2
    cost = predictions.sum() * (1/(2.0 * N))
    return cost

def gradient_descent(x,  Y, Theta, alpha, num_iters):
    N = len(x) #get number of rows
    T = len(Theta)
    Y = np.array(Y)
    # X = np.c_[np.ones(N), X]

    for i in range(num_iters):
        # x1 = np.array(X)
        Theta1 = np.array(Theta)
        # if i <  9:
            # print " theta: ", Theta1
        predictions = x.dot(Theta1)
        errors_x1 = (predictions - Y.reshape(N,1)) * np.reshape(x[:, 0], (N, 1))
        # print np.reshape(x[:,1], (N, 1))
        errors_x2 = (predictions - Y.reshape(N,1)) * np.reshape(x[:, 1], (N, 1))
        Theta1[0] = Theta1[0] - alpha * (1.0 / N) * errors_x1.sum()
        Theta1[1] = Theta1[1] - alpha * (1.0 / N) * errors_x2.sum()
    return Theta1 
  
def begin_gradient(x, y, num_iters):
    x_norm = (x - np.mean(x))/np.std(x)
    theta = np.zeros((2,1))
    x_norm = np.c_[np.ones(len(x)), x]
    y = np.array(y)
    # print "cost before: " , calculate_cost(x_norm,y,theta)
    theta = gradient_descent(x_norm, y, theta, .01, num_iters)
    # print "cost after: " , calculate_cost(x_norm,y, theta)
    # print x
    m = theta[1]
    b = theta[0]
    b -= np.mean(x)/np.std(x) * m
    m = m/np.std(x)
    yl = np.polyval([m,b], x)
    # print yl
    yl = yl * .02
    yl += -min(yl)
    # yl = yl + 7000
    # print yl
    # x1 = np.array(x)
    # x1 = np.c_[np.ones(len(x1)), x1]
    # print x1.dot(theta)
    plt.plot(x, yl)
    plt.scatter(x, y)
    plt.show()
x = lol_analyzer.getRecentTimesPlayed(15,800)
y = lol_analyzer.getRecentGoldEarned(15, 800)
# plt.scatter(x,y)
# plt.show()
begin_gradient(x, y, 1000)
#summonerAvgTimePlayedInMinutesHistogram()
#summonerAvgMinionsKilledHistogram()
#summonerAvgGoldEarningsHistogram()
#summonerAvgGoldSpendingsHistogram()
#summonerAvgNumDeathsHistogram()
#summonerAvgTotalDamageDealtHistogram()
#summonerAvgTotalDamageTakenHistogram()

