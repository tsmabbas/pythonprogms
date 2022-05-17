

f = open('demo.txt', 'w') # w stands for write.

print ("hello world")
print("this is a \n multi-line string")
print("this line has a \t tab")
print("this line has a backslash as backslash \\")
print("This is unicode for backslash: \U0001F604")
print("string1"," " "string2", "string3", sep=' ')

# variable
message = "This is a value in variable"
print(message.title())
#ends with  rld returns boolean

print(message.endswith('rld'))
print(message.startswith('rld'))
print(message.split())
print(message.split('o'))
message = "this-is-a-string-separated-by-dashes"
print(message.join('-'))
words = message.split('-')
'*'.join(words)
print(message.replace('-', '*'))

name = "John Smith"

print ("Hello, {0}".format(name))
print(f"Hello, {name}") #syntaxed sugar

from datetime import date
from math import pi
a = 2
b = 3
#expression:format  pi:.2f
print(f"{a} x {pi:.2f} = {a * pi:.2f})    
var1 = "    white space before and after        "
print(var1.strip())

var2 = "****** white space before and after *************"
print(var1.strip(*))

d1 = date(2022, 5, 16)
print(f"{d1:dd-mm-yyyy}")

name = input("Enter your name: ")
print(name.title())
# input taken as string 
age = int(input("Enter the age: "))

f.close()
