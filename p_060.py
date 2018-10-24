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

