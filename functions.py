#funtions

#function definition
def new_function():
    print('New Function!')
#calling function
new_function()

#function can have arguments and those arguments can be initialized with a default value
def add(n1=0, n2=0):
    if (type(n1) is not int or type(n2) is not int):
        return 0
    return n1+n2

total = add(3,5)
print(total)

#function can a non-specified amount of arguments
def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Harsh", 23, 256.67)

#function can also have arguments with key and value pairs
def multiple_pairs(**kwargs):
    print(kwargs)
    print(type(kwargs))

multiple_pairs(Name="Harsh", age=23, height=156.67)

