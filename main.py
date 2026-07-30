def add (a,b):
    return a+b
def substract (a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
   return a/b

number1 = float(input("First number : "))
operator = input("Choose Operator(+,-,*,/) : ")
number2 = float(input("Second Number : "))

if operator == "+":
    print(add(number1,number2))
elif operator == "-":
    print(substract(number1,number2))
elif operator == "*":
    print(multiply(number1,number2))
elif operator == "/":
    print(divide(number1,number2))
else :
    print("Invalid Operator")

