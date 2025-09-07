#what is Loops?

#: a loop is a control structure that helps execute a block of code repeatedly until a specific condition is met.

#In python there are 2 types of loop

# (a)For loop syntax:

# for variable in sequence

# example:

# for i in range(5):
#     print("Hello,Earth!")

#loops in list/string/dictionary:

#list:
germany =['Leipzig','Berlin','Munich']

for i in germany:
    print(i)


#index + value : enumerate

for index,i in enumerate(germany,start=1):
    print(index,i)


#string

s = 'python'

for too in s:
    print(too)

#dictionary

student = {'Name':'Dipto', 'Age' : 20, 'GPA': 3.85}

for x in student:
    print(x, student[x])

#parallel iteration: zip

names =["A","B","C"]
marks = [33,96,89]

for n,m in zip(names,marks):
    print(n,m)
















