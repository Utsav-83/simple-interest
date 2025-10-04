# Simple Interest Program
principal = float(input("Enter the Principal amount: "))
rate = float(input("Enter the Rate of Interest (%): "))
time = float(input("Enter the Time (in years): "))

simple_interest = (principal * rate * time) / 100
compound_interest = principal * (1 + rate/100) ** time - principal

print("Simple Interest is:", simple_interest)
print("Compound Interest is:", compound_interest)

