'''Coding Challenge #5
Return the number of even ints in the given array. Note: the % “mod” operator
computes the remainder, e.g. 5 % 2 is 1.

count_evens([2, 1, 2, 3, 4]) → 3
count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0
'''

def count_evens(l: list) -> int:
    return len([e for e in l if e % 2 == 0])

print(count_evens([2, 1, 2, 3, 4]))
print(count_evens([2, 2, 0]))
print(count_evens([1, 3, 5]))
