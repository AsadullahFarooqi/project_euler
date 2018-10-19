"""
p 21 : 
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def div_finder(num):
	l = []
	for i in range(1, (num//2)+1):
		if num % i == 0:
			l.append(i)
	return sum(l)

def amicable(n):
	l_amicable = []
	for i in range(1,n+1):
		a_divs = div_finder(i)
		# b_divs = div_finder(i_divs)
		if i == div_finder(a_divs) and i != a_divs:
			l_amicable.append(i)
	return sum(l_amicable)


print(amicable(10000))
