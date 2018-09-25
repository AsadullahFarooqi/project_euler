"""
03 : The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n
def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        print(i , " iterator i")
        if n % i:
            # print(i , " is not a division of ", n)
            i += 1
        else:
            n //= i
            # print(n , " is n ", i, " is factor of n")
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors
print("prime factors ",prime_factors(600851475143))
print("largest_prime_factor ", largest_prime_factor(600851475143))
