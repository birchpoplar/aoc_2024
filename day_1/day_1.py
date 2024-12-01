"""
Advent of Code 2024
Day: 1
Author: Johnnie Walker
"""

# Part 1

import numpy as np

# import data
data = np.loadtxt('input.txt', dtype = int)

list1 = data[:,0]
list2 = data[:,1]

list1.sort()
list2.sort()

diff = 0
diff_total = 0

for val1, val2 in zip(list1, list2):
    diff = abs(val1 - val2)
    print(f"list 1 value {val1}, list 2 value {val2} :: diff {diff}")
    diff_total += diff

print(diff_total)

# Part 2

count = 0
similarity_total = 0

for val1 in list1:
    count = np.sum(list2 == val1)
    print(f"val 1: {val1}, count: {count}")
    similarity_total += val1 * count

print(similarity_total)
