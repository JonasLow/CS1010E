from sys import exit

# Time complexity = O(n)
def fisherman_n():
    net = 3
    sea = [1, 2, -3, 5, -9, -2]
    if net > len(sea):
        exit()
    i = 0
    largest = 0
    while i < len(sea) - net:
        if i == 0:
            largest = sum(sea[i:i + net])
        elif sum(sea[i:i + net]) > largest:
            largest = sum(sea[i:i + net])
        i += 1
    print(largest)

fisherman_n()