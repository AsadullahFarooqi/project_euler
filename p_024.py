from itertools import permutations 
counter = 1
found = 0
for i in permutations(range(10)):
	# print(i)
	if counter == 1000000:
		print(i)
		found = i
		break
	counter += 1
