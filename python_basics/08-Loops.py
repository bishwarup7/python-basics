'''
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

#(b) while loop syntax:

count = 0
while count<5:
    print(count)
    count+=1
#example:

while True:
    cmd = input("Enter (q to quit): ")
    if cmd == "q":
        break
    print("you typed :",cmd)

#loop control :break, continue,pass

#break

for s in range(10):
    if s == 5:
        break
    print(s)

#continue

for i in range(6):
    if i % 2 == 0:
        continue
    print(i)

#pass

for x in range(3):
    pass
'''

#for-else/while-else:

#Whether a number is prime (for)

n = int(input("Enter a number: "))
if n <= 1:
    print('not prime')
else:
    for i in range(2, int(n **0.5)+1):
        if n % i == 0:
            print('not prime!')
            break
        else:
            print('prime!')
#Whether a number is prime (while)
n = int(input('enter a number: '))
i = 2
while i <= int(n**0.5):
    if n % i == 0:
        print('not prime!')
        break
    i +=1
else:
    print('prime')

#nested loops

#Quality rating 1 to 5 
for i in range(1,6):
    for j in range(1,6):
        print(f"{i*j:2}",end=' ')
    print()

rows = 5
for r in range(1, rows+1):
    print('*'*r)





