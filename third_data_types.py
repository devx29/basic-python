import math

# String data
first = "Harsh"
last = "Shah"

print(type(first))

# animal = str("Horse")
animal = 'Horse'
print(type(animal) == str)
print(isinstance(animal, str))

# Concatenation
fullname = first + " " + last
print(fullname)
fullname += "!"
print(fullname)

# Casting number to a string
year = 1995
year = str(year)
month = 'July'
print(type(year))
print(year)

sentence = "I was born in the year " + year + " month " + month + "!"
print(sentence)

# Multiple lines
multiline = '''
Hey, hows it going?                                       

See you tomorrow!    

Bye!
'''
print(multiline)

# Escaping special characters
sentence_2 = 'Hello! I\'m ' + fullname, 'This is how you put a \\'
print(sentence_2)

# String Methods
print(first.lower())
print(first.upper())

print(multiline.title())
print(multiline.replace("tomorrow", "tonight"))
print(multiline)

print(len(multiline))
multiline += "                                        "
multiline = "                  " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Bagel".ljust(16, ".") + "$2".rjust(4))

# string indexes
print(first[0])
print(first[-1])
print(first[1:-1])
print(first[1:])

# return boolean data
print(first.startswith("H"))
print(first.endswith("A"))


# Boolean data type
myvalue = 'True'
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data types

# integer
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float
gpa = 3.28
y = float(3.14)
print(type(gpa))

# complex type
# comp_value = 5+3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(49))
print(math.ceil(gpa))
print(math.floor(gpa))

# Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))
