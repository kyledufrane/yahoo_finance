# --------------------------------------------------------------
# API & Data Cleaning library
# --------------------------------------------------------------

# Import libaries needed for functions

import requests
import hmac
import hashlib
import time
import cbpro
import pickle
import json

import pandas as pd
import matplotlib.pyplot as plt

from lazypredict.Supervised import LazyRegressor

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from requests.auth import AuthBase

# --------------------------------------------------------------

def convert_ids(df, market, suffix):

    '''This function takes in:
        1. CoinBasePro Dataframe (cbpro.PublicClient().get_products())
        2. Market - EUR, USD, USDT, GBP, ECT.
        3. Suffix - Kraken's data comes with different time increments from 1 minute to 
                    1440 minutes. To select the correct csv for future loops add a string
                    '_1440.csv' for 1440 minute csv's.
        
        The output of this function will return a list of clean names that will allow you 
        to open the csv's stored in Kraken_OHLCVT'''
    
    coin = df[df['id'].str.contains(market)]
    
    coin.sort_values('id', inplace=True)
    
    coin = coin['id']
    
    coin = [clean_name.replace("-", "") for clean_name in coin]    
    
    coin = [clean_name + suffix for clean_name in coin]
    
    return coin

# --------------------------------------------------------------


