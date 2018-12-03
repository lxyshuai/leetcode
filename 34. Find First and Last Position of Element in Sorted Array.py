# coding=utf-8
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1, -1]

        left = 0
        right = len(nums) - 1
        # 确定左边界
        while left <= right:
            middle = left + (right - left) / 2
            if nums[middle] >= target:
                right = middle - 1
            else:
                left = middle + 1
        if right + 1 == len(nums) or nums[right + 1] != target:
            return result
        result[0] = right + 1

        left = 0
        right = len(nums) - 1
        # 确定右边界
        while left <= right:
            middle = left + (right - left) / 2
            if nums[middle] <= target:
                left = middle + 1
            else:
                right = middle - 1
        result[1] = left - 1
        return result

if __name__ == '__main__':
    print Solution().searchRange([],3)