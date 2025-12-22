import datetime
import utils
import math


# compute system timezone 
aware_local_now = datetime.datetime.now().astimezone()
local_tz = aware_local_now.tzinfo

# compute days until Christmas
christmas = datetime.datetime(year = datetime.datetime.now().year, month = 12, day = 25)
days_to_christmas = (christmas - datetime.datetime.now()).days + 1

# compute days of life
birthdate = utils.get_birthdate(person = "me")
days_of_life = utils.get_days_since_event(birthdate)
print(birthdate.date())

# compute days of life for my parents
birthdate_m = utils.get_birthdate(person = "mom")
days_of_life_m = utils.get_days_since_event(birthdate_m)
print(birthdate_m.date())

birthdate_d = utils.get_birthdate(person = "dad")
days_of_life_d = utils.get_days_since_event(birthdate_d)
print(birthdate_d.date())

# compute time the American Revolution
event = "american_independence"
year = datetime.datetime(year = utils.get_event_year(event),month = 1, day = 1)
year_gap = utils.get_years_since_event(year)
print(year.year)

# compute time since the French Revolution
event2 = "french_revolution"
year2 = datetime.datetime(year = utils.get_event_year(event2),month = 1,day = 1)
year2_gap = utils.get_years_since_event(year2)
print(year2.year)

# compute time since WWI
event3 = "ww1"
year3 = datetime.datetime(year = utils.get_event_year(event3),month = 1,day = 1)
year3_gap = utils.get_years_since_event(year3)
print(year3.year)

# compute time since WWII
event4 = "ww2"
year4 = datetime.datetime(year = utils.get_event_year(event4),month = 1,day = 1)
year4_gap = utils.get_years_since_event(year4)
print(year4.year)

# compute time since the moon landing
event5 = "moon_landing"
year5 = datetime.datetime(year = utils.get_event_year(event5),month = 1, day = 1)
year5_gap = math.ceil((datetime.datetime.now() - year5).days/365.25)
print(year5.year)

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
"""

print(date_paragraph)