
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
		

def formula_(n, a, b):
	return (n**2) + (a*n) + b

if __name__ == "__main__":
	for i in range(1,41):
		print(formula_(i, i, 41))