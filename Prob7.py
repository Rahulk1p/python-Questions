"""
You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example:

[13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.

[13, 4, 1] however, should return false, since there is no way to modify just one element to make the array non-decreasing.
"""

# Solution 1
def my_check(lst):
    length = len(lst)
    falseCounter = 0
    for i in range(0,length-2):
        if lst[i] > lst[i+1]:
            falseCounter = falseCounter + 1

    if falseCounter > 1:
            return False
    if falseCounter == 1:
        return True

# Solution 2
def check(lst):
  count = 0
  for i in range(len(lst) - 1):
    if lst[i] > lst[i + 1]:
      if count > 0:
        return False
      if (i - 1 >= 0 and i + 2 < len(lst) and
        lst[i] > lst[i + 2] and
        lst[i + 1] < lst[i - 1]):
        return False
      count += 1
  return True



print(my_check([13, 4, 7]))
# True
print (my_check([5,1,3,2,5]))
# False