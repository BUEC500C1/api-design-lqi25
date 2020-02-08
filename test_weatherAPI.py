# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 13:27:34 2020

@author: 18367
"""
import pytest
from weather import get_city_weather,forecast_airport_weather,get_airport_weather,current_weather

def test_weather():
    assert get_city_weather("Boston")
    assert get_airport_weather("Total Rf Heliport")
    assert forecast_airport_weather("Total Rf Heliport")