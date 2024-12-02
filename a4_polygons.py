#Area and Perimeter of various polygons.
import math
print("1. Circle")
print("2. Triangle")
print("3. Rectangle/Square")
print("4. Regular Polygon of 'n' sides.")
type= int(input("Select the type: "))

if type==1:
    rad= float(input("Enter the radius: "))
    peri= 2 * 22/7 * rad
    area= 22/7 * (rad**2)
    print("The circumference of the Circle is ", peri, "units.")
    print("The Area of the Circle is ", area, "sq. units.")

elif type==2:
    a= float(input("Enter the length of the first side: "))
    b= float(input("Enter the length of the second side: "))
    c= float(input("Enter the length of the third side: "))
    peri= a + b + c
    s= (a+b+c)/2
    area= (s*(s-a)*(s-b)*(s-c))**0.5
    print("The perimeter of the Triangle is ", peri, "units.")
    print("The Area of the Triangle is ", area, "sq. units.")

elif type==3:
    a= float(input("Enter the length: "))
    b= float(input("Enter the breadth: "))
    peri= 2 * (a + b)
    area= a*b
    print("The perimeter of the Rectangle is ", peri, "units.")
    print("The Area of the Rectangle is ", area, "sq. units.")

elif type==4:
    n = int(input("Enter the number of sides."))
    a = float(input("Enter the length of the sides."))
    peri = float(n*a)
    area = float(((a**2) * n) / ( 4 * math.tan(3.14 / n)))
    print("The perimeter of the polygon of ", n, "sides is ", peri, "units.")
    print("The Area of the polygon of ",n, "sides is ", area, "sq. units.")

else:
    print("Invalid Choice")