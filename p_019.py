import datetime

"""
p 19: How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def count_sundays():
	counter = 0
	for year in range(1901, 2001):
		for month in range(1,13):
			if datetime.date(year, month, 1).weekday() == 6:
				counter += 1
	return counter

if __name__ == "__main__":
	print(count_sundays())