def isLeapYear(year):
	return ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)

def count_sundays():
	sundays = 0
	days = [31,28,31,30,31,30,31,31,30,31,30,31]
	year = 1900
	weekday = 1
	
	while year < 2001:
		if isLeapYear(year):
			days[1] = 29
		else:
			days[1] = 28
		
		for month in range(0, 12):
			for day in range(0, days[month]):
				
				if day == 0 and weekday == 7 and year >= 1901:
					print("hit: " + str(year) + ", " + str(month) + ", " + str(day))
					sundays += 1
				
				weekday += 1	
				if weekday == 8:
					weekday = 1
		year += 1
		
	return sundays
	
print(count_sundays())
