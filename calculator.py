#Building Basic Calculator

num1=int(input("Enter first number: ")) #10
operator=input("Enter operator: ") # @
num2=int(input("Enter second number: ")) #20
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
elif operator=="%":
    print(num1%num2)
else:
    print("Invalid input!")