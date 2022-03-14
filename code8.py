# Sets == Collections, Can have only unique elements, denoted by {}
numbers = {1,2,3,4,5}
print(numbers)
# Below prints true or false
print(5 in numbers)
numbers.add(9)
print(numbers)
numbers.remove(4)
print(numbers)

seta={1,2,3,4,5}
setb={4,5,6,7,8}
# union operation in sets
print(seta | setb)
# Intersion operation (Common Values between two sets )
print(seta & setb)
# difference operator in python
print(seta - setb)
print(setb - seta)

