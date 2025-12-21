import datetime
import zoneinfo

aware_local_now = datetime.datetime.now().astimezone()
local_tz = aware_local_now.tzinfo


print(f"It's {datetime.datetime.now().strftime("%Y-%m-%d %H:%M")} in {local_tz} time zone and I would just like to say, 'Hello World!!!'")