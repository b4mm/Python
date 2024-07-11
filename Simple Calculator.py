use_calculator = True
sum = float(input("Enter a Number: "))
operation = input("Choose in operation: +, -, /, *: ")

while use_calculator == True:
    while operation == "+":
        userInput = float(input("Enter a Number: "))
        sum = sum + userInput
        print(sum)
        operation = input("Enter an Operation: ")

    while operation == "-":
        userInput = float(input("Enter a Number: "))
        sum = sum - userInput
        print(sum)
        operation = input("Enter an Operation: ")
    while operation == "/":
        userInput = float(input("Enter a Number: "))
        sum = sum / userInput
        print(sum)
        operation = input("Enter an Operation: ")
    while operation == "*":
        userInput = float(input("Enter a Number: "))
        sum = sum * userInput
        print(sum)
        operation = input("Enter an Operation: ")
