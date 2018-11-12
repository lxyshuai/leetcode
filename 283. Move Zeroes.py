"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        last_zero= 0
        current = 0
        length = len(nums)
        while last_zero != length and current != length:
            if nums[current] != 0:
                nums[last_zero], nums[current] = nums[current], nums[last_zero]
                last_zero += 1
            current += 1
        return nums

if __name__ == '__main__':
    print Solution().moveZeroes([0,1,0,3,12])
