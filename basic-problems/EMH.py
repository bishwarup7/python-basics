'''
#pros-01: sum of Two Numbers

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

sum = a+b
print(f'sum of two number is {sum} ')
'''
'''
#pros-02: simple calculator

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print("sum=", a+b)
print("sub=", a-b)
print("mul=", a*b)
print("dic=", a/b)

'''
'''
#pros-03: Multiplication Table

n = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{n} x {i} = {n * i}")
'''
'''
#pros-04: Sum of N natural numbers

n = int(input("Enter a number: "))
total=0
for x in range(1,n+1):
    total += x
print(total)
'''
'''
#pros-05: count vowels in string

txt = input("Enter a text: ")

vowels="aeiouAEIOU"
count = 0
for x in txt:
    if x in vowels:
        count += 1
print(count)
'''
'''
#pros-06: Reverse a string

txt = input("Enter a text: ")

revs=txt[::-1]
print(revs)

#or
txt = input("Enter a text: ")
res = ""
for ch in txt:
    res = ch + res
print(res)
'''






