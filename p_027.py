
def is_prime(x):
	if x <= 1:
		return False
	elif x <= 3:
		return True
	elif x % 2 == 0:
		return False
	else:
		for i in range(3, int(x**0.5)+1):
			if x % i == 0:
				return False
		return True

def formula_(n, a, b):
	return (n**2) + (a*n) + b

# def compute():
# 	for i in range(1, 1000):
# 		for j in range(1, 1000):
			
def n(b,p):
	return ((b**(p-1)) - 1) / p 

if __name__ == "__main__":

	for i in range(1,1000):
		if is_prime(i):
			continue
			# print(n(1, i))

	# for i in range(1,41):
	# 	print(formula_(i, i, 41))