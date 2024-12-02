#to calculate roots of a quadratic equation
print(f"The equation of a line is ax + by + c = 0")
print("Enter the values of a, b and c.")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

print(f"The equation of the line is {a}x + {b}y + {c} = 0")

d = (b**2 - 4*a*c)**0.5

root1= (-b + d) / 2*a
root2= (-b - d) / 2*a

print(f"The roots of the above equation are x = {root1} and x = {root2} .")