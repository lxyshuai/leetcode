"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        def reverse(string_list, start, end):
            while start < end:
                string_list[start], string_list[end] = string_list[end], string_list[start]
                start += 1
                end -= 1

        result = list(s)
        time = len(result) / (2 * k)
        left = len(result) % (2 * k)
        for index in range(time):
            reverse(result, index * 2 * k, index * 2 * k + k - 1)
        if left < k:
            reverse(result, time * 2 * k, time * 2 * k + left - 1)
        elif left >= k:
            reverse(result, time * 2 * k, time * 2 * k + k - 1)
        return ''.join(result)



if __name__ == '__main__':
    print Solution().reverseStr("hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl", 39)
