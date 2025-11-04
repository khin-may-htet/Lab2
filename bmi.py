

def calculate_bmi(height, weight):
    bmi = weight / (height * height)

    if bmi < 18.5:
        print ("Underweight")
        return -1    
    elif 18.5 <= bmi < 24.9:
        print("Normal weight")
        return 0
    else:
        print("Overweight")
        return 1

    return bmi

def main():
    height = float(input("Enter height"))
    weight = float(input("Enter weight"))
    bmi = calculate_bmi(height, weight)
    print("BMI = ", str(round(bmi,2)))

if __name__ == "__main__":
    main()
    



