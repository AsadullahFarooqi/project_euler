"""
04 : A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
# brute force approache
def list_of_palindromes(start_, end_):
    l = []
    for i in range(start_, end_):
        for j in range(start_, end_):
            if str(i*j) == str(i*j)[::-1]:
                l.append(i*j)
    return l
# start = time.perf_counter()
# print(max(list_of_palindromes(100, 1000)))
# stop =  time.perf_counter()
# print("Time ", stop - start)

# in the short form
#######################################################3
"""print (max(i*j for i in range(100,1000) for j in range(100,1000) if str(i*j) == str(i*j)[::-1]))"""

# efficient and faster approache
#####################################################3
def checking_factors_palindrome(n):
    i = 100
    while i * i <= n:
        if not(n%i):
            if n//i <= 999:
                print(n/i , i)
                return [n/i, i]
        i += 1
    return 0
def palindrome_generator(start_, end_):
    for i in range(end_*end_, 100, -1):
        if str(i) == str(i)[::-1]:
            if checking_factors_palindrome(i):
                return  i
# start = timeit.default_timer()
# print(palindrome_generator(100, 999))
# stop =  timeit.default_timer()
# print("Time ", stop - start)

####################################################
