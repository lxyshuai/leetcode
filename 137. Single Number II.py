"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""


class Solution(object):
    def singleNumber(self, nums):
        def convert(x):
            if x >= 2 ** 31:
                x -= 2 ** 32
            return x

        result = 0
        for i in xrange(32):
            count = 0
            for number in nums:
                count += (number >> i) & 1
            result |= (count % 3) << i
        return convert(result)


class Solution(object):
    def singleNumber(self, nums):
        def convert(x):
            if x >= 2 ** 31:
                x -= 2 ** 32
            return x

        result = 0
        bin_result = [0 for _ in range(32)]
        for number in nums:
            for index in range(32):
                bin_result[index] += (number >> index) & 1
        for index, count in enumerate(bin_result):
            result |= (count % 3) << index
        return convert(result)


if __name__ == '__main__':
    print Solution().singleNumber([-2 - 2, -2, 1, 1, 1, -3, -3, -3, -4])
