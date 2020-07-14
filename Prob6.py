"""
Given a list of numbers, where every number shows up twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1
"""

# Performance is high with with constant space o(1)
def singleNumber_way1(nums):
    unique = 0
    for n in nums:
        unique ^= n
        print(unique)
    return unique

# o(n) space
def singleNumber_way2(nums):
    occurance = {}
    for n in nums:
        occurance[n] = occurance.get(n, 0) + 1

    for key, value in occurance.items():
        if value == 1:
            return key
print (singleNumber_way1([4, 3, 2, 4, 1, 3, 2]))
print (singleNumber_way2([4, 3, 2, 4, 1, 3, 2]))
# 1