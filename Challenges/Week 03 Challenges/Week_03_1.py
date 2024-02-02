def staircase(n):
    if n <= 0:
        raise ValueError
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return staircase(n - 1) + staircase(n - 2)

def main():
    try:
        steps = int(input("Please enter an integer: "))
        wayz = staircase(steps)
        print(f"There are {wayz} ways to climb a staircase with {steps} steps!")
    
    except (ValueError, TypeError):
        print("Please provide a real POSITIVE number!")

if __name__ == "__main__":
    main()