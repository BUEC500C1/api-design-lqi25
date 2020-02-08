# api-design-lqi25
## Introduction
Created a weather API based on OpenWeatherAPI and implemented three functions: 
- Enter the city name to get the current weather conditions of the city. 
- Enter the airport name to get the current weather conditions at the airport. 
- Enter the airport name and get the weather conditions for the next 5 days at the airport.

## Target User(s)
- Tourists
- City dweller
- Airport staff

## User Stories
- I, a tourist, want to know the current weather conditions at the airport.
- I, a city dweller, want to know the current weather conditions in the city where I live.
- I, an airport worker, want to know the future weather around the airport.

## OpenWeather API
The OpenWeather API supports multiple functions, which can get the current weather conditions, historical weather records, and forecast future weather conditions by city name, latitude and longitude. You need to register at https://openweathermap.org/api and get the API key. The obtained data format is json data, which includes temperature, weather, latitude and longitude, humidity and other information.

## Weather API
1. Install Requests   
Open terminal and enter the following command：   
```python
pip install requests
```
2. Run weather.py 
- Select the function you need and enter the corresponding number before the function.
Enter 1 and enter the city name to get the current weather conditions for the city, including weather, temperature, humidity and wind speed.      
<p align="center">   
<img src="https://github.com/BUEC500C1/api-design-lqi25/blob/master/img/w2.png"/> 
</p>      
Enter 2 and enter the airport name to get the current weather conditions for that airport.       
<p align="center">   
<img src="https://github.com/BUEC500C1/api-design-lqi25/blob/master/img/w3.png"/> 
</p>         
Enter 3 and enter the name of the airport to get the weather conditions of the airport for the next 5 days at 3 hour intervals.   
<p align="center">
<img src="https://github.com/BUEC500C1/api-design-lqi25/blob/master/img/w4.png"/> 
</p>         
Enter 4 to leave weather API.   
<p align="center">
<img src="https://github.com/BUEC500C1/api-design-lqi25/blob/master/img/w5.png"/> 
</p>

