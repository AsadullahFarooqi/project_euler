"""
Distinct primes factors
Problem 47 
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""


def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, (x//2)+1):
			if x % i == 0:
				return False
		return True

def primes_in_range():
	n = 1
	while True:

		prime_factors_of_f = [x for x in range(1,(n//2)+1) if n % x == 0 and is_prime(x)]
		prime_factors_of_s = [x for x in range(1,((n+1)//2)+1) if (n+1) % x == 0 and is_prime(x)]		
		prime_factors_of_t = [x for x in range(1,((n+2)//2)+1) if (n+2) % x == 0 and is_prime(x)]
		prime_factors_of_4 = [x for x in range(1,((n+3)//2)+1) if (n+3) % x == 0 and is_prime(x)]

		# if len(set(prime_factors_of_f)) == 2 and len(set(prime_factors_of_s)) == 2:
		# 	print(prime_factors_of_f, " :: ", n)
		# 	print(prime_factors_of_s, " :: ", n+1)
		# 	break

		# if len(set(prime_factors_of_f)) == 3 and len(set(prime_factors_of_s)) == 3 and len(set(prime_factors_of_t)) == 3:
		# 	print(prime_factors_of_f, " :: ", n)
		# 	print(prime_factors_of_s, " :: ", n+1)
		# 	print(prime_factors_of_t, " :: ", n+2)
		# 	break

		if len(set(prime_factors_of_f)) == 4 and len(set(prime_factors_of_s)) == 4 and len(set(prime_factors_of_t)) == 4 and len(set(prime_factors_of_4)) == 4:
			print(prime_factors_of_f, " :: ", n)
			print(prime_factors_of_s, " :: ", n+1)
			print(prime_factors_of_t, " :: ", n+2)
			print(prime_factors_of_t, " :: ", n+3)

			break
		n += 1

if __name__ == '__main__':
	primes_in_range()