def bmi():
    bmivalue = weight/height**2
    print("Hello"+" "+name +" "+ "Your body mass index is")
    print(round(bmivalue,2))



    if bmivalue <18.5:
        print("Body mass index is categorized as underweight range based on your bmi")
    elif bmivalue <25:
        print("Body mass index is categorized as healthy weight range based on your bmi")
    elif bmivalue <30:
        print("Body mass index is categorized as healthy weight range based on your bmi")
    elif bmivalue >30:
        print("Body mass index is categorized as healthy weight range based on your bmi")



name = input("Dear user, please enter your name:")
weight = float(input("please enter your weight:"))
height = float(input("please enter your height in meters:"))

bmi()