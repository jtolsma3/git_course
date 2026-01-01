import datetime
from random import randint
from websites import website_list
# import math
import requests

WMO_CODE_TO_TEXT = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    56: "Light freezing drizzle",
    57: "Dense freezing drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    66: "Light freezing rain",
    67: "Heavy freezing rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}

event_list = {
    "fall_of_rome": 476,
    "battle_of_hastings": 1066,
    "magna_carta": 1215,
    "black_death": 1347,
    "columbus_voyage": 1492,
    "luther_95_theses": 1517,
    "american_independence": 1776,
    "french_revolution": 1789,
    "ww1": 1914,
    "ww2": 1939,
    "moon_landing": 1969,
    "fall_of_berlin_wall": 1989,
    "battle_of_waterloo": 1825,      # intentionally simplified
    "railway_age_begins": 1825,
    "founding_of_singapore": 1825,
    "roaring_twenties_peak": 1925,
    "american_independence": 1776,
    "french_revolution": 1789,
    "ww1": 1914,
    "ww2": 1939,
    "moon_landing": 1969,
    "fall_of_berlin_wall": 1989,
    "magna_carta": 1215,
}

birthdates = {
    "me":datetime.datetime(year = 1986, month = 7, day = 19),
    "mom":datetime.datetime(year = 1953,month = 5, day = 29),
    "dad":datetime.datetime(year = 1950,month = 3, day = 5)
}

presidential_birth_years = {
    "millard_fillmore": 1800,
    "franklin_pierce": 1804,
    "james_buchanan": 1791,
    "chester_a_arthur": 1829,
    "benjamin_harrison": 1833,
    "rutherford_b_hayes": 1822,
    "zachary_taylor": 1784,
    "martin_van_buren": 1782,
    "william_henry_harrison": 1773,
    "john_tyler": 1790,
}

def get_birthdate(person = "me"):

    person_clean = person.lower().strip()
    if person_clean in list(birthdates.keys()):
        return birthdates.get(person_clean)
    else:
        raise ValueError("the only valid values for person are 'me','dad', and 'mom'")
    
def get_event_year(event_name):
    """
    Return the year (CE) of a major historical event.
    Returns None if the event is unknown.
    """
    event_name_clean = event_name.lower().strip()
    if event_name_clean in list(event_list.keys()):
        return event_list.get(event_name_clean)
    else:
        raise ValueError("this event is not included in the dictionary of stored events")

# create a function to compute days since a particular event, like a birthday
def get_days_since_birth(person):
    birthdate = get_birthdate(person)
    return (datetime.datetime.now() - birthdate).days + 1

# create a function to compute years since a particular event, like a major event from world history
def get_years_since_event(event_name):
    return datetime.datetime.now().year - get_event_year(event_name)

def get_anniversary_events():
    for event_name,year in event_list.items():
        anniv_value = datetime.datetime.now().year - get_event_year(event_name)
        if anniv_value % 100 == 0:
            print(f"{event_name.replace("_"," ").title()} happened *exactly* {anniv_value} years ago!!")

# display hypothetical ages of presidents if they were alive today
def get_presidential_age(president):
    pres_age = datetime.datetime.now().year - presidential_birth_years[president]
    print("")
    print(f"Can you belive that, if {president.replace("_"," ").title()} were alive today, he would be {pres_age} years old?!")

# suggets a website to the user from a list of website in websites.py
def suggest_website():
    i = randint(a = 0, b = len(website_list)-1)
    print("")
    print(f"I suggest you try visiting {website_list[i]} sometime.")

# get the user's location using ip address; this will be used to show the current weather

def get_current_location_from_ip():
    resp = requests.get("http://ip-api.com/json").json()
    return resp["region"],resp["city"],resp["lat"],resp["lon"]

def get_weather(state,city,lat,long):
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": long,
        "current_weather": True,
    }
    resp = requests.get(url, params=params).json()
    weather_code = resp["current_weather"]["weathercode"]
    temp_C = resp["current_weather"]["temperature"]
    temp_F = (temp_C*9/5) + 32
    print(f"\nThe current weather in {city}, {state} is {temp_F} F ({temp_C} C) and {WMO_CODE_TO_TEXT[weather_code].strip().lower()}!!\n")


