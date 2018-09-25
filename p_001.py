"""
01 : If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
def multiples_of_x_y(x,y, limit):
	list_of_multiples = []
	for i in range(1, limit):
		if not i % x or not i % y:
			list_of_multiples.append(i)

	list_of_multiples = set(list_of_multiples)
	print(list_of_multiples)
	return sum(list_of_multiples)
