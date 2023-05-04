def calculate_bmi (height, weight) :
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    #Add code here to calculate BMI
    bmi = weight/(height * height)
    #Add code here to display calculated BMI
    print("BMI = " + str(round(bmi,2)))
    bmi = weight / (height * height)
    if bmi < 18.5:
        print("You are underweight")
        return -1
    elif bmi >= 18.5 and bmi <= 25.0:
        print("You have a normal weight")
        return 0
    else:
        print("You are overweight")
        return 1
calculate_bmi(weight=57, height=1.73)


