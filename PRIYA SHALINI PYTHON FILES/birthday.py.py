from datetime import datetime

def date_diff_in_seconds(dt2, dt1):
  timedelta = dt1 - dt2
  return timedelta.days * 24 * 3600 + timedelta.seconds

def dhms_from_seconds(seconds):
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	days, hours = divmod(hours, 24)
	return (days, hours, minutes, seconds)

#Specified date
date1 = datetime.strptime('23-11-2022 01:00:00', '%d-%m-%Y %H:%M:%S')

#Current date
date2 = datetime.now()

print("countdown for the birthday is: \n%d days, %d hours, %d minutes, %d seconds" % dhms_from_seconds(date_diff_in_seconds(date2, date1)))
print()
int(input(datetime.now()))
print("%d",dhms_from_seconds)
