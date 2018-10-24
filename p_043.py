"""
Sub-string divisibility
Problem 43 
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""
import itertools

if __name__ == '__main__':
	s_pandigital = list("0123456789")
	ans = 0
	for s in itertools.permutations(s_pandigital, 10):
		if s[0] == "0":
			continue
		if int(s[1]+s[2]+s[3]) % 2 == 0 and int(s[2]+s[3]+s[4]) % 3 == 0 and int(s[3]+s[4]+s[5]) % 5 == 0 and int(s[4]+s[5]+s[6]) % 7 == 0 and int(s[5]+s[6]+s[7]) % 11 == 0 and int(s[6]+s[7]+s[8]) % 13 == 0 and int(s[7]+s[8]+s[9]) % 17 == 0:
			print("s : ", s)
			ans += int("".join(s))
	print(ans)