principle = float(input("Enter the principle."))
rate = float(input("Enter the rate."))
time = float(input("Enter the time."))
Interest = float(principle*((1+rate/100)**time-1))
print(f"The Compound Interest is ", Interest)
