def test_calculate_bmi(weight=57, height=1.68):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi = weight / (height * height)
    print("\nBMI = " + str(bmi))

    if bmi < 18.5:
        print("Underweight")
        return -1
    elif bmi < 25:
        print("Normal weight")
        return 0
    else:
        print("Overweight")
        return 1
