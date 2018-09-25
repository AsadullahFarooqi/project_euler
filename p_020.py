"""
20 : Find the sum of the digits in the number 100!
"""
def factorial_(n):
    i = n
    result = i
    while i > 1:
        result = result * (i - 1)
        i -=1

    return result
def factorial_digit_sum(number):
    factorial = factorial_(number)
    summation = 0
    for digit in str(factorial):
        summation += int(digit)

    return summation

# print(factorial_digit_sum(100))
