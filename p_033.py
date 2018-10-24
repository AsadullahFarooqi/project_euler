if __name__ == '__main__':
	for i in range(10,100):
		for j in range(10, 100):
			if i/j > 1:
				continue
			if i % 10 == 0 and j % 10 == 0:
				print(str(i) + " / " + str(j)+ " = " + str(i)[0] +"/"+ str(i)[0])