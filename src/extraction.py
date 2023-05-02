import os
import pandas as pd
import requests




def open_csv_df_temperature (name):
       
    # 1. Establish variables
    path = f"data/{name}.csv"
      
    # 2. We read from the path
    df_csv_temp = pd.read_csv(path)
    
    return df_csv_temp




def open_csv_df_covid (name):
       
    # 1. Establish variables
    path = f"data/{name}.csv"
      
    # 2. We read from the path
    df_csv_covid = pd.read_csv(path)
    
    return df_csv_covid




def open_api_df_1 (url):
      
    # Set query parameters:
    params = {
    'country': 'ES',
    'city': 'Madrid',
    'parameter': 'pm25',
    'limit': 10000,    
    'date_from': '2020-01-01T00:00:00Z',
    'date_to': '2020-05-31T23:59:59Z',
    'page': 1,
    }

    # Send initial API request
    response = requests.get(url, params=params)
    response_json_1 = response.json()

    # Convert the response to a Pandas DataFrame
    df_1 = pd.DataFrame(response_json_1['results'])

    return df_1




def open_api_df_2 (url):
       
    # Set query parameters:
    params = {
    'country': 'ES',
    'city': 'Madrid',
    'parameter': 'pm25',
    'limit': 10000,    
    'date_from': '2020-01-01T00:00:00Z',
    'date_to': '2020-05-31T23:59:59Z',
    'page': 2,
    }

    # Send initial API request
    response = requests.get(url, params=params)
    response_json_2 = response.json()

    # Convert the response to a Pandas DataFrame
    df_2 = pd.DataFrame(response_json_2['results'])

    return df_2




