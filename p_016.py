"""
16 : What is the sum of the digits of the number 21000?
"""
def power_digit_sum(number, power):
    summation = 0
    for digit in str(number**power):
        summation += int(digit)

    return summation

# print(power_digit_sum(2, 1000))
