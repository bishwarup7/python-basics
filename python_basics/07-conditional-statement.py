
#conditional statement: conditional statement is a programming concept where different code is run based on whether a condition is true or false.

#python have 3 conditional statements:

#(1) if--->if condition is true then run.

#(2) elif ---> if perivous condition false,then test new condition.

#(3) else ---> if there is no condition true ,then this block run.

#if statement example:

age = 19

if age>=18:
    print("you are an adult now.")


#if-else statement example:

num = 5

if num % 2 == 0:
    print("Even Number.")
else:
    print("Odd Number.")

#if-elif-else statement example:

age = 25

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("child")


#Nested if statements example:

age = 17

student = True

if age >= 18:
    if student:
        print("can go to university.")
    else:
        print("stay in school.")
else:
    print("Too young.")

#short-hand if/Ternary operator

#if:

x = 10
if x > 5 : print("x is greater than 5.")

#if-else:

x = 5
print("positive") if x>0 else print("Negative")

#Logical operator in conditions:

#and

age = 15

has_id = True

if age >= 18 and has_id:
    print("Allowed to enter")

#or

age = 15

parent_permission = True

if age >= 18 or parent_permission:
    print("Allowed to enter")

#not

logged_in = False

if not logged_in:
    print("Please log in first")

#Membership & Identity operators with conditions:

#Membership(in, notin)

netherland =[" Amsterdam", "Rotterdam", "The Hague", "Utrecht"]

if "Utrecht" in netherland:
    print("Utrecht is a city of Netherland.")

#Identity(is, isnot):

x = None

if x is None:
    print('No value assigned')

#practical Examples:

#(1)Grade System:

marks = 85

if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
elif marks >= 70:
    print("A-")
elif marks >= 60:
    print("B")
elif marks >= 50:
    print("C")
elif marks >= 33:
    print("D")
else:
    print("You are failed.")

#(2)Simple Login system:

username = "admin"
password = "456123"

if username =="admin" and password =="456123":
    print("Login successful")

else:
    print("Invalid Credentials")


























