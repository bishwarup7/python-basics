'''

#string is a string of letters,numbers,words or sentences that are written between double ("") or single ('') quotes.
#example:
name = "Dipto"
msg = "I like py"
print(name)
print(msg)

#multiple string

bio ="""My name is bishwarup.
I wanna be a programmer.
My dream country is canada."""

print(bio)

#string indexing:
z = "python"

print(z[0])
print(z[1])
print(z[-1])
print(z[-2])

#slicing:
r = "python"
print(r[1:4]) #yth(index 1-3)
print(r[:3]) #pyt(start to index 2)
print(r[2:]) #thon   (index 2 to end)
print(r[-4:-1]) #tho (negative lndex )

r = "python"

print(r[::2]) #pto
print(r[::-1]) #nohtyp

# Important Built in methods in python string.

txt = "python"

print(txt.upper())

print(txt.lower())

ok = '     hi,martha      '

print(ok.strip())

pol = "I love Finland"

print(pol.replace("Finland","Canada"))
'''
land ="Red,Blue,yellow"

print(land.split(","))

words =["I","Love","BMW"]

print("".join(words))

word ="I love BMW"

print(word.find("Toyota"))

poko ="canada"

print(poko.count("a"))

#f-strings:

name ="dipto"
age =18
print(f"My name is {name} & Iam {age} years old.")

#.format()

name = "dipto"
age =18
print("My name is {} & I'm {} years old.".format(name,age))

#old % formatting

name ="dipto"
age =19
print('My name is %s & Iam %d years old.'%(name,age))

#practical Example:

sentence = "I love python programming"

print(sentence.strip())
print(sentence.upper())
print(sentence.replace("python","java"))
print(sentence.split())


ger = ["I ","Like","RUSSIA"]

print("_".join(ger))

lang ="java"

version =3.11
print(f"Iam learning {lang} version{version}")









