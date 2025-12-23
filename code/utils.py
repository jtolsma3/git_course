import datetime
# import math

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

# create a function to compute years since a particualr event, like a major event from world history
def get_years_since_event(event_name):
    return datetime.datetime.now().year - get_event_year(event_name)

def get_anniversary_events():
    for event_name,year in event_list.items():
        anniv_value = datetime.datetime.now().year - get_event_year(event_name)
        if anniv_value % 100 == 0:
            print(f"{event_name.replace("_"," ").title()} happened *exactly* {anniv_value} years ago!!")