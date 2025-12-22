import datetime

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
