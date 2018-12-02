"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        def reverse_word(word):
            if len(word) <= 1:
                return word
            return reverse_word(word[len(word) / 2:]) + reverse_word(word[:len(word) / 2])

        words = s.split(' ')
        result = []
        for index in range(len(words)):
            result.append(reverse_word(words[index]))
        return ' '.join(result)
