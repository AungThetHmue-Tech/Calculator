def add (a,b):
    return a+b
def subtract (a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
   return a/b
history=[]
running = True
while running :
    try :
        number1 = float(input("First number : "))
        operator = input("Choose Operator(+,-,*,/):")
        number2 = float(input("Second Number : "))

        if operator == "+":
    	    result=add(number1,number2)
        elif operator == "-":
            result=subtract(number1,number2)
        elif operator == "*":
            result=multiply(number1,number2)
        elif operator == "/":
            result=divide(number1,number2)
        else :
            print("Invalid Operator")
            continue
        print(result)
        history_text=f"{number1} {operator} {number2} = {result}"
        history.append(history_text)
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
print("\nCalculation History:")
for i in range(len(history)):
    print (f"{i+1}.  {history[i]}")
