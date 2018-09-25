
"""
07 : 10001st prime number
"""
def prime_numbers():
    i = 2
    while True:
        j = 2
        while(j <= (i/j)):
            if not(i%j): break
            j = j + 1
        if (j > i/j) :
            yield i
        i = i + 1
def specific_term_prime(n):
    counter = 1
    for i in prime_numbers():
        if counter == n:
            return i
        counter +=1
# print(specific_term_prime(10001))
