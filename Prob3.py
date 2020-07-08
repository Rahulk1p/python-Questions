"""
This problem was recently asked by Twitter:
A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

Example:
Input: "banana"
Output: "anana"

Input: "million"
Output: "illi"


class Solution:
    def longestPalindrome(self, s):


# Fill this in.

# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar
"""

class MySolution:
    def longestPalindrome(self, s):
        # create dictionary of letters and their latest index
        letters = {"final":""}
        # create a tail pointer, it updates whenever we meet a duplicate character
        tail = -1
        # create a head pointer, this one just iterates through every letter
        head = 0
        # result variable, updates whenever it's higher than result
        result = 0

        while head < len(s):
            x = s[head:tail]
            print(x)
            if x[0::] ==  x[::-1]:
                if result < len(x[head:tail]):
                    print(x[head:tail])
                    result = len(x[head:tail])
                    letters["final"]=x

            head += 1
            tail = tail - 1
        print(letters)
        return letters["final"]

s = "tracecarts"
print(str(MySolution().longestPalindrome(s)))


"""
Another Standard Solution

We can think of every palindrome as a mirror image around a central character. For example , "racecar" is a mirror around the center "e". Sometimes, the center character can be doubled and we still have a valid palindrome. For example, in the palindrome "ABBA", the center is the double character "BB". Using this knowledge, we can write a function that finds the longest palindrome by doing the following:

1.) Looping over our string s, treating each character as the "center" character
2.) Checking to see if it creates a longer possible palindrome than we have yet seen.

Note that in each iteration of this loop, we treat the selected character as both a "single-center" odd length palindrome and a "double-center" even length palindrome.

In a string s of n characters, we have 2n-1 possible "center" characters. This is because we have two possibilities for each character, a single-center or a double-center. In other words, for a given index i, our central character could either be the single-center s[i] or the double-center s[i] s[i+1]. This is true for all n indices of s except for the last thus we have 2 * n - 1 possibilities.

This solution has time complexity O(n2). This is because of the following:
1.) In our for loop, we need to go through 2n-1 "center" characters, thus this is O(n).
2.) For each of these "center" characters, checking for the longest palindrome is O(n) time. This palindrome check is linear, and thus it is O(n).
Thus, we have O(n2) time. There is no additional space requirement, so our space complexity is simply O(1).
"""


class Solution:
    def longestPalindrome(self, s):
        if s is '':
            return s
        self.maxLength = 0
        self.start = 0

        for i in range(len(s)):
            # Check for odd length palindromes
            self.expandFromCenter(s, i, i)
            # Check for even length palindromes
            self.expandFromCenter(s, i, i + 1)
        return s[self.start:self.start + self.maxLength]

    # Helper function to expand a substring around a central character or characters.
    def expandFromCenter(self, s, low, high):
        while low > -1 and high < len(s) and s[low] == s[high]:
            low -= 1
            high += 1
        # Check to see if we found a longer palindrome than our current counter.
        # Adjust maxLength and start index to counteract increment from while loop.
        if self.maxLength < high - low - 1:
            self.maxLength = high - low - 1
            self.start = low + 1

        # Test program


s = "tracecars"
print(str(Solution().longestPalindrome(s)))