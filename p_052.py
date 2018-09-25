"""
52 : Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
def permuted_multiplies(multiplies):
    ans_founded = False
    number = 10

    while not ans_founded:
        # print(number, " got here")
        if len(str(multiplies*number)) > len(str(number)):
            number +=1
            pass
        else:
            for i in [z * number for z in range(2, multiplies+1)]:
                temp = all([j in str(i) for j in str(number)]) and all([j in str(number) for j in str(i)])
                if temp:
                    temp_result.append(temp)
                else:
                    temp_result = []
                    break
            if all(temp_result) and len(temp_result) == multiplies -1:
                print(number, " number, 2x:",2*number, ", 3x:",3*number, ", 4x:",4*number, ", 5x:",5*number, ", 6x:",6*number)
                return number
            number +=1

# print(permuted_multiplies(6))
