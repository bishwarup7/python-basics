'''
What is a Variable? 

A variable is like a container or box in which we store data (numbers, text, etc.) so we can use or modify it later in our program.
Think of a variable like a labeled jar:
The label = variable name
The content = stored value
You can change what’s inside the jar anytime.
'''

name ='Dipto' #name->variable & Dipto ->String value
age = 18 #age -> variable & int value
gpa = 4.83 # gpa -> variable & 4.83 ->float value

#how variables works:

x = 10
y = x + 9
print(y)

#+++++++++++++++++++++++++++Data Types++++++++++++++++++++++++++++++++++++++
#Built-in data types :

#(a) Numeric Data Types
#1.Integer
x = 5
y = -2
print(type(x))

#2.Floating Point
pi = 3.1416
gpa =4.83
print(type(pi))

#Complex Number
num = 3 + 5j
print(num.real)   # 3.0  (real part)
print(num.imag)   # 5.0  (imaginary part)
print(type(num))  # <class 'complex'>


#(b) String Data Types

#str(String)

name ="Dipto"
message = "Focus"

print(type(name))

#(c) Boolean Data Type

is_admin = False
is_student = True
print(type(is_student))

#(d) Sequence Data Types

#1.List

#List is ordered
#List is mutable

fruits=["apple","banana","mango"]
print(type(fruits))
print(fruits[1])

#2.tuple

#ordered
#immutable

usa =("San Diego","Ohio","Utha")

print(type(usa))
print(usa[0])

#3.set

#unordered
#unique

numbers = {1,2,3,4,4,4}

print(type(numbers))
print(numbers)

#dictionary

#Stores data in key value pairs
#keys unique

studenti = {
    "name":"Dipto",
    "Age": 20,
    "gpa": 4.83
}

print(type(studenti))
print(studenti["name"])








