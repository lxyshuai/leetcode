# coding=utf-8
"""
A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.



Example 1:

Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.


Note:

1 <= S.length <= 20000
S only consists of '0' and '1' characters.
"""


class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        """
        思路分析：
        假设经过最优解的翻转使其变成了 s = '0'*i + '1'*j
        其实我们要决定的是在原字符串中选择哪一个位置的’1’，使其作为最优解中的第一个’1’！

        例如对于示例2中的010110，假设我们选择index=1处的’1’作为开头的’1’，那么我们需要将后面所有的’0’全部翻转成’1’，翻转次数取决于后面’0’的个数。

        又假设我们选取index=3处的’1’作为开头的’1’，那么我们需要将前面所有的'1'翻转成0，将后面所有的'0'翻转成'1'，翻转次数取决于前面’1’的个数和后面’0’的个数。

        OK，那我们只要一直记录着当前位置的前面有多少个1，后面有多少个0即可！
        注意：可能存在最后全为0的情况（如示例3），那么我们是选不到某个’1’作为开头的，所以我们先将全部翻转成’0’所花费的次数作为初始默认次数，然后和我们每次计算的结果比较即可。
        """
        after_zero_count = S.count('0')
        before_one_count = 0
        # 可能存在最后全为0的情况（如示例3），那么我们是选不到某个’1’作为开头的，所以我们先将全部翻转成’0’所花费的次数作为初始默认次数，
        result = len(S) - after_zero_count
        for index in range(len(S)):
            if S[index] == '0':
                after_zero_count -= 1
            elif S[index] == '1':
                result = min(result, before_one_count + after_zero_count)
                before_one_count += 1
        return result
