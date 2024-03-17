print("SIMPLE CALCULATOR")

print("Which operation you want to perform?")
print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")

#User will select operation he wants to perform

select = int(input("Select Operation (1, 2, 3, or 4).\n"))

#Here user will input 2 numbers he wants to make an operation between

if select in (1, 2, 3, 4):
    input1 = int(input("Enter first number: "))
    input2 = int(input("Enter second number: "))

#Based on selected choice, operation will perform respectively

if select == 1:
    print("Addition: ", (input1+input2))
elif select == 2:
    print("Subtraction: ", (input1-input2))
elif select == 3:
    print("Multiplication: ", (input1*input2))
elif select == 4:
    if input2 == 0:
        print("Error! Can't divide by 0.")
    else:
        print("Division: ", (input1/input2))
else:
    print("Invalid Selection Number.\nType 1 for Addition, 2 for Subtraction, 3 for Multiplication, and 4 for Division.") #In case if user mistakenly or willingly tries to divide input1 by 0, it will generate an error.