"""
25 : What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""
def fib_finder():
    a, b = 0, 1
    while True:
        yield a
        a, b = b , a+b
def fib_counter(n):
    counter = 0
    for i in fib_finder():
        if len(list(str(i))) >= n:
            return i, ", index is : ", counter
        counter +=1
    return 0

# print(fib_counter(1000))
