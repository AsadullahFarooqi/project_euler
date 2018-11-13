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

def F(num):
	# ans = 0
	# for num in range(1, lim):
	for i in range(2, int(num**0.5)+1):
		for j in range(2, int(num**0.33333333)+1):
			if ((i**2) * (j**3)) == num:
				
				# print(i,j, (i**2) * (j**3))
				return True
				# ans += 1
			
			# print(num)
	return False

if __name__ == '__main__':
	ans = 0
	for i in range(1, 3000000+1):
		if is_prime(i):
			continue
		if F(i):
			# print(i)
			ans += 1
		# print(i)
	# F(9*(10**18))
	print(ans+ 2014)