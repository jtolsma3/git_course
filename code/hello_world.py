import datetime
import zoneinfo

aware_local_now = datetime.datetime.now().astimezone()
local_tz = aware_local_now.tzinfo
christmas = datetime.datetime(year = datetime.datetime.now().year, month = 12, day = 25)
days_to_christmas = (christmas - datetime.datetime.now()).days


print(f"It's {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} in {local_tz} time zone and I would just like to say, 'Hello World!!!'")
print(f"It's {days_to_christmas} days until Christmas!")