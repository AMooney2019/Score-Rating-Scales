#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 16:16:34 2023

@author: Aaron Mooney
"""

# References:
# Sauro, J., &; Lewis, J. R. (2016). 
# In Quantifying the user experience: Practical statistics for user research 
# (pp. 19–60). essay, Morgan Kaufmann. 

import pandas as pd
import statistics as stats
from scipy.stats import sem
import scipy.stats


def getDescriptStats(scores):
    """Reads in a list of sample scores. Calculates descriptive statistics
    from those scores.
    Returns a list object containing descriptive statistics values."""
    
    # Calculate (n) based on length of data list.
    print('')
    numScores = len(scores)
    #print('The number of scores(n) is:', numScores)
    print('n:', numScores)
    
    # Sum of scores in data list.
    sumScores = sum(scores)
    #print('The sum of the scores is:', sumScores)
    print('Sum:', sumScores)
    print('')
    
    # Range of values.
    minVal = min(scores)
    maxVal = max(scores)
    rangeVals = maxVal - minVal
    print('Range:', rangeVals)
    print('Min Value:', minVal)
    print('Max Value:', maxVal)
    print('')
    
    # Mean of scores in data list.
    meanScores = round(stats.mean(scores), 2)
    #print('The mean of the scores is:', meanScores)
    print('Mean:', meanScores)
    
    # Standard deviation of scores in data list.
    stdDev = round(stats.stdev(scores), 2)
    #print('The standard deviation is:', stdDev)
    print('Standard deviation:', stdDev)
    
    # Standard error of scores in data list.
    stdErr = round(sem(scores), 2)
    #print('The standard error is:', stdErr)
    print('Standard Error:', stdErr)
    
    return numScores, sumScores, meanScores, stdDev, stdErr

def getDegFree(scores):
    """Reads in a list of scores. Counts the number of items in the list
    and subtracts 1 to calculate the degrees of freedom.
    Returns a degrees of freedom value."""
    
    numScores = len(scores)
    doF = numScores - 1
    print('Degrees of Freedom:', doF)
    
    return doF

def getConfIntvals(scores, alpha):
    """Calculates the confidence intervals for a list of data. 
    Takes in a list of data and the alpha level, calculates tabled-T values
    and confidence level values."""
    
    alphaTwoTail = (1 - (alpha / 2))    
    descriptStats = []
    
    descriptStats = getDescriptStats(scores)
    doF = descriptStats[0] - 1
    
    tCrit = round(scipy.stats.t.ppf(alphaTwoTail, doF), 2)
    stdErr = descriptStats[4]
    critVal = (stdErr * tCrit)
    
    meanVal = descriptStats[2]
    LCL = round((meanVal - critVal), 2)
    UCL = round((meanVal + critVal), 2)
    
    print('Confidence Interval:', LCL, '<', meanVal, '<', UCL, '\n')
    print('The population value of the mean at alpha', alpha, 'level is between', LCL, 'and', UCL)
    
    return LCL, UCL

### *******************************************************
### Use this block if you have data as a list of values. 
### *******************************************************
# If you have a list of values, enter them in these brackets. 

#scores = [6, 6, 5, 3, 4, 4, 3, 5, 5, 3]

### *******************************************************


### *******************************************************
### Use this block if you have data in a .csv file.
### *******************************************************
# If you have a data table to score, use this block.
# Place your .csv file in the same directory as this file. 

# File Name Example: 'FakeUXData.csv'
inFile = 'Fake_Ratings_Data.csv'
df = pd.read_csv(inFile, index_col=False)

# Include the column name you wish to calculate the scores on.
# Example: 'Rating_1'

alpha = 0.05
scores = df['Rating_1'] 

scoreRatingData = getConfIntvals(scores, alpha)
### *******************************************************


