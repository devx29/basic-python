#dictionaries

#how to create and print a dict
user = {
    'Name' : 'Harsh',
    'Age' : 28,
    'Height' : 177.8
}

user2 = dict(Name='Krish', Age=26, Height=150)

print(user['Age'], user2.get('Age'))

#print all keys and values
print(user.keys())
print(user2.values())
print(user.items())
print("Gender" in user)
user.update({"Gender": "Male"})
print('Gender' in user)
user.popitem()
print(user)
del user['Height']
print(user)

#how to not make a copy of a dict ❌
# user3 = user #doing this will impact both dict when updating/clear()/
# print(user3)
# user3.update({'can cook?': False})
# user3.clear()
# print(user, user3)

#how to make a copy of dict in to not impact the original ✅
user4 = user.copy()
user5 = dict(user)
user4.clear()
user5.popitem()
print(user, user4, user5)

#create a nested dict

student1 = {'Name':'Harsh', 'Grade':11, 'GPA':3.7}
student2 = {'Name':'Krish', 'Grade':9, 'GPA':3.9}

students = {'Student-1': student1, 'Student-2': student2}

print(students)
print(students['Student-1']['Name'])
print(students['Student-2']['GPA'])