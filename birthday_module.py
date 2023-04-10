from datetime import datetime
import calendar


def get_time() -> tuple:
	"""
	Returns the current year, month, day, hour, minute and second
	"""

	TODAY = datetime.now()
	YEAR = TODAY.year
	MONTH = TODAY.month
	DAY = TODAY.day
	HOUR = TODAY.hour
	MINUTE = TODAY.minute
	SECOND = TODAY.second
	return YEAR, MONTH, DAY, HOUR, MINUTE, SECOND


def get_year(year: int) -> int:
	"""
	Converts the year in the format "YY" to "YYYY"
	"""

	YEAR, MONTH, DAY, HOUR, MINUTE, SECOND = get_time()
	if year <= int(str(YEAR)[-2:]):
		year += 2000
	
	elif 22 < year < 100:
		year += 1900

	return year


def already(day: int, month: int) -> bool:
	"""
	Returns whether it's past the birthdate (True) or not (False)
	"""

	YEAR, MONTH, DAY, HOUR, MINUTE, SECOND = get_time()
	if month > MONTH:
		return False
	elif month < MONTH:
		return True
	else:
		if day > DAY:
			return False
		elif day <= DAY:
			return True


def get_age(day: int, month: int, year: int) -> int:
	"""
	Calculates the age based on the current date
	"""

	YEAR, MONTH, DAY, HOUR, MINUTE, SECOND = get_time()
	year = get_year(year)
	if already(day, month):
		age = YEAR - year
	else:
		age = YEAR - year - 1 
	return age
	

def get_days(day: int, month: int, year: int) -> int:
	"""
	Calculates the number of days from the specified date until the current date
	"""

	YEAR, MONTH, DAY, HOUR, MINUTE, SECOND = get_time()
	age = get_age(day, month, year)
	leaps = calendar.leapdays(year, YEAR-1)
	
	if calendar.isleap(YEAR):
		months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	else:
		months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

	dayz = 0
	for y in range(year, YEAR+1):
		if calendar.isleap(y):
			dayz += 366
		else:
			dayz += 365

	d_in_t_year = 366 if calendar.isleap(YEAR) else 365
	this_year = sum(months[:MONTH]) - (months[:MONTH][-1] - DAY) # before today
	born_year = (sum(months[:month]) - (months[:month][-1] - day)) # before born

	other_days_in_this_year = d_in_t_year - this_year # after today

	mid_time = dayz - (other_days_in_this_year + born_year)

	return mid_time


def get_hours(day: int, month: int, year: int) -> int:
	"""
	Calculates the number of hours from 00:00:00 of the specified date until 00:00 of the current date
	"""
	return get_days(day, month, year) * 24


def get_minutes(day: int, month: int, year: int) -> int:
	"""
	Calculates the number of minutes from 00:00:00 of the specified date until 00:00 of the current date
	"""

	return get_hours(day, month, year) * 60


def get_seconds(day: int, month: int, year: int) -> int:
	"""
	Calculates the number of seconds from 00:00:00 of the specified date until 00:00:00 of the current date
	"""

	return get_minutes(day, month, year) * 60


def get_weeks(day: int, month: int, year: int) -> int:
	"""
	Calculates the number of weeks from the specified date until the current date
	"""

	return int(get_days(day, month, year) / 7)


def get_months(day: int, month: int, year: int) -> int:
	"""
	Calculates the number of months from the specified date until the current date
	"""

	YEAR, MONTH, DAY, HOUR, MINUTE, SECOND = get_time()
	age = get_age(day, month, year)

	if already(day, month):
		number_of_months = age * 12 + (MONTH - month)
	
	else:
		number_of_months = (age + 1) * 12 - month + MONTH
		if day > DAY and month > MONTH:
			number_of_months = (age * 12) + (12 - month + MONTH) - 1

	return number_of_months

