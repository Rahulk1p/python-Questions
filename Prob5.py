"""
5. Find first and last occurence of target element in Sorted Array
Description:Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x.
Return -1 if the target is not found.

Example: Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9 Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150 Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9 Output: [-1, -1]

"""


class Solution:
    def my_getRange(self, arr, target):
        result = [-1, -1]
        index = 0
        found = False
        for n in arr:
            if n == target:
                if not found:
                    result[0] = index
                if found:
                    a = result[1]
                    if index > a:
                        result[1]= index

            index = index + 1
            if result[0] != -1:
                found = True

        return result

    def getRange(self, arr, target):
        low = 0
        high = len(arr) - 1
        first = self.binarySearchIterative(arr, low, high, target, True)
        last = self.binarySearchIterative(arr, low, high, target, False)
        return [first, last]

    def binarySearch(self, arr, low, high, target, findLowest):
        if (high >= low):
            mid = low + (high - low) / 2
            if findLowest:
                if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                    return mid
                elif target > arr[mid]:
                    return self.binarySearch(arr, mid + 1, high, target, findLowest)
                else:
                    return self.binarySearch(arr, low, mid - 1, target, findLowest)
            else:
                if (mid == len(arr) - 1 or x < arr[mid + 1]) and arr[mid] == x:
                    return mid
                elif target < arr[mid]:
                    return self.binarySearch(arr, low, mid - 1, target, findLowest)
                else:
                    return self.binarySearch(arr, mid + 1, high, target, findLowest)
        return -1

    def binarySearchIterative(self, arr, low, high, target, findLowest):
        while high >= low:
            mid = low + (high - low) / 2
            if findLowest:
                if (mid == 0 or target > arr[mid - 1]) and arr[mid] == target:
                    return mid
                elif target > arr[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if (mid == len(arr) - 1 or x < arr[mid + 1]) and arr[mid] == x:
                    return mid
                elif target < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1

# Fill this in.

# Test program
arr = [100, 150, 150, 153]
x = 150
print(Solution().my_getRange(arr, x))
# [1, 4]
