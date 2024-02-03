print("\n************** SIMPLE CALCULATOR **************\n")

def add(a,b):
    print("\nAddition :",a+b)

def sub(a,b):
    print("\nSubtraction :",a-b)

def mult(a,b):
    print("\nMultiplication :",a*b)

def div(a,b):
    if b!= 0:
        print("\nDivision :",a/b)
    else:
        return "Cannot divide by zero"

def calc():
    while True:
        print("Select operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division\n")
    
        choice=int(input("Enter Choice (1,2,3,4) :\n"))

        if choice in [1,2,3,4]:
            a1 = float(input("Enter first number: "))
            b1 = float(input("Enter second number: "))

            if choice==1:
                add(a1,b1)

            elif choice==2:
                sub(a1,b1)

            elif choice==3:
                mult(a1,b1)

            elif choice==4:
                div(a1,b1)
        else:
            print("Please Enter a valid choice.")

        cont=input("\nDo you want to perform another calculation? (y/n): ").lower()
        if cont!='y':
            print("\nExiting Calculator.Goodbye!\n")
            break

calc()
