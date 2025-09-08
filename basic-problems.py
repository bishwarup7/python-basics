'''
#Basics----easy

#01--Take two numbers as input and print their sum.
x = int(input("Enter your 1st Number: "))
y = int(input("Enter your 2nd Number: "))

z = x+y
print(f"The sum of 2 number is :{z}")



#02--Take two numbers as input and print their product.
x = int(input("Enter your 1st Number: "))
y = int(input("Enter your 2nd Number: "))

z = x*y
print(f"The product of 2 number is :{z}")


#03--Take three numbers as input and print their average.

x = int(input("Enter your 1st Number: "))
y = int(input("Enter your 2nd Number: "))
z = int(input("Enter your 2nd Number: "))


s = (x+y+z)/3
print(f"The average of 3 number is :{s}")


#04--Take the user's name as input and print “Hello, [name]”.
usersname =input("Enter username: ")

print(f"Hello,{usersname}!")

#05--Take the user's age as input and print their age after one year.

usersage =int(input("Enter user age : "))

old=usersage + 1
print(f"Userage after one year will be: {old}")

#06--Take two numbers as input and print the larger number.

x = int(input("Enter your 1st Number: "))
y = int(input("Enter your 2nd Number: "))

if x > y:
    print(f"the larger number is : {x}")
elif y > x:
    print(f"the larger number is : {y}")
else:
    print(f"Both numbers are equal.")


#07--Take two numbers as input and print the smaller number.

x = int(input("Enter your 1st Number: "))
y = int(input("Enter your 2nd Number: "))

if x < y:
    print(f"the smaller number is : {x}")
elif y < x:
    print(f"the smaller number is : {y}")
else:
    print(f"Both numbers are equal.")

#08--Take a number as input and check whether it is even or odd.

n =int(input("Enter your name : "))

if n%2 == 0:
    print(f"your number {n} is Even.")
else:
    print(f"your number {n}is Odd.")

#09--Take a number as input and check whether it is positive or negative.

n =int(input("Enter your name : "))

if n >= 0:
    print(f"your number {n} is positive.")
else:
    print(f"your number {n}is negative.")


#10--Swap two variables without using a third variable.

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

a,b == b,a

print(f"After swapping: a={a},b ={b}")
'''