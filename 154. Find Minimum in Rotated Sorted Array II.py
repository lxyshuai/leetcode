# coding=utf-8
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""

# coding=utf-8
"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        画出数轴图，明显可以看出如果出现重复，有可能出现nums[left] == nums[right] == nums[middle],此时无法分辨middle是属与第一个递增数列（left）还是
        第二个递增数列（right）,此时可以将left右移一位或者right左移一位避免重复
        """
        if len(nums) == 1:
            return nums[0]
        if nums[0] < nums[-1]:
            return nums[0]
        left = 0
        right = len(nums) - 1
        while right - left != 1:
            middle = left + (right - left) / 2
            # 当nums[left]=nums[right]=nums[middle]且第一个递增区间只有一个数的时候（[10, 1, 10, 10, 10]不通过）, left = left + 1直接进入了第二个递增区间，出错了.
            # if nums[middle] < nums[left]:
            #     right = middle
            # elif nums[middle] > nums[left]:
            #     left = middle
            # else:
            #     left += 1

            # 当nums[left]=nums[right]=nums[middle]且第二个递增区间只有一个数的时候，发现只有[10,10,10,10,10]这种情况，不会出错（真神奇）
            # 此处如果应该用right作为比较标准，因为取中位数时候取得下中位数.可以排除right = right - 1直接进入第一个递增区间的情况。
            # 如果用left就没办法排除这种情况
            if nums[middle] > nums[right]:
                left = middle
            elif nums[middle] < nums[right]:
                right = middle
            else:
                right -= 1

        return nums[right]

