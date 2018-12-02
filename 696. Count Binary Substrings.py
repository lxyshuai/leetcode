# coding=utf-8
"""
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Notice that some of these substrings repeat and are counted the number of times they occur.

Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
Note:

s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
"""


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        首先理解好题意，0和1必须要连续且0和1的数量相同，而且substrings可以重复
        将字符串中连续的0和连续1分组并记录数量，我们可以得到一个类似[a个0,b个1，c个0...]的数组
        任意两个区间之间可以构成符合要求子串的数量是min(group1, group2)
        """
        group = [1]
        for index in range(1, len(s)):
            if s[index] != s[index - 1]:
                group.append(1)
            else:
                group[-1] += 1

        result = 0
        for index in range(0, len(group) - 1):
            result += min(group[index], group[index + 1])
        return result


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        首先理解好题意，0和1必须要连续且0和1的数量相同，而且substrings可以重复
        将字符串中连续的0和连续1分组并记录数量，我们可以得到一个类似[a个0,b个1，c个0...]的数组
        任意两个区间之间可以构成符合要求子串的数量是min(group1, group2)
        优化空间复杂度，不适用数组记录，直接在记录的时候进行比较
        """
        result = 0
        pre = 0
        cur = 1
        for index in range(1, len(s)):
            if s[index] != s[index - 1]:
                result += min(pre, cur)
                pre, cur = cur, 1
            else:
                cur += 1
        # 最后一定要记得最后一轮比较还没进行，此处要加上
        return result + min(pre, cur)
