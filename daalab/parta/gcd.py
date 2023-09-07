import math

# Input two integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))

# Calculate the GCD using the math.gcd function
gcd_result = math.gcd(num1, num2)

# Display the GCD
print(f"The greatest common divisor (GCD) of {num1} and {num2} is {gcd_result}")

'''
Enter the first integer: 12
Enter the second integer: 42
The greatest common divisor (GCD) of 12 and 42 is 6'''