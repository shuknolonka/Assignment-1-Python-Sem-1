print("Type 1 if the temperature is in Celsius. ")
print("Type 2 if the temperature is in Fahrenheit. ")
choice = int(input("Enter choice: "))
if choice==1:
    temp = float(input("Enter temperature - "))
    tempf = temp*9/5 +32
    print(tempf, "F")

elif choice==2:
    temp = float(input("Enter temperature - "))
    tempc = (temp-32)*5/9
    print(tempc, "C")

else:
    print("invalid choice")