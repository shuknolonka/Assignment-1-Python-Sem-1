num = []
sum = 0
for i in range(0,5):
    e = float(input("Enter number "))
    num.append(e)
    sum+=num[i]

mean = sum/5

d_sum = 0 #deviation sum

for i in range(0,5):
    d_sum+= ((num[i]-mean)**2)
    
std_dev = (d_sum/(5-1))**0.5

print("The mean of the given scores is ", mean)
print("The Standard Deviation of the given scores is ", std_dev)