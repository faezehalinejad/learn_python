operator = input("Choose an operation (+, -, *, /): ")
a = float(input("enter your first number: "))
b = float(input("enter your second number: "))

if operator == "+":
	result = a + b
elif operator == "-":
	result = a - b
elif operator == "*":
	result = a * b
elif operator == "/":
	if b == 0:
		print("Cannot divide by zero.")
		result = None
	else:
		result = a / b
else:
	print("Invalid operation.")
	result = None

if result is not None:
	print(f"Your result is {result}")