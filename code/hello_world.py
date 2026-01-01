import datetime
import utils
import math


# compute system timezone 
aware_local_now = datetime.datetime.now().astimezone()
local_tz = aware_local_now.tzinfo

# compute days until Christmas
if datetime.datetime.now().month == 12 and datetime.datetime.now().day > 25:
  christmas = datetime.datetime(year = datetime.datetime.now().year+1, month = 12, day = 25)
else:
  christmas = datetime.datetime(year = datetime.datetime.now().year, month = 12, day = 25)
days_to_christmas = (christmas - datetime.datetime.now()).days + 1

# compute days of life
days_of_life = utils.get_days_since_birth(person = "me")

# compute days of life for my parents
days_of_life_m = utils.get_days_since_birth(person = "mom")
days_of_life_d = utils.get_days_since_birth(person = "dad")

# compute time the American Revolution
event = "american_independence"
year_gap = utils.get_years_since_event(event)

# compute time since the French Revolution
event2 = "french_revolution"
year2_gap = utils.get_years_since_event(event2)

# compute time since WWI
event3 = "ww1"
year3_gap = utils.get_years_since_event(event3)

# compute time since WWII
event4 = "ww2"
year4_gap = utils.get_years_since_event(event4)

# compute time since the moon landing
event5 = "moon_landing"
year5 = datetime.datetime(year = utils.get_event_year(event5),month = 1, day = 1)
year5_gap = math.ceil((datetime.datetime.now() - year5).days/365.25)
print(year5.year)

# compute time since the Battle of Hastings
event6 = "battle_of_hastings"
year6_gap = utils.get_years_since_event(event6)

date_paragraph = f"""
It's {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} in {local_tz} time zone and I would just like to say, 'Hello World!!!
It's {days_to_christmas} days until Christmas!

I have lived a total of {days_of_life} days!!
Mom has lived {days_of_life_m} days and dad has lived {days_of_life_d} days!!

The {event.replace("_"," ").title()} happened {year_gap} years ago!!
The {event2.replace("_"," ").title()} happened {year2_gap} years ago!!

{event3.upper()} happened {year3_gap} years ago!!
{event4.upper()} happened {year4_gap} years ago!!
The {event5.replace("_"," ")} happened {year5_gap} years ago!!
The {event6.replace("_"," ").title()} happened {year6_gap} years ago!!
"""

print(date_paragraph)
utils.get_anniversary_events()
utils.get_presidential_age("rutherford_b_hayes")
utils.get_presidential_age("martin_van_buren")

utils.suggest_website()

state,city,lat,long = utils.get_current_location_from_ip()
utils.get_weather(state,city,lat,long)