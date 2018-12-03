"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = float('inf')

        import collections
        counter = collections.Counter()
        left_index = {}
        for index, char in enumerate(s):
            if char not in left_index:
                left_index[char] = index
            counter[char] += 1
        for char, count in counter.items():
            if count == 1:
                result = min(result, left_index[char])
        return result


if __name__ == '__main__':
    print Solution().firstUniqChar('leetcode')
