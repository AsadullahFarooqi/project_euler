"""
Square digit chains
Problem 92 
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

def squar_sum(s_n):
	ans = 0
	if s_n == "89":
		return True
	elif s_n == "1":
		return False
	for i in s_n:
		ans += int(i)**2
	return squar_sum(str(ans))

if __name__ == '__main__':
	ans = 0
	for i in range(1, 10000000):
		if squar_sum(str(i)):
			ans += 1
			print(i, ans)
		# print(squar_sum(str(89)))

	print("ans : ", ans)