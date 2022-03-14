# Iter tools: Set of tools required for functional programming, Module
from itertools import count,accumulate,takewhile

for i in count(3):
    print(i)
    """3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
"""

    if i>=20:
        break

numbers = list(accumulate(range(8)))
print(numbers)   #[0,   1,     3,       6,         10,          15,             21,             28]
                 # 0, 0+1, 0+1+2, 0+1+2+3,  0+1+2+3+4, 0+1+2+3+4+5,  0+1+2+3+4+5+6, 0+1+2+3+4+5+6+7

data1 = [1,20,333,344444]
data = list(accumulate(data1))

print(list(takewhile(lambda  x: x<= 10,numbers)))


