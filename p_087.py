
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

# l_of_primes = [i for i in range(1, 2500000000000000) if is_prime(i)]


def prime_power_triples1(num):

	for i in l_of_primes:
		# p1 = i**2
		if i > num**0.5:
			break
		for j in l_of_primes:
			# p2 = j**3
			if j > num**0.33333:
				break
			for k in l_of_primes:
				# p3 = k**4
				if k > num**0.25:
					break
				if i**2 + j**3 + k**4 == num:
					return True

	return False


def prime_power_triples(num):
	for i in l_of_primes:
		p1 = i**2
		if p1 >= num:
			break
		for j in l_of_primes:
			p2 = j**3
			if p2 >= num:
				break
			for k in l_of_primes:
				p3 = k**4
				if p3 >= num:
					break
				if p1 + p2 + p3 == num:
					return True

	return False

# if __name__ == '__main__':
	
	# ans = 0
	# print(l_of_primes)
	# for i in range(28, 5000000):
	# 	# pows_ = (int(i**0.5),int(i**0.25)+1)
	# 	# if prime_power_triples1(i):
	# 	if prime_power_triples(i):
	# 		ans += 1
	# 		print(ans)

	# print("got it : ", ans)