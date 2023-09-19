def add(a,b):
    answer = a + b
    print(str(a) + " + " +str (b) + " = " + str(answer))
   
def subtract(a,b):
    answer= a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def multiply(a,b):
    answer = a*b
    print(str(a) + " * " + str(b) + str (answer))

def divide(a,b):
    answer = a/b
    print(str(a) + " / " + str(b) + str(answer))

print("A. Addition")
print("B.Subtraction")
print("C.Multiplication")
print("D.Division")
print("E.Exit")

choice = input("Enter your choice:")

if(choice=="a" or choice=="A"):
    print("Addition")
    a = int(input("First number"))
    b= int(input("Second Number "))

elif(choice=="b" or choice=="B"):
    print("Subtraction")
    a = int(input("First number"))
    b= int(input("Second Number "))   

elif(choice=="c" or choice=="C"):
    print("Multiplication")
    a = int(input("First number"))
    b= int(input("Second Number ")) 

elif(choice=="d" or choice=="D"):
    print("Division")
    a = int(input("First number"))
    b= int(input("Second Number ")) 

elif(choice=="e" or choice=="E"):
    print("Exiting")
    quit()
         