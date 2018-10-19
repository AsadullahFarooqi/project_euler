# numerator = 10000000000000000000
numerator = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# print("numerator length ", len(str(numerator)))

def division(denominator):
	return numerator // denominator

l_of_ans = []
l_of_non_recurring_len = []

def finding_repetition(s):
	i = 1
	occurance = 0
	occured_on_ith = 0
	occured = ""
	while i < 1001:
		# for i in range(1,len(s)):
		# occurance = s[0]
		# l = len(s[:i])
		# print(l)
		# print(s[:i], " == " ,s[i:i+i])
		# i+=1
		# if s[-40:-20] == s[-20:]:
		# 	return False
		# if occurance > 1:
		# 	print("occured_on_ith : ", occured_on_ith)
		# 	print("occurance : ", occurance)
		# 	print("occured : ", occured)
		# 	return False
		# if i > 499:
		# 	if s[:10] == s[i:10]:
		# 		print("i'm here")
				
		# 		i = i + i
		# 		occurance += 1
		# 		print("occured : ", occured)
		# 		print("occured_on_ith : ", occured_on_ith)
		# 		return False

		if s[:i]  == s[i:i+i]:
			i = i+i
			occured = s[:i]

			print("occured : ", occured)
			print("occured_on_ith : ", occured_on_ith)
			return False
			occured_on_ith = i
			occurance += 1
		else:
			i += 1
	# 	print("ith : ", i)
		
	print(s)

	return True

# finding_repetition(str(division(3)))

for d in range(2, 1001):
	if numerator % d > 1:
		rec = finding_repetition2(str(division(d)))
		if rec:
			print("gotta : ", d)
			break
		else:
			print(rec)
			# l_of_ans.append(str(division(d)))
			# print("1/", d ," = ", division(d))
			# print(d, " : " ,numerator % d)