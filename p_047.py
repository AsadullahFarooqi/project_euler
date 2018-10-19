
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
	
	# n = 134043
	n = 374
	while True:

		prime_factors_of_f = [x for x in range(1,(n//2)+1) if n % x == 0 and is_prime(x)]
		n += 1
		prime_factors_of_s = [x for x in range(1,((n+1)//2)+1) if (n+1) % x == 0 and is_prime(x)]		
		n += 1
		prime_factors_of_t = [x for x in range(1,((n+2)//2)+1) if (n+2) % x == 0 and is_prime(x)]
		n += 1
		# prime_factors_of_4 = [x for x in range(1,((n+3)//2)+1) if (n+3) % x == 0 and is_prime(x)]

		if len(set(prime_factors_of_f)) == 3 and len(set(prime_factors_of_s)) == 3 and len(set(prime_factors_of_t)) == 3:
			print(prime_factors_of_f, " :: ", n-2)
			print(prime_factors_of_s, " :: ", n-1)
			print(prime_factors_of_t, " :: ", n)
			break
		# if len(set(prime_factors_of_f)) == 4 and len(set(prime_factors_of_s)) == 4 and len(set(prime_factors_of_t)) == 4 and len(set(prime_factors_of_4)) == 4:
		# 	print(prime_factors_of_f, " :: ", n, n+1)
		# 	break
		print(n)


	# print("primes : ", primes, " :: ", n)
# l = []
# for i in range(1,(n//2)+1):
# 	print(i)
# 	if n % i == 0 and is_prime(i):
# 		l.append(i)

# print(l)
# n = 644
# print([x for x in range(1,(n//2)+1) if n % x == 0 and is_prime(x)])
# n2 = 644
# print([x for x in range(1,(n2//2)+1) if n2 % x == 0 and is_prime(x)])
# n3 = 644
# print([x for x in range(1,(n3//2)+1) if n3 % x == 0 and is_prime(x)])
primes_in_range()