"""
p 15:Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
So if the grid is NxN the and N=N. 
And we want to go to from top left to bottom right. 
Then there are exactly N steps to right and exactly N steps to down wards
we can solve such a problem with Binomial theorm because it gives us the
number of ways to choose k elements from an n-element set.
Which in this case there are 20 steps to left and 20 steps to right 
so k = 20 and n = 40  
"""
import math
def binomial(n, k):
	assert 0 <= k <= n
	return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))
print(binomial(40, 20))