# coding=utf-8
"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        用stack,stack中存储的是字符的index
        1.如果字符是'(',直接压入栈
        2.如果字符是')',查看栈顶的元素
            1.如果是'(',弹出栈顶元素,更新最大长度=当前字符index-弹出后栈顶的index
            2.如果是')',压入栈
        """
        max_length = 0
        stack = []
        stack.append(-1)
        for index, char in enumerate(s):
            if char == '(':
                stack.append(index)
            elif char == ')':
                if len(stack) > 1 and s[stack[-1]] == '(':
                    stack.pop()
                    max_length = max(max_length, index - stack[-1])
                else:
                    stack.append(index)
        return max_length
