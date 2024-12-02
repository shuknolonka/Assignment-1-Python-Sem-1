print("Enter the range to check whether it is prime or not.")
n1 = int(input("Enter starting range : "))
n2 = int(input("Enter ending range : "))

print("The prime numbers are :")

for num in range(n1, n2+1):
    if num > 1 :
        for i in range (2, (num//2)+1):
            if(num % i) == 0:
                
                break

        else: 
            print(num)

