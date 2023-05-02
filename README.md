# Project2-API-and-Scrapping
## Goal
The goal of this project is to find an API and realate its information to a Dataset.

## Information source
1. **Dataset 1**: dataset hosted on Kaggel (https://www.kaggle.com/) titled "Daily Temperature of Major Cities". The dataset contains daily temperature readings for major cities around the world. The temperature readings are provided in degrees Celsius (°C) and cover a period from 1985 to 2020.
2. **Dataset 2**: dataset hosted on Kaggle (https://www.kaggle.com/) titled "COVID-19 Daily Case & Hospitalization Spain Dataset". The dataset contains information about daily COVID-19 cases and hospitalizations in Spain. The data covers a period from February 2020 to July 2021, and includes information about the number of confirmed cases, hospitalizations, and deaths for each day and region.
2. **API**: API (Application Programming Interface) hosted on OpenAQ, an open platform for air quality data from various locations around the world.

## Database description
**Database 1**: 
- Each row of the database refers to a daily average temperature measurement.
- For each temperature measurement it is given certain information such as the region, country, state, city, date, among others.
- The database contains 2.906.327 rows and 8 columns.

**Database 2**: 
- Each row of the database refers to a daily count of covid cases.
- For each covid case it is given certain information such as the province and date.
- The database contains 43.778 rows and 8 columns.

## API description
In order to get all the information that matches the request made to the selected API, it was necessary to make two different request, due to the limit on the response. After making the two requests, both resulting dataframes have been merged.
- Each row of the database refers to PM2.5 measurement on a certain coordinate. PM2.5 (Particulate Matter 2.5) is a measure of air pollution that refers to tiny particles in the air that are 2.5 micrometers or smaller in diameter. These particles can be made up of a variety of substances, including dust, soot, and smoke, and can come from both natural and human-made sources. Exposure to high levels of PM2.5 has been linked to respiratory and cardiovascular problems, including asthma, bronchitis, and heart disease.
- For each covid case it is given certain information such as the country, city, date, etc.
- The database contains 24.549 rows and 8 columns.

## HYPOTHESIS
1. Find any possible relation between air pollution and temperature in first covid months and precovid months (Jan-May 2020)
2. Find any possible relation between air pollution and covid cases in first covid months and precovid months (Jan-May 2020)

## Cleaning data - Database 1 (temperature)
- Filter only rows where the country is Spain, city is Madrid, year 2020, and month is January, February, March, April, or May.
- Drop column state as it is not useful for our analisys.
- Check for null values and duplicates.
- Replace each value in the 'Month' column with a string representing the corresponding month.

## Cleaning data - Database 2 (covid cases)
- Filter only rows where the province is Madrid and year 2020.           
- Drop the following columns as they are not useful for our analisys: "num_casos_prueba_pcr", "num_casos_prueba_test_ac", "num_casos_prueba_ag", "num_casos_prueba_elisa", "num_casos_prueba_desconocida".
- Check for null values and duplicates.
- Extract the month and year into new columns.
- Replace each value in the 'Month' column with a string representing the corresponding month.
        
## Cleaning API (air pollution)
- Extract information from dictionaries and drop them after.
- Create new colum for year, month and day, respectively.
- Check for null values and duplicates.
- Replace each value in the 'Month' column with a string representing the corresponding month.

## HYPOTHESIS 1 - Conclusions

The values of PM2.5 increased in April 2020. One possible reason can be that the restrictions and confinement measures implemented to mitigate the spread of COVID-19 reduced the number of vehicles on the streets and the economic activity, leading to a decrease in the emissions of other pollutants, which in turn favored the accumulation of PM2.5 in the air. Meanwhile, if we observe the temperature plot, we can see a slight increase of the dayly average temperature after covid restrictions. Air pollution can lead to increased temperatures due to the greenhouse effect, but we cannot assume this fact by the analyzed datasets because the effect is not instantaneous.

## HYPOTHESIS 2 - Conclusions
The number of covid cases increased on March, but after restructions the cases dicreased significantly until August, that the lack of restrictions lead to higher rate of covid cases. If we compare these results to air pollution, we can see that the maxium average value for PM2.5 measurement (April) does not lead to higher covid cases, although PM2.5 high levels can represent a risk to human health. The most logical explanation is that the restrictions had a higher impact (lowering spread of covid) than a higher level of air pollution. 


