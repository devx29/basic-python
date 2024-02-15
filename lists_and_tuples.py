#experimenting with lists and tuples

colors = ['red', 'green', 'blue']
print(colors)

data = ['Harsh', 29, True, 4.20]

# print("green" in colors)

# print(colors[1:2])
# print(colors.index('blue'))

# print(colors[-1])
# print(colors[0:2])

# print(len(data))

colors.append('white')
# print(colors)

colors += ['black']
# print(colors)

colors.extend(['yellow','pink'])

colors += data
print(colors)

colors.insert(0, 'brown')
# print(colors)

colors[2:2] = ['orange', 'violet']
# print(colors)

colors.remove('pink')
# print(colors)

# print(colors.pop())
# print(colors)

del colors[-4:]
print(colors)

# del data
# data.clear()
# print(data)

# colors[1:2] = ['Grey']
# colors.sort()
# print(colors)

# colors.sort(key=str.lower)
# print(colors)

nums = [23, 4, 7, 12, 57]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)
# print(sorted(nums, reverse=True))

# numscopy = nums.copy()
# mynums = list(nums)
# mycopy = nums[:]

#Tuples

first_tuple = tuple(('Harsh', 29, False))

second_tuple = (3, 21, 54, 12, 34, 29)

print(first_tuple)
# print(type(first_tuple))

newlist = list(first_tuple)
newlist.append(56.54)
newlist += list(second_tuple)
newtuple = tuple(newlist)
print(newtuple)

(one, *two, three) = newtuple
print(one)
print(two)
print(three)

print(newtuple.count(29))