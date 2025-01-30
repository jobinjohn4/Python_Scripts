number1 = int(input("Write 1st number : "))
number2 = int(input("Wriet 2nd number : "))
operator = input("Write operator : ")
result=0
if (operator == "+"):

    result = number1 + number2

elif (operator == "-"):

    result = number1 - number2

elif (operator == "*"):

    result = number1 * number2

elif (operator == "/"):

    result = number1 / number2

else:

    print ("Wrong input")

print(f"The Result is {result}")
