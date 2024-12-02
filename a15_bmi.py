weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))

bmi = weight / (height * height)

if  bmi < 18.5:
    print("Underweight.")

elif    bmi < 24.9:
    print("Normal Weight.")

elif bmi < 29.9:
    print("Overweight.")

else:
    print("Obesity.")


