"""
Circular primes
Problem 35 
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

from collections import deque
import math

def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, math.ceil(math.sqrt(x)) + 1, 2):
			if x % i == 0:
				return False
		return True

def rotation(num):
	s_num = deque(num)
	# if len(num) < 2:
	while True:
		s_num.rotate()
		yield int("".join(s_num))
		# print(s_num)
		if s_num == deque(num):
			return
	# for i in range(len(s_num)-1):

def circular_prime_checker(num):
	s_num = str(num)
	for i in rotation(s_num):
		if not is_prime(i):
			return False

	return True



def circular_primes():
	ans = 0
	for i in range(2,1000000):
		# first it'll check if the number is prime or not and then it'll call circular_prime_checker
		# to check all the rotations
		if is_prime(i) and circular_prime_checker(i):
			print(i)
			ans += 1

	print("answer : ", ans)

if __name__ == "__main__":

	circular_primes()