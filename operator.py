x = int(input("Enter first number ===> "))
y = int(input("Enter second number ===> "))
z = input("Enter operator + - * / ===> ")
try:
    if operator == "+":
        result = x + y
        print("result is ===> ", result)
    elif operator == "-":
        result = x - y
        print("result is ===> ", result)
    elif operator == "*":
        result = x * y
        print("result is ===> ", result)
    elif operator == "/":
        result = x / y
        print("result is ===> ", result)
    else:
        print("Please type the correct operator")
except ValueError:
    print("Please type the number only")