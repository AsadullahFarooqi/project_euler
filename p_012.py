import math, time

def tringular_gen():
	counter = 0
	tringular = counter
	while True:		
		counter+=1
		tringular += counter
		yield tringular
		

def divisors(n):
	div_ = 1
	for i in range(1, math.ceil(n**0.5)):
		if n % i == 0:
			div_ += 1
	return div_


for i in tringular_gen():
	# print(i)
	div = divisors(i)
	if  div > 500:
		print(div, " got it " , i)
		break
	# time.sleep(2)