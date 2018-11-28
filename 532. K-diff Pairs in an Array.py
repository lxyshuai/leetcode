"""
Given an array of integers and an integer k, you need to find the number of unique k-diff pairs in the array. Here a k-diff pair is defined as an integer pair (i, j), where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
"""


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0 or len(nums) == 0:
            return 0
        count = 0
        count_dict = {}
        for number in nums:
            count_dict[number] = count_dict.get(number, 0) + 1
        for key in count_dict:
            if k != 0:
                if key + k in count_dict:
                    count += 1
            else:
                if count_dict[key] >= 2:
                    count += 1
        return count


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0 or len(nums) == 0:
            return 0
        count = 0
        import collections
        counter = collections.Counter()
        for number in nums:
            counter[number] += 1
        for number in counter.keys():
            if k == 0:
                if counter[number] >= 2:
                    count += 1
            else:
                if counter[number + k] > 0:
                    count += 1
        return count


if __name__ == '__main__':
    print Solution().findPairs([1, 2, 3, 4, 5], - 1)
