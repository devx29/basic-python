#sets

#creating a set
set1 = {1,3,5,7,9}
set2 = set((2,4,6,8,0))

print(set1, set2)
print(type(set1), type(set2))

#sets dont allow duplicates, initial value will be maintained (True is 1, False is 0)
set1.add(True)
set2.add(False)
print(set1,set2)

#cannot refer an index position in a set, can only check if value exists in a set
print(2 in set1)
print(2 in set2)

#update a set: add new values, add values from another set and merge 2 sets
set1.add(11)
set2.add(10)
# set2.update(set1)
# set3 = set1.union(set2)
# print(set2)
# print(set3)

#remove duplicates / merge unique values
set1.add(0)
set2.add(1)
print(set1)
print(set2)
set1.symmetric_difference_update(set2)
print(set1)

#find common values
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
s3 = s2.intersection(s1)
print(s3)