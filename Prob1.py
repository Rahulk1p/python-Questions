# Question
"""
Add two numbers as a linked list

#You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.


Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
Here is the function signature as a starting point (in Python):

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print result.val,
  result = result.next
# 7 0 8

Why Python? We recommend using Python as a generalist language for interviewing, as it is well-regarded in the tech industry and used across Google/YouTube,
Facebook/Instagram, Netflix, Uber, Dropbox, Pinterest, Spotify, etc., It is easy to learn with readable syntax, and very similar in structure to other popular
languages like Java, C/C++, Javascript, PHP, Ruby, etc. Python is generally faster to read/write though, which makes it ideal for interviews. You can, of
  course, use any language you like!
"""

# SOLUTION
"""
This can be done recursively, keeping track of the carryover value as a parameter.

The algorithm iterates O(max(m,n)) times, so it is linear time.
It can use linear space, as the recursion stack space will iterate O(max(m,n)) times as well.

A fun exercise is to also do the iterative version, which you should try to write! The answer for this as well is included below. 
It is also linear time/space complexity because of the single iteration through each linked list and the construction of the result.
"""
class Node(object):
  def __init__(self, x):
    self.val = x
    self.next = None


class Solution:
  def addTwoNumbers(self, l1, l2):
    return self.addTwoNumbersRecursive(l1, l2, 0)
    # return self.addTwoNumbersIterative(l1, l2)

  def addTwoNumbersRecursive(self, l1, l2, c):
    val = l1.val + l2.val + c
    c = val / 10
    ret = Node(val % 10)

    if l1.next != None or l2.next != None:
      if not l1.next:
        l1.next = Node(0)
      if not l2.next:
        l2.next = Node(0)
      ret.next = self.addTwoNumbersRecursive(l1.next, l2.next, c)
    return ret

  def addTwoNumbersIterative(self, l1, l2):
    a = l1
    b = l2
    c = 0
    ret = current = None

    while a or b:
      val = a.val + b.val + c
      c = val / 10
      if not current:
        ret = current = Node(val % 10)
      else:
        current.next = Node(val % 10)
        current = current.next
      if a.next or b.next:
        if not a.next:
          a.next = Node(0)
        if not b.next:
          b.next = Node(0)
      a = a.next
      b = b.next
    return ret


l1 = Node(2)
l1.next = Node(4)
l1.next.next = Node(3)

l2 = Node(5)
l2.next = Node(6)
l2.next.next = Node(4)

answer = Solution().addTwoNumbers(l1, l2)
while answer:
  print
  answer.val,
  answer = answer.next