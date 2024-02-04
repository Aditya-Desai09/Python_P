import random 

print("\n\n****************** Random Password Generator ******************\n")

num="0123456789"
letter="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
sp_c="-~!@#$%^&*"

c=num+letter+sp_c

def generate(pass_length):
    temp = random.sample(c,pass_length)
    password = "".join(temp)

    print("\n\nPassword:",password,"\n\n")


choice="y"
while choice=="y":
    try:
        pass_length=int(input("\nEnter Desired Password Length :\n"))
        generate(pass_length)
        choice=input("Do you want to generate another password? (y/n): ").lower()
        if choice!='y':
            print("\nGoodbye!\n")
            break
    except:
        print("Please Enter integer value for length")
        