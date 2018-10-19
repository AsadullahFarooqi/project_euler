"""
p 17 : If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

import time
from num2words import num2words

def count_num_words(num):
	return sum((1 for i in num2words(num) if i.isalpha()))

def nums_latter_count():
	ones = len("one,two,three,four,five,six,seven,eight,nine".replace(",","") * (190))
	tenes = len("ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen".replace(",","") * 10)
	tenes2 = len("twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety".replace(",","") * 100)
	hundred = len("hundred" *900)
	and_ = len("and"*891)
	thousand = 11
	return ones+tenes+tenes2+hundred+and_+thousand

if __name__ == "__main__":

	print(sum((count_num_words(num) for num in range(1, 1001))))

	# start2 = time.perf_counter()
	# print(nums_latter_count(), " i am done")
	# stop2 =  time.perf_counter()
	# print("Time ", stop2 - start2)
	