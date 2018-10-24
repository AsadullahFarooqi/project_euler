# numerator = 10000000000000000000
numerator = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# print("numerator length ", len(str(numerator)))

def division(denominator):
	return numerator // denominator



def naive_search(s, m):
	for i in range(1, len(s)-len(m)+1):
		for j in range(1, len(m)):
			if s[i+j-1] != m[j]:
				break
		continue
		return i
	return False


def simple_rep(s,d):
	if s[10:20] == s[20:30]:
		print(d, " : occured : ", s[:i])
		return False
	i = 1
	start = 1
	end = 5
	while i < 1001:

		if s[:i]  == s[i:i+i]:
			# i = i+i
			print(d, " : occured : ", s[:i])
			return False
		else:
			i += 1
	print(d, " : not occured!", s[:50])
	return True

# def a_lil_complex_rep(s, z):
# 	i = 1
# 	while i < 1001:
# 		if s[:i]  == s[i:i+i]:
# 			i = i+i
# 			print(z, " : occured : ", s[:i])
# 			return False
# 		else:
# 			i += 1
# 	print(z, " : not occured!")
	# return True

# def reciprocal_cycle_len(n):
# 	if n == 9:
# 		return n+80
# 	return n

# print(max(range(1, 10), key=reciprocal_cycle_len))

if __name__ == '__main__':
	
	s = "a quick brown fox jumps over a lazzy dog"	
	print(naive_search(s, "over"))
	# for d in range(2, 1001):
	# 	if numerator % d > 2:
	# 		# print(simple_rep(str(division(d)), d), end=", ")
	# 		simple_rep(str(division(d)), d)
		# if numerator % d > 1:
		# 	rec = finding_repetition2(str(division(d)))
		# 	if rec:
		# 		print("gotta : ", d)
		# 		break
