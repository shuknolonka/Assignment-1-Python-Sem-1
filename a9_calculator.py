print("Select 1 for Addition, 2 for Substraction, 3 for Multiplication, 4 for Division") 
choice = int(input("Enter choice: "))

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if choice==1:
    print(f"{n1} + {n2} = {n1+n2}")
elif choice==2:
    print(f"{n1} - {n2} = {n1-n2}")
elif choice==3:
    print(f"{n1} x {n2} = {n1*n2}")
elif choice==4:
    print(f"{n1} / {n2} = {n1/n2}")
else:
    print("invalid choice")