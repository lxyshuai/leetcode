"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.
"""


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        # 一共有三种情况：1.全大写 2.首字母大写 3.全小写
        # 判断逻辑：
        # 1.判断首字母是否是大写
        # 2.首字母不是大写（情况3），大写的数量不能大于0。首字母大写（情况1或者情况3），大写的数量要么是1要么和遍历到字母的数量相同

        is_first_upper = word[0].isupper()
        upper_count = 0
        for index, char in enumerate(word):
            if char.isupper():
                upper_count += 1
            if is_first_upper:
                if not (upper_count == 1 or upper_count == index + 1):
                    return False
            else:
                if upper_count > 0:
                    return False
        return True
