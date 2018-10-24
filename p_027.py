"""
Quadratic primes
Problem 27 
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

"""

def is_prime(x, cache={}):
	if x in cache:
		return cache[x]
	if x <= 1:
		cache[x] = False
		return False
	elif x <= 3:
		cache[x] = True
		return True
	elif x % 2 == 0:
		cache[x] = False
		return False
	else:
		for i in range(3, int(x**0.5)+1):
			if x % i == 0:
				cache[x] = False
				return False
		cache[x] = True
		return True

def quadretic_p(a, b):
	n = 0
	val = abs(n**2 + a*n + b)
	prime = is_prime(val)
	while prime:
		yield val
		n += 1
		val = abs(n**2 + a*n + b)
		prime = is_prime(val)
			

if __name__ == "__main__":

	longest_p_list = (0,0,0)
	for a in range(-999, 1000):
		for b in range(-1000, 1001):
			p = [x for x in quadretic_p(a,b)]
			if len(p) > longest_p_list[2]:
				longest_p_list = (a,b, len(p))

	print(longest_p_list, longest_p_list[2])
	print(longest_p_list[0]* longest_p_list[1])