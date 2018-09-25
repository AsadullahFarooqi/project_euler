"""
10 : Find the sum of all the primes below two million.
"""
def summation_of_primes(n):
    list_of_primes = []
    i = 2
    while (i < n):
        j = 2
        while(j <= (i/j)):
            if not(i%j): break
            j = j + 1
        if (j > i/j) :
            list_of_primes.append(i)
            # print (i, " is prime")
        i = i + 1
    return sum(list_of_primes)

# print(summation_of_primes(2000000))
