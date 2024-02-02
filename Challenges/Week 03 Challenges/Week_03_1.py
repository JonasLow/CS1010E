import sys

def staircase(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return staircase(n - 1) + staircase(n - 2)

def main():
    while True:
        try:
            steps = int(input("Please enter an integer: "))
            if steps <= 0:
                raise ValueError 
            wayz = staircase(steps)
            sys.exit(print(f"There are {wayz} ways to climb a staircase with {steps} steps!"))
        
        except ValueError:
            print("Please provide a real POSITIVE number!")

if __name__ == "__main__":
    main()