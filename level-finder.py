import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema

def identify_levels(data, window=10, distance=0.01):
    """
    Identify significant support and resistance levels in the stock price data.

    Parameters:
    data (pd.Series): The stock price data.
    window (int): The window size for rolling minimum and maximum.
    distance (float): Minimum percentage distance between levels.

    Returns:
    levels (dict): Dictionary with 'support' and 'resistance' levels.
    """
    levels = {'support': [], 'resistance': []}

    # Identify local minima and maxima
    local_min = argrelextrema(data.values, np.less_equal, order=window)[0]
    local_max = argrelextrema(data.values, np.greater_equal, order=window)[0]

    # Filter out close levels
    for i in local_min:
        if not levels['support'] or min([abs(i - x) for x in levels['support']]) > window:
            levels['support'].append(i)
    for i in local_max:
        if not levels['resistance'] or min([abs(i - x) for x in levels['resistance']]) > window:
            levels['resistance'].append(i)

    # Convert index to values
    levels['support'] = data.iloc[levels['support']].values
    levels['resistance'] = data.iloc[levels['resistance']].values

    # Filter levels based on minimum distance
    levels['support'] = filter_levels(levels['support'], distance)
    levels['resistance'] = filter_levels(levels['resistance'], distance)

    return levels

def filter_levels(levels, distance):
    """
    Filter levels to keep only the most significant ones based on distance.

    Parameters:
    levels (list): List of levels.
    distance (float): Minimum percentage distance between levels.

    Returns:
    filtered_levels (list): List of filtered levels.
    """
    filtered_levels = []
    for level in levels:
        if not filtered_levels or min([abs(level - x) for x in filtered_levels]) > distance * level:
            filtered_levels.append(level)
    return filtered_levels

def plot_levels(data, levels):
    """
    Plot the stock price data with support and resistance levels.

    Parameters:
    data (pd.DataFrame): The stock price data.
    levels (dict): Dictionary with 'support' and 'resistance' levels.
    """
    plt.figure(figsize=(14, 7))
    plt.plot(data.index, data['Close'], label='Close Price', color='blue')
    for level in levels['support']:
        plt.axhline(y=level, color='green', linestyle='--', linewidth=1, label='Support Level' if level == levels['support'][0] else "")
    for level in levels['resistance']:
        plt.axhline(y=level, color='red', linestyle='--', linewidth=1, label='Resistance Level' if level == levels['resistance'][0] else "")
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Support and Resistance Levels')
    plt.legend()
    plt.show()

# Input the ticker symbol and period
ticker = 'AAPL'  # Example ticker symbol
# '1d': 1 day, '1mo': 1 month, '1y': 1 year,
# 'ytd': Year to date,'max': Maximum available data
# must be one of ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', 'ytd', 'max']
period = '1y'


# Download the stock price data
data = yf.download(ticker, period=period)

# Identify significant support and resistance levels
levels = identify_levels(data['Close'])

# Plot the levels
plot_levels(data, levels)
