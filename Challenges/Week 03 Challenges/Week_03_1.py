def staircase(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return staircase(n -1) + staircase(n -2)

def main():
    steps = 10
    wayz = staircase(steps)
    print(f"There are {wayz} ways to climb a staircase with {steps} steps!")

if __name__ == "__main__":
    main()