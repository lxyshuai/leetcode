# coding=utf-8
"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""


# 1 Brute Force
class Solution1(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            for index in range(len(nums)):
                nums[index], nums[-1] = nums[-1], nums[index]


# 2 Using Extra Array
class Solution2(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        temp = list()
        for index in range(len(nums) - k, len(nums)):
            temp.append(nums[index])
        for index in range(0, len(nums) - k):
            temp.append(nums[index])
        for index in range(len(nums)):
            nums[index] = temp[index]


# 3 Using Cyclic Replacements
class Solution3(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # 计算每个位置的位移
        k = k % len(nums)
        count = 0
        start_index = 0
        while count != len(nums):
            current_index = start_index
            current_number = nums[start_index]
            next_index = (current_index + k) % len(nums)
            next_number = nums[(current_index + k) % len(nums)]
            is_first = True
            while current_index != start_index or is_first == True:
                nums[next_index] = current_number
                current_index = next_index
                current_number = next_number
                next_index = (current_index + k) % len(nums)
                next_number = nums[(current_index + k) % len(nums)]
                is_first = False
                count += 1
            start_index += 1
        return nums


# 4 Using Reverse
class Solution4(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, start, end):
        while (start < end):
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    print Solution3().rotate([1, 2, 3, 4, 5, 6], 2)
