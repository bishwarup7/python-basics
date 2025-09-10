#what is function?

#:A function is a block of code that performs a specific task and can be reused multiple times in a program.

#example:
def ok(name):
    return f'Hello,{name}'
print(ok('dipto'))
print(ok('jonas'))

#parameter : A parameter is a variable that you define in a function header to receive values when the function is called.

#argument : An argument is the actual value you pass to the function when you call it.

def add(a,b):
    return a+b
res =add(5,14)
print(res)

#default argument : a default argument means a function parameter that has a predefined value.

def greet(name = 'guest'):
    return f'hello,{name}'
print(greet('dipto'))

#keyword arguments:

def info (name,age):
    return f'Name: {name}, age: {age}'
print(info(age=20, name ='dipto'))












