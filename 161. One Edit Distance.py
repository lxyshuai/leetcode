# coding=utf-8
"""
Given two strings S and T, determine if they are both one edit distance apart.
"""


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        分为三种情况：
        1.长度相同，只能有一个地方不相同
        2.长度相差大于1，不可能
        3.长度相差1，找到第一个不相同的位置，较长的排除不同的的位置的后面要和较短的包括不同的位置后面相同
        :param s:
        :param t:
        :return:
        """
        if len(s) < len(t):
            s, t = t, s
        length_diff = len(s) - len(t)
        if length_diff == 0:
            count = 0
            for index in range(len(s)):
                if s[index] != t[index]:
                    count += 1
            return count <= 1
        elif length_diff == 1:
            for index in range(len(t)):
                if s[index] != t[index]:
                    return s[:index] + s[index + 1:] == t
                else:
                    return True
        else:
            return False


if __name__ == '__main__':
    print Solution().isOneEditDistance('aa', 'aab')
