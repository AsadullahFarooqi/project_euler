"""
29 : Consider all integer combinations of ab for 2 ≤ a ≤ 5 and 2 ≤ b ≤ 5:
22=4, 23=8, 24=16, 25=32
32=9, 33=27, 34=81, 35=243
42=16, 43=64, 44=256, 45=1024
52=25, 53=125, 54=625, 55=3125
If they are then placed in numerical order, with any repeats removed, we get the following sequence of 15 distinct terms:
4, 8, 9, 16, 25, 27, 32, 64, 81, 125, 243, 256, 625, 1024, 3125
How many distinct terms are in the sequence generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
"""
def power_generator(start_, end_):
    for a in range(start_, end_+1):
        for b in range(start_, end_+1):
            yield a**b

def finding_sequence_in_numbers(start_, end_):
	set_of_combinations = []
    for i in power_generator(start_, end_):
        print(i)
        set_of_combinations.append(i)

    return len(set(set_of_combinations))

# print(finding_sequence_in_numbers(2,100))