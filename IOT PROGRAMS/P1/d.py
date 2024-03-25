# d) Combined Program for Area:
print("Select one of the following:")
print("1. Rectangle\n2. Triangle\n3. Circle")
s = input("Enter your choice: ")

if s == '1':
    x = int(input("Enter length:"))
    y = int(input("Enter breadth:"))
    print("Area =", x * y)
elif s == '2':
    x = int(input("Enter base:"))
    y = int(input("Enter height:"))
    print("Area =", 0.5 * x * y)
elif s == '3':
    x = int(input("Enter radius:"))
    print("Area =", 3.14 * x * x)
else:
    print("Enter a valid choice")