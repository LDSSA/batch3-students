import pandas as pd
import matplotlib.pyplot as plt
import warnings
from statsmodels.tsa.stattools import acf
from statsmodels.graphics.tsaplots import plot_acf
idx = pd.IndexSlice
warnings.simplefilter(action='ignore', category=FutureWarning)   
from random import seed
from sklearn.metrics import mean_absolute_error
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import math
from statsmodels.tsa.seasonal import seasonal_decompose
from sklearn.ensemble import GradientBoostingRegressor
import itertools
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa import stattools
import hashlib # for grading purposes
from sklearn.model_selection import ParameterGrid
from datetime import timedelta
from pandas.plotting import lag_plot
from statsmodels.tsa.arima_model import ARIMA


def build_target(series_, number_of_periods_ahead):
    """ 
    takes a series, turned it into a dataframe, and adds a new column called target
    This column is the input series, lagged number_of_periods_ahead into the future
    """
    
    # make a copy 
    series_ = series_.copy()
    series_.name = 'value'
    
    # make a dataframe from the series
    df_ = pd.DataFrame(series_)
    
    # the target column will be the input series, lagged into the future
    df_['target'] = series_.shift(-number_of_periods_ahead)
    return df_

    
def separate_last_day(df_):
    
    """
    takes a dataset which has the target and features built 
    and separates it into the last day
    """
    # take the last period 
    last_period = df_.iloc[-1]
    
    # the last period is now a series, so it's name will be the timestamp
    training_data = df_.loc[df_.index < last_period.name]

    return last_period, training_data

def build_some_features(df_, num_periods_ahead, num_periods_lagged=1, num_periods_diffed=0,
                        monthday= False, weekday=False, month=False, rolling=[]): 
    """
    Builds some features by calculating differences between periods  
    """
    # make a copy 
    df_ = df_.copy()
    
    target_date = df_.index
    
    # for a few values, get the lags  
    for i in range(1, num_periods_lagged+1):
        # make a new feature, with the lags in the observed values column
        df_['lagged_%s' % str(i)] = df_['value'].shift(i)
        
    # for a few values, get the diffs  
    for i in range(1, num_periods_diffed+1):
        # make a new feature, with the lags in the observed values column
        df_['diff_%s' % str(i)] = df_['value'].diff(i)
    
    for stat in rolling:
        df_['rolling_%s'%str(stat)] = df_['value'].rolling('1D').aggregate(stat)
    
    if monthday == True:
        df_['day_month'] = df_.index.day
    
    
    return df_


def separate_train_and_test_set(last_period_, training_data_, target='target'): 
    
    """ 
    separates training and test set (clue was in the name, really... )
    Ok, we were lazy and left the target hardcoded as 'target'. Shame on us. 
    """
    
    # anything that isn't a target is a feature 
    features = [feature for feature in training_data_.columns if feature != target]
    
    # adding a sneaky little dropna to avoid the missing data problem above 
    X_train = training_data_.dropna()[features]
    y_train = training_data_.dropna()[target]
    
    X_last_period = last_period_[features]
    
    return X_train, y_train, X_last_period



def prepare_for_prediction(series_, number_of_periods_ahead, num_periods_lagged, 
                           num_periods_diffed, weekday, month, rolling, monthday):
    
    """ 
    Wrapper to go from the original series to X_train, y_train, X_last_period 
    
    """
    
    # build the target 
    data_with_target = build_target(series_, 
                                    number_of_periods_ahead)
    
    # build the features 
    data_with_target_and_features = build_some_features(data_with_target, 
                                                        num_periods_lagged=num_periods_lagged,
                                                       num_periods_diffed=num_periods_diffed,
                                                       num_periods_ahead=number_of_periods_ahead,
                                                       weekday=weekday,
                                                       month=month,
                                                       monthday=monthday,
                                                       rolling=rolling)
    # separate train and test data 
    last_period, training_data = separate_last_day(data_with_target_and_features)

    # separate X_train, y_train, and X_test 
    X_train, y_train, X_last_period = separate_train_and_test_set(last_period, 
                                                           training_data, 
                                                           target='target')
    
    # return ALL OF THE THINGS! (well, actually just the ones we need)
    return X_train, y_train, X_last_period, data_with_target_and_features



def predict_period_n(series_, model, number_of_periods_ahead, num_periods_lagged, 
                     num_periods_diffed, weekday, month, monthday, rolling): 
    
        X_train, y_train, X_last_period, data = prepare_for_prediction(series_, 
                                                             number_of_periods_ahead=number_of_periods_ahead, 
                                                             num_periods_lagged=num_periods_lagged,
                                                             num_periods_diffed=num_periods_diffed,
                                                             weekday=weekday,
                                                             month=month,
                                                             monthday=monthday,
                                                             rolling=rolling)
        
        model.fit(X_train, y_train)
        return model.predict(X_last_period.values.reshape(1, -1)),data
    
    
    
def predict_n_periods(series_, n_periods, model, num_periods_lagged, num_periods_diffed=0, 
                      weekday=False, month=False,rolling=[], monthday=False): 
    predictions = []

    for period_ahead in range(1, n_periods+1):
        pred, data = predict_period_n(series_=series_, 
                                model=model, 
                                number_of_periods_ahead=period_ahead, 
                                num_periods_lagged=num_periods_lagged,
                                num_periods_diffed=num_periods_diffed,
                                weekday=weekday,
                                month=month,
                                monthday=monthday,
                                rolling=rolling
                                )
        
        predictions.append(pred[0])
        
    return predictions



def mean_absolute_percentage_error(y_true, y_pred): 
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100

def generate_submission_file(predictions_area_1, predictions_area_2, predicitons_area_3):
    test_1 = pd.DataFrame(predictions_area_1,index=pd.date_range(start='23/05/2005', end='30/05/2005', freq='h')[:-1])
    test_2 = pd.DataFrame(predictions_area_2,index=pd.date_range(start='2005-10-07', end='2005-10-14', freq='h')[:-1])
    test_3 = pd.DataFrame(predicitons_area_3,index=pd.date_range(start='2005-12-16', end='2005-12-23', freq='h')[:-1])
    test = pd.concat([test_1,test_2,test_3], axis=1)
    test.columns = ['area_1','area_2','area_3']
    test.index.name = 'date'
    test = test.reset_index().melt(id_vars='date',value_vars=['area_1','area_2','area_3']).set_index('date')
    test = test.dropna()
    test = test.drop('variable',axis=1)
    test.to_csv('submission.csv')
    return test