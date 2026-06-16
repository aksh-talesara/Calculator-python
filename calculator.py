print("                                    ** Welcome to the calculator program**                          \nThis program can perform basic arithmetic operations like addition, subtraction, multiplication, and division.  ")
a = int(input("Please enter the first number: "))
b= int(input("Please enter the second number: "))
op = input("Enter the operator (+,-,* or /) ")

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

heyyyyyyy


