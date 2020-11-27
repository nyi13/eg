firstnumber = input("Enter first number ===> ")
secondnumber = input("Enter second number ===> ")
try:
    firstnumber = int(firstnumber)
    secondnumber = int(secondnumber)
    if secondnumber <= 0:
        print("Secondnumber should be greater than 0")
    else:
        print(firstnumber, "divided by", secondnumber)
        print(firstnumber/secondnumber)
except ValueError:
    print("Please enter number only")    