dict_of_divisors = {}
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

if __name__ == '__main__':
	l = [div_finder(i) for i in range(1,1000000)]
	print(l)

# print(amicable(10000))