def calculate_bmi(weight, height):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height * height)
    print("\nBMI = " + str(bmi))

    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    else:
        print("Overweight")


calculate_bmi(weight=57, height=1.68)
