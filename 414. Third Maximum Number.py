import sys


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1 = -sys.maxint
        max2 = -sys.maxint
        max3 = -sys.maxint
        current = 0
        while current < len(nums):
            if nums[current] in (max1, max2, max3):
                current += 1
                continue
            if nums[current] > max1:
                max3 = max2
                max2 = max1
                max1 = nums[current]
            elif nums[current] > max2:
                max3 = max2
                max2 = nums[current]
            elif nums[current] > max3:
                max3 = nums[current]
            current += 1
        if max3 != -sys.maxint:
            return max3
        else:
            return max1


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        for number in nums:
            if number > max1:
                max3 = max2
                max2 = max1
                max1 = number
            elif max1 > number > max2:
                max3 = max2
                max2 = number
            elif max2 > number > max3:
                max3 = number
        if max3 != float('-inf'):
            return max3
        else:
            return max1


if __name__ == '__main__':
    print Solution().thirdMax([3, 2, 1])
