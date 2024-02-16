#scope

#this is a global scope which can be accessed inside a function
animal = "Lion"
bird = "Flamingo"

def zoo(animal):
    #this is local scope which can be only acessed inside the funtion
    bird = "Peacock"
    fish = "Dolphin"
    print(animal)
    print(fish)
    print(bird)

#passing an argument to a function this way overwritten the initial global variable
zoo("Whale")

#nested functions

#nested functions follow the same rules as above

#initializing global variable students
students = 35

def school(teacher):
    print(teacher)
    principal = "Jane"
    teacher = "Harsh"
    print(teacher)
    #global variable cannot be updated within the function directly
    #students += 1
    global students
    #global variable is accessible within funtion and be updated using the global keyword
    print(students)
    students += 5
    print(students)

    #variables from the parent function can be accessed in the child function. It can be overwritten using arguments
    def coding(teacher):
        print(teacher)
        #using the nonlocal keyword we can use the variable from the parent function and update the same
        nonlocal principal
        principal = "Kelly"
        print(principal)

    coding("Krish")

school("John")

