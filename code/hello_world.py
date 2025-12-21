import datetime
import utils

# compute system timezone 
aware_local_now = datetime.datetime.now().astimezone()
local_tz = aware_local_now.tzinfo

# compute days until Christmas
christmas = datetime.datetime(year = datetime.datetime.now().year, month = 12, day = 25)
days_to_christmas = (christmas - datetime.datetime.now()).days + 1

# compute days of life
birthdate = utils.get_birthdate()
days_of_life = (datetime.datetime.now() - birthdate).days + 1 

print("")
print(f"It's {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} in {local_tz} time zone and I would just like to say, 'Hello World!!!'")
print(f"It's {days_to_christmas} days until Christmas!")
print(f"I have lived a total of {days_of_life} days!!")
print("")