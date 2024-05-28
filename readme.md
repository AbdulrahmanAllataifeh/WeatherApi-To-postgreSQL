# API data to Database
## Overview 

This project marks a significant milestone in my journey as a data engineer, as I have successfully built a robust ETL pipeline to fetch real-time data from the weatherAPI and store it in a PostgreSQL database. Inspired by the <a href="https://github.com/san089/Udacity-Data-Engineering-Projects">Udacity Data Engineering Projects</a>.

In the near future, I plan to automate the ETL pipeline to ensure seamless data processing and minimize manual intervention. This will enable me to focus on higher-level tasks such as data analysis and visualization, ultimately driving business insights and decision-making.
## Config File
```
[KEYS]
API_KEY=<YOUR API KEY>


[DATABASE]
host=<HOST NAME>
database=<DB NAME>
username=<USER NAME>
password=<PASSWORD>
port=<PORT>

```

## Files
```
auth.py - Contains configuration variable for making HTTP Request

weathersearch.py - Contains class to handle results returned from the search request

dbdriver.py - Contains Connection detials to Postgres database and executing queries

queries.py - Contains queries to create schema and tables in postgres and insert statement format

request.py - Contains class to handle making request to the API

driver.py - Entry point for the application, contains parsing command line arguments and control the program flow.
```

## How to Run
`python driver.py --date 2024-05-27 --city Dubai` 

## Raw Input
![RawInput](https://github.com/AbdulrahmanAllataifeh/WeatherApi-To-postgreSQL/blob/master/RawInput.png)


## Results
![RESULTS](https://github.com/AbdulrahmanAllataifeh/WeatherApi-To-postgreSQL/blob/master/Result.png)