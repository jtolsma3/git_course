import datetime
import utils


# compute system timezone 
aware_local_now = datetime.datetime.now().astimezone()
local_tz = aware_local_now.tzinfo

# compute days until Christmas
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


date_paragraph = f"""
It's {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} in {local_tz} time zone and I would just like to say, 'Hello World!!!
It's {days_to_christmas} days until Christmas!

I have lived a total of {days_of_life} days!!
Mom has lived {days_of_life_m} days and dad has lived {days_of_life_d} days!!

The {event.replace("_"," ").title()} happened {year_gap} years ago!!
The {event2.replace("_"," ").title()} happened {year2_gap} years ago!!

{event3.upper()} happened {year3_gap} years ago!!
{event4.upper()} happened {year4_gap} years ago!!
"""

print(date_paragraph)