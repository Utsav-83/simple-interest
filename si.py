# Simple Interest Program
principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Rate of Interest (%): "))
time = float(input("Enter the Time (in years): "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest is:", simple_interest)
