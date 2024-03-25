# b) Arithmetic Operations:
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
ch = input("Enter operation (+, -, *, /): ")
result = 0

if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("Input character is not recognized!")

print(num1, ch, num2, ":", result)