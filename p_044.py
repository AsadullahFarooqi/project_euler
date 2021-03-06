"""
Pentagon numbers
Problem 44 
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
"""
import time

def pentagon_nums():
	n = 1
	while True:
		if n >= 20000:
			return 
		yield int((n*((3*n)-1))/2)
		n+=1

if __name__ == '__main__':

	l_of_pentagonals = [i for i in pentagon_nums()]
	
	# print(len(l_of_pentagonals), l_of_pentagonals[-1],"just got out from list")

	for i in l_of_pentagonals:
		for j in l_of_pentagonals:
			if i+j in l_of_pentagonals and i-j in l_of_pentagonals:
				print("ans is : ",i,j, abs(j-i))
				time.sleep(5)
				exit()
				break
			# print(i,j)
		# print(i)


"""
import time

def pentagon_nums():
	n = 1
	while True:
		if n >= 20000:
			return 
		yield int((n*((3*n)-1))/2)
		n+=1
def compute():
	l_of_pentagonals = []
	for i in pentagon_nums():
		l_of_pentagonals.append(i)
	for j in l_of_pentagonals:
		for k in l_of_pentagonals:
			if j+k in l_of_pentagonals and j-k in l_of_pentagonals:
				print("ans is : ",j, k,  abs(k-j))
				return abs(k-j)
				# time.sleep(5)
			print(j, k)

if __name__ == '__main__':

	compute()
"""