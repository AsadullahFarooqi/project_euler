from math import ceil, sqrt

"""
Consecutive prime sum
Problem 50 
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""


def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(x**0.5)+1): # ceil(sqrt(x))+1
			if x % i == 0:
				return False
		return True

l_of_primes = [i for i in range(1, 1000000) if is_prime(i)]

def l_of_p_till_n(index_, num):
	for inex in range(len(l_of_primes[:index_])):
		total_of_p = 0
		for i in l_of_primes[inex:index_]:
			if total_of_p > num:
				break
			if total_of_p == num:
				return len(l_of_primes[inex:l_of_primes.index(i)])
			total_of_p += i
	return 0

if __name__ == '__main__':
	
	len_of = 0
	nop = 0

	for i in l_of_primes[::-1]:
		# print(i)
		ans = l_of_p_till_n(l_of_primes.index(i), i)
		# print(len(ans))
		if ans > len_of:
			print(i, ans)
			len_of = ans
			nop = i
		# print()
		# ans = l_of_p_till_n(l_of_primes, 953)
		# print(i, ans)
	print(nop, len_of)