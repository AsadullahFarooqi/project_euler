"""
Pandigital prime
Problem 41 
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

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

def is_pandigital(num):
	return len(num) == len(set(num))

def compute_answer():
	for i in range(7777777, 2, -1):
		if "0" in str(i) or "8" in str(i) or "9" in str(i):
			continue
		if is_pandigital(str(i)):
			# print(i)
			if is_prime(i):
				print("ans : ", i)
				break
				return

if __name__ == '__main__':
	compute_answer()
