def calculate_bmi(height,weight):
    print("Height =" + str(height))
    print("Weight =" + str(weight))

    bmi= weight / (height * height)
    print("BMI = " + str(bmi))

    if bmi< 18.5:
        print("Underweight")
        
    elif bmi >= 18.5 and bmi < 24.9:
        print("Normal weight")

    else:
        print("Overweight")


calculate_bmi(1.75, 108)
