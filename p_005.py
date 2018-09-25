"""
05 : 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
def multiple_generator(n):
    counter = 1
    while True:
        yield n * counter
        counter += 1
def lcm_finder(n):
    for i in multiple_generator(n):
        list_ = [not(i%j) for j in range(1,n)]
        if all(list_):
            return i
# print(lcm_finder(20))p
