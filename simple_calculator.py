print("Hello my friend")
print("You hit the simple calculator")
while True:
    print("Options: ")
    print("Enter 'add' to add two numbers")
    print("Enter 'subtract' to subtract two numbers")
    print("Enter 'multiply' to multiply two numbers")
    print("Enter 'divide' to divide two numbers")
    print("Enter 'quit' to quit two numbers")
    user_input=input(": ")
import math
    if user_input=="quit":
        break
    elif user_input=="add":
        num1=float(input("Enter number: "))
        num2=float(input("Enter another number: "))
        result=str(num1+num2) 
        print(num1,"+",num2,"=",result,sep="")
        print("The aswer is " +result)
    elif user_input=="subtract":
        num1=float(input("Enter number: "))
        num2=float(input("Enter another number: "))
        result=str(num1-num2)
        print(num1,"-",num2,"=",result,sep="")
        print("The aswer is " +result)
    elif user_input=="multiply":
        num1=float(input("Enter number: "))
        num2=float(input("Enter another number: "))
        result=str(num1*num2)
        print(num1,"*",num2,"=",result,sep="")
        print("The aswer is " +result)
    elif user_input=="divide":
        num1=float(input("Enter number: "))
        num2=float(input("Enter another number: "))
        result=str(num1/num2)
        print(num1,"/",num2,"=",result,sep="")
        print("The aswer is " +result)
    else:
        print("Uknown input")
