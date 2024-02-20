#lambda

squared = lambda num : num * num
print(squared(2))

sum = lambda a,b : a * b
print(sum(10,12))

#higher-order-function

def funcBuilder(x):
    return lambda num: num - x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(5))
print(addTwenty(2))

numbers = [1,2,3,4,5,6,7,8,9,10]

squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))

odd_nums = filter(lambda num: num % 2 != 0, numbers)
print(list(odd_nums))

from functools import reduce

total = reduce(lambda acc, curr: acc - curr, numbers)
print(total)

names = ['Harsh', 'Krish', 'John', 'Jane']
chars = reduce(lambda acc, char: acc + len(char), names, 0)
print(chars)

