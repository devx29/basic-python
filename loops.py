#loops

#while loop: it is important to put the increment statement based on the goal of the while loop. continue and break statements can be used as well
number = 1
while number <= 10:
    number += 1
    if number == 3:
        continue
    print(number)
else:
    print('number is now equal to', number)

#for loop:
states = ['New York', 'Massachusetts', 'Mississippi', "Ohio", "Michigan", "Florida"]

# for x in states:
#     print(x)

for x in states:
    if x == "Ohio":
        break
    print(x)

for x in states:
    if x == "Ohio":
        continue
    print(x)

# for x in range(5):
#     print(x)

# for x in range(2,7):
#     print(x)
    
# for x in range(2, 100, 2):
#     print(x)
# else:
#     print("Here's all even numbers between 0 and 100")
    
#nested loops
    
names = ['Harsh', 'Krish', 'John']
actions = ['eats', 'sleeps', 'codes']

# for name in names:
#     for action in actions:
#         print(name + " " + action)

for action in actions:
    for name in names:
        print(name + " " + action)