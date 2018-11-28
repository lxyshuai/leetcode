"""
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation:
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6
Note:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
"""


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, count = {}, {}, {}
        for index, number in enumerate(nums):
            if number not in left:
                left[number] = index
                right[number] = index
                count[number] = 1
            else:
                right[number] = index
                count[number] = count[number] + 1

        ans = len(nums)
        degree = max(count.values())
        for key in count:
            if count[key] == degree:
                ans = min(ans, right[key] - left[key] + 1)

        return ans


import collections


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_index, right_index = {}, {}
        count = collections.Counter([])
        for index, number in enumerate(nums):
            if number not in left_index:
                left_index[number] = index
            right_index[number] = index
            count[number] += 1

        result = len(nums)
        degree = count.most_common()[0][1]
        for number in count:
            if count[number] == degree:
                result = min(result, right_index[number] - left_index[number] + 1)
        return result

if __name__ == '__main__':
    print Solution().findShortestSubArray([1])