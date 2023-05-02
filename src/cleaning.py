import pandas as pd



def basic_cleaning_csv_temperature (df_csv_temp):
    
    # Filter only rows where the country is Spain, city is Madrid, year is 2018, 2019, or 2020, and month is January, February, March, April, or May.           
    df_csv_temp = df_csv_temp[(df_csv_temp['Country'] == 'Spain') & (df_csv_temp['City'] == 'Madrid') & (df_csv_temp['Year'].isin([2018, 2019, 2020])) & (df_csv_temp['Month'].isin([1, 2, 3, 4, 5]))]
    # Drop column state as it is not useful for our analisys
    df_csv_temp.drop(columns=["State"], axis = 1, inplace = True)
    # Check for null values:
    pd.isna(df_csv_temp).sum()
    # Check for duplicates:
    df_csv_temp.duplicated().sum()
    # Replace each value in the 'Month' column with a string representing the corresponding month:
    months_dict = {1: 'January', 2: 'February', 3: 'March (Covid)', 4: 'April', 5: 'May'}
    df_csv_temp['Month'] = df_csv_temp['Month'].replace(months_dict)

    return df_csv_temp

def basic_cleaning_csv_covid (df_csv_covid):
    
    # Filter only rows where the province is Madrid and year 2020.           
    df_csv_covid = df_csv_covid[(df_csv_covid['provincia_iso'] == 'M') & (df_csv_covid['fecha'] >= '2020-01-01') & (df_csv_covid['fecha'] <= '2020-12-31')]
    # Drop the following columns as they are not useful for our analisys
    df_csv_covid.drop(columns=["num_casos_prueba_pcr", "num_casos_prueba_test_ac", "num_casos_prueba_ag", "num_casos_prueba_elisa", "num_casos_prueba_desconocida"], axis = 1, inplace = True)
    # Check for null values:
    pd.isna(df_csv_covid).sum()
    # Check for duplicates:
    df_csv_covid.duplicated().sum()
    # Convert "fecha" column to datetime format
    df_csv_covid['fecha'] = pd.to_datetime(df_csv_covid['fecha'])
    # Extract the month into a new column
    df_csv_covid['mes_numero'] = df_csv_covid['fecha'].dt.month
    # Extract year into a new column
    df_csv_covid['año'] = df_csv_covid['fecha'].dt.year
    # Replace each value in the 'Month' column with a string representing the corresponding month
    months_dict = {1: 'January', 2: 'February', 3: 'March (Covid)', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    df_csv_covid['mes_nombre'] = df_csv_covid['mes_numero'].replace(months_dict)

    return df_csv_covid

def basic_cleaning_api (df_api):
    
    # Extract information from dictionaries
    df_api['date_utc'] = df_api['date'].apply(lambda x: x['utc'])
    df_api['date_local'] = df_api['date'].apply(lambda x: x['local'])
    df_api['coordinates_latitude'] = df_api['coordinates'].apply(lambda x: x['latitude'])
    df_api['coordinates_longitude'] = df_api['coordinates'].apply(lambda x: x['longitude'])
    # Drop dictionaries
    df_api.drop(columns=["date", "coordinates"], axis = 1, inplace = True)
    # Create new colum for year, month and day, respectively
    df_api['year'] = df_api['date_utc'].apply(lambda x: int(x[:4]))
    df_api['month'] = df_api['date_utc'].apply(lambda x: int(x[6]))
    df_api['day'] = df_api['date_utc'].apply(lambda x: int(x[8:10]))
    # Check for null values:
    pd.isna(df_api).sum()
    # Check for duplicates:
    df_api.duplicated().sum()
    # Replace each value in the 'Month' column with a string representing the corresponding month
    months_dict = {1: 'January', 2: 'February', 3: 'March (Covid)', 4: 'April', 5: 'May'}
    df_api['month_name'] = df_api['month'].replace(months_dict)

    return df_api