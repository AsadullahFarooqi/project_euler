"""
Truncatable primes
Problem 37 :
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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

def truncat_checker(num):
	for i in range(len(num)-1, 0, -1):
		# print(num[:i])
		if not is_prime(int(num[:i])):
			return False

	for j in range(1, len(num)):
		# print(num[j:])
		if not is_prime(int(num[j:])):
			return False

	return True

# print(truncat_checker(str(37897)))

def compute_answer():
	truncatable_p = []
	counter = 9
	while True:
		if len(truncatable_p) >= 11:
			break

		if is_prime(counter):
			if truncat_checker(str(counter)):
				# print(counter)
				truncatable_p.append(counter)
				counter += 1
			else:
				counter += 1
		else:	
			counter += 1

	print(sum(truncatable_p), " : ", truncatable_p)

if __name__ == '__main__':
	compute_answer()