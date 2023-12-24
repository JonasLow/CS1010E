def max_and_min(values):
    max = 0
    min = 0
    for i in range(len(values)):
        if i == 0:
            max = values[i]
            min = values[i]
        elif values[i] > max:
            max = values[i]
        elif values[i] < min:
            min = values[i]
    
    return (max, min)
