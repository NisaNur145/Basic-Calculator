print("Welcome to Basic Calculator!")
print("Enter 1 for Addition")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
print("Enter 5 for Exponent")

a=int(input("Enter a number: "))
if a in [1,2,3,4,5]:
    b = int(input("Enter the first number: "))
    c = int(input("Enter the second number: "))
    if a==1:
        print("Addition Result: ",b+c)
    elif a==2:
        print("Subtraction Result: ",b-c)
    elif a==3:
        print("Multiplication Result: ",b*c)
    elif a==4 and c==0:
        print("Division by 0 is not possible")
    elif a==4 and c!=0:
        print("Division Result: ",b/c)
    elif a==5:
        print("Exponent Result: ",b**c)
else:
    print("Please enter a valid number")
