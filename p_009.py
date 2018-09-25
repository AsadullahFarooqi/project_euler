"""
09 : There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
"""

def pythagorean_triplet(n):
    triple_number = n
    for a in range(1, n+1):
        for b in range(a+1, n+1):
            c = n - a - b
            if a*a + b*b == c*c:
                # print(a*a,b*b,c*c)
                return a*b*c

# print(pythagorean_triplet(1000))
