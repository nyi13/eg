x = input("Enter first number ===> ")
y = input("Enter second number ===> ")
operator = input("Enter operator + - * / ===> ")
try:
    x = int(x)
    y = int(y)
    if operator == "+":
        print("result is ===> ", x + y)
    elif operator == "-":
        print("result is ===> ", x - y)
    elif operator == "*":
        print("result is ===> ", x * y)
    elif operator == "/":
        print("result is ===> ", x / y)
    else:
        print("Please type the correct operator")
except ValueError:
    print("Please type the number only")