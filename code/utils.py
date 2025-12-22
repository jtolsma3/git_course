import datetime
import math

def get_birthdate(person = "me"):
    birthdates = {
        "me":datetime.datetime(year = 1986, month = 7, day = 19),
        "mom":datetime.datetime(year = 1953,month = 5, day = 29),
        "dad":datetime.datetime(year = 1950,month = 3, day = 5)
    }

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

    events = {
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
    }

    event_name_clean = event_name.lower().strip()
    if event_name_clean in list(events.keys()):
        return events.get(event_name_clean)
    else:
        raise ValueError("this event is not included in the dictionary of stored events")

# create a function to compute days since a particular event, like a birthday
def get_days_since_event(event_date):
    return (datetime.datetime.now() - event_date).days + 1

# create a function to compute years since a particualr event, like a major event from world history
def get_years_since_event(event_year):
    return math.ceil((datetime.datetime.now() - event_year).days/365.25)
