"""
p 36: Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
"""
def palindrome_generator():
    l_of_palindroms = []

    for i in range(1, 1000000):
        if str(i) == str(i)[::-1]:
            binary = str(bin(i))[2:]
            if binary == binary[::-1]:
                # print(i, " : ", binary)
                l_of_palindroms.append(i)

    return sum(l_of_palindroms)

print(palindrome_generator())