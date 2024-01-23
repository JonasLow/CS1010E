def compute_bmi():
    height = input("Enter height: ")
    weight = input("Enter weight: ")
    
    try:
        bmi = float(weight) / (float(height) ** 2)
        if bmi <= 0:
            print("Please give positive inputs for height and weight")

        if bmi < 18.5:
            return "Under"
        elif bmi < 25:
            return "Normal"
        elif bmi < 35:
            return "Over"
        else:
            return "Obese"
    
    except ZeroDivisionError:
        print("height cannot be zero")
    
    except (ValueError, TypeError):
        print("Please enter real numbers")
