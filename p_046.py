"""
Goldbach's other conjecture
Problem 46 
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

l_of_p = []

def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return False
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(x**0.5)+1):
			if x % i == 0:
				return True
		return False

def l_of_primes(end):
	x = l_of_p[-1]+1
	while x <= end:
		if x <= 1:
			x += 1
			continue
			# return False
		elif x <= 3:
			# return True
			l_of_p.append(x)
			x += 1

		elif x % 2 == 0:
			x += 1
			continue
			# return False
		else:
			for i in range(3, int(x**0.5)+1):
				if x % i == 0:
					x += 1
					continue
					# return False
			# return True
			l_of_p.append(x)
			x += 1

def conjecture(num):
	l_of_primes(num)
	for i in l_of_p:
		if i >= num:
			return False
		for j in range(1,i+1):
			if i + (2*(j**2)) == num:
				return True
		
if __name__ == '__main__':
	ans = 0
	i = 1
	while True:
		if i < 9:
			continue
		if i >= 35:
			break 
		if is_prime(i):
			if conjecture(i):
				ans = i
			print(i)
		i+=1

	print("ans : ", ans)

