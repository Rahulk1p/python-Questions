# python-Questions
<b>1. Add two numbers as a linked list</b>
<br><b>Description:</b> You are given two linked-lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.<br>
      Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)<br>
      Output: 7 -> 0 -> 8<br>
      Explanation: 342 + 465 = 807.<br>
<br><b>=========================================================</b>     
<br><b>2. Longest Substring Without Repeating Characters length</b>
<br><b>Description:</b> Given a string, find the length of the longest substring without repeating characters.
          For Example: Suppose this is the String 'abrkaabcdefghijjxxx'. Longest Palindrome string without repeating character is aabcdefghij and its length is 10.
<br><b>=========================================================</b>
<br><b>3. A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.</b><br>
<b>Description:</b> Example:<br>
Input: "banana"<br>
Output: "anana"<br>

Input: "million"<br>
Output: "illi"<br>

<br><b>=========================================================</b>
<br><b>4 Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. <BR>
         Every opening bracket must have a corresponding closing bracket. We can approximate this using strings.</b><br>
<b>Description:</b> Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
- Open brackets are closed by the same type of brackets.
- Open brackets are closed in the correct order.
- Note that an empty string is also considered valid.

Example:
Input: "((()))"
Output: True

Input: "[()]{}"
Output: True

Input: "({[)]"
Output: False


<br><b>=========================================================</b>
<br><b>5. Find first and last occurence of target element in Sorted Array<BR>
<b>Description:</b>Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x.</BR>
      Return -1 if the target is not found.

Example:
Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
Output: [6,8]

Input: A = [100, 150, 150, 153], target = 150
Output: [1,2]

Input: A = [1,2,3,4,5,6,10], target = 9
Output: [-1, -1]      


<br><b>=========================================================</b>
<br><b>6. Given a list of numbers, where every number shows up twice except for one number, find that one number.</br>

Example:
Input: [4, 3, 2, 4, 1, 3, 2]
Output: 1

<br><b>=======================================================================</b></br>
<b>7. You are given an array of integers in an arbitrary order. Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.</b>
<br><b>Description:</b> We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).<br>
      Example:
             [13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.</br>
             [13, 4, 1] however, should return false, since there is no way to modify just one element to make the array non-decreasing.</br>
<br><b>=========================================================</b>     


<br><b>=======================================================================</b></br>
<b>8. Finding the Floor and Ceiling in Binary Search Tree</b>
<br><b>Description:</b> Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. If either does not exist,then print them as None.<br>
