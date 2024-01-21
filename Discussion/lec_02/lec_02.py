def max_min_difference(a, b, c):
    x = min(a, b, c)
    y = max(a, b, c)

    for number in [a, b, c]:
        if number != x and number != y:
            print((y * 100 + number * 10 + x) - (x * 100 + number * 10 + y))

if __name__ == "__main__":
    a = input("Input first integer: ")
    b = input("Input second integer: ")
    c = input("Input third integer: ")
    max_min_difference(5, 3, 7)
    