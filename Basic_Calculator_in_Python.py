#Basic Calculator Program in Python

#Operator Functions

#Addition
def add(x,y):
    return x+y
#Subtraction
def sub(x,y):
    return x-y
#Multiplication
def mul(x,y):
    return x*y
#Division
def div(x,y):
    if(y!=0):
        return x/y
    else:
        print("Mathematical error!")
        print("Run the program again!")
#Power
def pow(x,y):
    return x**y

#User Input
num1=float(input("Enter first number:"))
print("Codes of operators:add-1,sub-2,mul-3,div-4,pow-5")
op=int(input("Enter operator:"))
num2=float(input("Enter second number:"))
ans=0

#Calculation Functions
if(op==1):
    ans=add(num1,num2)
elif(op==2):
    ans=sub(num1,num2)
elif(op==3):
    ans=mul(num1,num2)
elif(op==4):
    ans=div(num1,num2)
elif(op==5):
    ans=pow(num1,num2)
else:
    print("Invalid syntax!Run the program again!")

#Displaying the answer
print("Answer= " , ans)
