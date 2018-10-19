import itertools

def coin_sum():
	ways = []
	l = [1,2,5, 10, 20, 50, 100, 200]
	
	for i in range(1,len(l)+1):
		for j in itertools.permutations(l[:i], 200):
			print(sum(j))
			if sum(j) == 200:
				ways.append(j)

	print(len(ways))

# coin_sum()
