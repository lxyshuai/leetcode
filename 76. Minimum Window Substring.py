"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
import collections


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not t or not s:
            return ""

        t_counter = collections.Counter(t)
        window_counter = collections.Counter()

        left = 0
        right = 0
        satisfy = 0
        result = float('inf')
        result_left = None
        result_right = None

        while right < len(s):
            current_char = s[right]
            window_counter[current_char] += 1
            if window_counter[current_char] == t_counter[current_char]:
                satisfy += 1
            while left <= right and satisfy == len(t_counter):
                current_char = s[left]
                if right - left + 1 < result:
                    result = right - left + 1
                    result_left = left
                    result_right = right
                window_counter[current_char] -= 1
                if window_counter[current_char] < t_counter[current_char]:
                    satisfy -= 1
                left += 1
            right += 1
        return "" if result == float('inf') else s[result_left: result_right + 1]


if __name__ == '__main__':
    print Solution().minWindow("ADOBECODEBANC", "ABC")
