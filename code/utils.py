import datetime
from random import randint
from websites import website_list
# import math
import requests
from const import birthdates,event_list,presidential_birth_years,wmo_codes
from pgeocode import Nominatim

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

def get_family_location(postal_code):
    df = Nominatim("US").query_postal_code(postal_code)
    return df["latitude"],df["longitude"]

def get_weather(lat,long):
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
    conditions = wmo_codes[weather_code].strip().lower()
    
    return temp_C,temp_F,conditions

def print_weather(state,city,family,temp_C,temp_F,conditions):
    if state and city:
        print(f"\nThe current weather at my location of {city}, {state} is {temp_F} F ({temp_C} C) and {conditions}.")
    elif family:
        family_formatted = family.strip().replace("_"," ").title()
        print(f"\nThe current weather for {family_formatted} is {temp_F} F ({temp_C} C) and {conditions}.")
    else:
        raise ValueError("invalid values for either your location or family location.")


