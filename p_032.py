"""
Pandigital products
Problem 32 
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

s = "123456789" # "".join(str(i) for i in range(1, 10))
def is_pandigital(x,y,z):
	t = str(x) + str(y) + str(z)
	return "".join(sorted(t)) == s


if __name__ == '__main__':
	ans = []
	for i in range(1, 10000):
		for j in range(1, 1000):
			if is_pandigital(i,j, i*j):
				# print(i*j, " : ", i , j)
				ans.append(i*j)

	print(sum(set(ans)))
