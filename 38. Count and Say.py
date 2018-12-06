# coding=utf-8
"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.



Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return None
        if n == 1:
            return '1'
        result = '1'
        for _ in range(n - 1):
            temp = ''
            index = 1
            count = 1
            while index < len(result):
                if result[index] != result[index - 1]:
                    temp += str(count) + result[index - 1]
                    count = 1
                else:
                    count += 1
                index += 1
            # 结尾单独处理
            temp += str(count) + result[index - 1]
            result = temp
        return result


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        """
        双指针的做法
        第一个指针指向当前联系序列的第一个数，第二个指针往后遍历，知道遇到一个不等于的数
        """
        if n == 0:
            return
        if n == 1:
            return '1'

        result = '1'
        for _ in range(n - 1):
            temp = ''
            first = 0
            second = 0
            while second < len(result):
                if result[second] == result[first]:
                    second += 1
                else:
                    temp += str(second - first) + result[first]
                    first = second
            temp += str(second - first) + result[first]
            result = temp
        return result
