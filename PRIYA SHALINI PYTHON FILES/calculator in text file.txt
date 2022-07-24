def add(x,y,a,b):
    return x+y+a+b

def multiple(x,y,a,b):
    return x*y*a*b

print("Select operation.")
print("1.Add")
print("2.Multiple")

while True:
    choice = input("Enter choice(1/2): ")
    
    if choice in ('1', '2'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        num3 = float(input("Enter third number: "))
        num4 = float(input("Enter fourth number: "))
        if (num1 % 2 and num2 % 2 and num3 % 2 and num4 % 2) == 0:
            if choice == '1':
                print(num1, "+", num2, "+" ,num3, "+",num4, "=", add(num1, num2, num3, num4))
            elif choice == '2':
                print(num1, "*", num2, "*" ,num3, "*",num4, "=", multiple(num1, num2, num3, num4))
        else:
            print("in given 4 numbers one number is also not even ")
    else:
        print("Invalid Input")
            
    
