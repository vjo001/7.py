name = input("Enter your name: ")
print("Hello", name)

num1 = float(input("Enter num1: "))
num2 = float(input("Enter num2: "))

num3 = num1 * num2
print("Product is: ", num3)

num4 = num1/num2
print("Quotient is: ", num4)

num5 = num1-num2
print("Difference is: ", num5)

num6 = num1+num2
print("Sum is: ", num6)



# menus
print("Calculator")
print("1.Add")
print("1.Subtract")
print("3.Multiply")
print("4.Divide")

# input choice
ch = int(input("Enter Choice(1-4): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")