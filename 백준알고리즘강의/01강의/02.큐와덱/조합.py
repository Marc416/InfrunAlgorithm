import sys
from itertools import permutations
from itertools import combinations

a = []
b = []
itm = [1, 2, 3, 4]
# 조합
for i in list(combinations(itm, 2)):
    a.append(i)
print(a)
# 순열(중복)
for i in list(permutations(itm, 2)):
    b.append(i)
print(b)
