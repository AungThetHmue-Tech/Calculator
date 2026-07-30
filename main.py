def add (a,b):
    return a+b
def subtract (a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
   return a/b

running = True
while running :
    try :
        number1 = float(input("First number : "))
        operator = input("Choose Operator(+,-,*,/):")
        number2 = float(input("Second Number : "))

        if operator == "+":
    	    print(add(number1,number2))
        elif operator == "-":
            print(subtract(number1,number2))
        elif operator == "*":
            print(multiply(number1,number2))
        elif operator == "/":
            print(divide(number1,number2))
        else :
            print("Invalid Operator")
            continue
    except ValueError :
        print ("Enter Numbers Only")
        continue
    except ZeroDivisionError :
        print("Can't be divided by Zero")
        continue

    again = input("Calculate Again (Yes or No) :")
    if again.lower() == "yes" :
        running = True
    else :
        running = False
print("Good Bye")

