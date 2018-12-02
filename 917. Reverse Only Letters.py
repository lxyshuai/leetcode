"""
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.



Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "
"""


class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        left = 0
        right = len(S) - 1
        result = list(S)
        while left < right:
            if all((result[left].isalpha(), result[right].isalpha())):
                result[left], result[right] = result[right], result[left]
                left += 1
                right -= 1
            else:
                if not result[left].isalpha():
                    left += 1
                else:
                    right -= 1
        return "".join(result)
