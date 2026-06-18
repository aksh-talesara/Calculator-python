print("                                    ** Welcome to the calculator program**                          \nThis program can perform basic arithmetic operations like addition, subtraction, multiplication, and division.  ")
try:
    a = int(input("Please enter the first number: "))

    b= int(input("Please enter the second number: "))
    op = input("Enter the operator (+,-,* or /) ")
except:
    print("error invalid")
try:
    match op:
        case "+":
            print("The value of", a, "+", b, "is equals to",a+b)
        case "-":
            print("The value of", a, "-", b, "is equals to",a-b)
        case "*":
            print("The value of", a, "*", b, "is equals to",a*b)
        case "+":
            print("The value of", a, "x", b, "is equals to",a*b)
        case "/":
            print("The value of", a, "+", b, "is equals to",a/b)
        case _:
            print("invalid")
except:
    pass
#this is the latest version2 as of 16 June 2026


