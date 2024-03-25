# f) Handle Divide by Zero Exception:
n1 = int(input("Enter first no: "))
n2 = int(input("Enter second no: "))

try:
    div = n1 / n2
    print(div)
except ZeroDivisionError:
    print("Zero division is handled")

print("Out of try-catch block")