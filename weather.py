# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:31:40 2020

@author: 18367
"""

import requests
import csv

key = '5a05e6b823b0c38116d07afbc034e3c1'

def get_city_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?" + "&q=" + city + "&appid=" + key
    data = requests.get(url).json()
    print()
    print("City:",city)
    current_weather(data)
    print()

def forecast_airport_weather(airport):
    with open ('C:\\Users\\18367\\Desktop\\airports.csv') as airportinfo:
        airportlist = csv.DictReader(airportinfo)
        for row in airportlist:
            if row['name']== airport:
                lati = row['latitude_deg']
                logi = row['longitude_deg']
                region = row['iso_region']
                print()
                print("Region:",region)
                print("Airport:",airport)
                url = "http://api.openweathermap.org/data/2.5/forecast?" + "lat=" + lati + "&lon=" + logi + "&appid=" + key
                data = requests.get(url).json()
                #print(data)
                info_list=data['list']
                for info in info_list:
                    ttime = info['dt_txt']
                    wweather = info['weather'][0]['description']
                    ttemp = info['main']['temp']
                    print(ttime," weather:",wweather," temperature:",ttemp)
                
def get_airport_weather(airport):
    with open ('C:\\Users\\18367\\Desktop\\airports.csv') as airportinfo:
        airportlist = csv.DictReader(airportinfo)
        for row in airportlist:
            if row['name']== airport:
                lati = row['latitude_deg']
                logi = row['longitude_deg']
                region = row['iso_region']
                print()
                print("Region:",region)
                print("Airport:",airport)
                url = "http://api.openweathermap.org/data/2.5/weather?" + "lat=" + lati + "&lon=" + logi + "&appid=" + key
                data = requests.get(url).json()
                current_weather(data)

def current_weather(data):
    print("Lon:",data['coord']['lon'],"Lat:",data['coord']['lat'])
    print("Weather:",data['weather'][0]['description'])
    print("Temperature:",data['main']['temp'])
    print("Humidity:",data['main']['humidity'])
    print("Wind speed:",data['wind']['speed'])
   
def main():
    while True:
        print("1.Current weather in the city.")
        print("2.Current weather at the airport.")
        print("3.Weather at the airport for the next 5 days.")
        print("4.Leave the API.")
        num = input("Please enter the number:")
        if num == '1':
            city = input("Please enter a city name:")
            get_city_weather(city)
            print()
        if num == '2':
            airport = input("Please enter an airport name:")
            get_airport_weather(airport)
            print()
        if num == '3':
            airport = input("Please enter an airport name:")
            forecast_airport_weather(airport)
            print()
        if num == '4':
            break

if __name__ == '__main__':
    main()