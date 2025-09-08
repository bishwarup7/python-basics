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


#11--Take the user's name and age as input and print “Hello [name], you are [age] years old”.

usersname = input("Enter user name: ")

userage = int(input("Enter user age: "))

print(f"Hello {usersname},you are {usersage} years old.")


#12--Take the user's height in meters as input and print it in centimeters.

userheight =float(input("Enter your height in meter: "))


height = userheight *100
print(f"Your height in centimeters: {height} ")


#13--Take three numbers as input and print the largest number.

x = int(input("Enter your 1st Number: "))
y = int(input("Enter your 2nd Number: "))
z = int(input("Enter your 3rd Number: "))
if x >= y and x >= z:
    print(f"the larger number is : {x}")
elif y >= x and y >= z:
    print(f"the larger number is : {y}")
else:
    print(f"the larger number is : {z}.")
#using function:
x = int(input("Enter your 1st Number: "))
y = int(input("Enter your 2nd Number: "))
z = int(input("Enter your 3rd Number: "))

print(f"The largest number is: {max(x,y,z)}")


#14--Take three numbers as input and print the smallest number.

x = int(input("Enter your 1st Number: "))
y = int(input("Enter your 2nd Number: "))
z = int(input("Enter your 3rd Number: "))
if x <= y and x <= z:
    print(f"the smallest number is : {x}")
elif y <= x and y <= z:
    print(f"the smallest number is : {y}")
else:
    print(f"the smallest number is : {z}.")
#using function:
x = int(input("Enter your 1st Number: "))
y = int(input("Enter your 2nd Number: "))
z = int(input("Enter your 3rd Number: "))

print(f"The smallest number is: {min(x,y,z)}")


#15--Take two numbers as input and print their remainder.

x = int(input("Enter your 1st Number: "))
y = int(input("Enter your 2nd Number: "))

reminder= x % y
print(f"the reminder when {x} is divided by {y} is: {reminder}")

#16--Take two numbers as input and print their division result as float.
x = int(input("Enter your 1st Number: "))
y = int(input("Enter your 2nd Number: "))

if y != 0:
    z = z/y
    print(f"the division result as float: {z}")

else:
    print("error: division by zero is not allowed.")


#17--Take a number as input and check if it is divisible by 5.

n = int(input("Enter the number: "))

if n % 5 == 0:
    print(f"the number {n} is  divisible by 5")
else:
    print(f"not divisible by 5")

#18--Take a number as input and check if it is divisible by both 3 and 5.

n = int(input("Enter the number: "))

if n % 5 == 0 and n % 3 == 0:
    print(f"the number {n} is  divisible by both 5 & 3")
elif n % 5 == 0:
    print(f"the number {n} is divisible by 5 only")
elif n % 3 == 0:
    print(f"the number {n} is divisible by 3 only")
else:
    print(f"the number {n} is not divisible by 5 & 3")


#19--Take a number as input and print its square.

n = int(input("Enter the number: "))

print(f"the number square is {n**2}")

'''
#20--Take a number as input and print its cube.

n = int(input("Enter the number: "))

print(f"the number cube is {n**3}")





























