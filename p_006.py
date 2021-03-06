"""
06 : The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
def sum_of_squares(n):
	l = list(i**2 for i in range(n+1))
	return sum(l)
def square_of_sums(n):
	return (sum(range(n+1)))**2
# print(square_of_sums(100)- sum_of_squares(100))
