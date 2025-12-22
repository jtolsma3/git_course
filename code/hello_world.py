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
days_of_life = (datetime.datetime.now() - birthdate).days + 1 

# compute days of life for my parents
birthdate_m = utils.get_birthdate(person = "mom")
days_of_life_m = (datetime.datetime.now() - birthdate_m).days + 1

birthdate_d = utils.get_birthdate(person = "dad")
days_of_life_d = (datetime.datetime.now() - birthdate_d).days + 1

# compute time the American Revolution
event = "american_independence"
year = datetime.datetime(year = utils.get_event_year(event),month = 1, day = 1)
year_gap = math.ceil((datetime.datetime.now() - year).days/365.25)

# compute time since the French Revolution
event2 = "french_revolution"
year2 = datetime.datetime(year = utils.get_event_year(event2),month = 1,day = 1)
year2_gap = math.ceil((datetime.datetime.now() - year2).days/365.25)

print("")
print(f"It's {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} in {local_tz} time zone and I would just like to say, 'Hello World!!!'")
print(f"It's {days_to_christmas} days until Christmas!")
print(f"I have lived a total of {days_of_life} days!!")
print(f"Mom has lived {days_of_life_m} days and dad has lived {days_of_life_d} days!!")
print(f"The {event.replace("_"," ").title()} happened {year_gap} years ago!!")
print(f"The {event2.replace("_"," ").title()} happened {year2_gap} years ago!!")
print("")