from a1_q10_template import invert_number

def reversed_number(low, high):
    acceptable_numbers = []
    for i in range(low, high + 1):
        if i == invert_number(i):
            acceptable_numbers.append(i)
    
    return(len(acceptable_numbers))

print(reversed_number(151, 202))