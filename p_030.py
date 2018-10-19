"""
p 30: Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
def digit_powers():
	n = 2
	ans = 0
	while n <= 1000000:
		if n == sum([int(x)**5 for x in str(n)]):
			print(n)
			ans += n
			# break
		n += 1

	print(ans)

if __name__ == "__main__":
	digit_powers()