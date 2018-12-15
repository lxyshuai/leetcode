# coding=utf-8
"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.
Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
"""
# https://leetcode.windliang.cc/leetCode-30-Substring-with-Concatenation-of-All-Words.html
import collections


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s is None or not words:
            return []
        result = []
        # 单词数组的计数器
        word_frequency = collections.Counter(words)
        # 单词数组的数量
        word_count = len(words)
        # 单词的长度
        word_length = len(words[0])
        # 最后一个子串的开始index
        end_index = len(s) - word_count * word_length

        for index in range(0, end_index + 1):
            # 子串内单词的计数器
            has_word_frequency = collections.Counter()

            # 子串包含的单词的数量
            count = 0
            while count < word_count:
                # 截出一个单词
                word = s[index + count * word_length: index + (count + 1) * word_length]
                if word in word_frequency:
                    if has_word_frequency[word] < word_frequency[word]:
                        has_word_frequency[word] += 1
                    else:
                        break
                else:
                    break
                count += 1
            if count == word_count:
                result.append(index)
        return result
