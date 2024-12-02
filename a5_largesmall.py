numbers = input("Enter three numbers separated by commas: ")

numlist = [int(i) for i in numbers.split(",")]


l = max(numlist)
s = min(numlist)

# Print the results
print("The largest number is:", l)
print("The smallest number is:", s)

