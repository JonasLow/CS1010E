import sys

def main():
    check_command_line()
    fisherman_n()

def check_command_line():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)

    if len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)

# Time complexity = O(n)
def fisherman_n():
    net = 10000
    sea = [1] * 100000
    if net > len(sea):
        sys.exit(1)
    i = 0
    largest = 0
    while i < len(sea) - net:
        if i == 0:
            largest = sum(sea[i:i + net])

        elif sum(sea[i:i + net]) > largest:
            largest = sum(sea[i:i + net])
        i += 1
    print(largest)

if __name__ == "__main__":
    main()