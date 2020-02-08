# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 13:27:34 2020

@author: 18367
"""
import pytest
from weather import get_city_weather,forecast_airport_weather,get_airport_weather,current_weather

def test_weather():
    get_city_weather("Boston")
    get_city_weather("London")
    get_city_weather("New York")
    get_airport_weather("Total Rf Heliport")
    forecast_airport_weather("Total Rf Heliport")
    get_airport_weather("Aero B Ranch Airport")
    forecast_airport_weather("Aero B Ranch Airport")
    get_airport_weather("Newport Hospital & Clinic Heliport")
    forecast_airport_weather("Newport Hospital & Clinic Heliport")
