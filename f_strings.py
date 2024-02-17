#different ways to print

student = "Harsh"
points = 5

print(student + " has " + str(points) + " points!")

message = "%s has %s points!"%(student, points)
print(message)

message = "{} has {} points!".format(student, points)
print(message)

message = "{1} has {0} points!".format(points, student)
print(message)

message = "{student} has {points} points!".format(points=points, student=student)
print(message)

person = {'student': 'Krish', 'points': 6}
message = "{student} has {points} points!".format(**person)
print(message)

#using f-strings

student = "JOHN"
points = 2

message = f"{student} has {points} points!"
print(message)

message = f"{student.lower()} has {points*2} points!"
print(message)

message = f"{student.capitalize()} has {points*0.75:.2f} points!"
print(message)







