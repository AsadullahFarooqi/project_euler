"""
p 48 : Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
"""

def self_pows(n):
	total = 0
	for i in range(1,n+1):
		total += i**i

	return str(total)

if __name__ == "__main__":
	print(self_pows(1000)[-10:])

9110846700