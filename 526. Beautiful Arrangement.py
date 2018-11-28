"""
Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

The number at the ith position is divisible by i.
i is divisible by the number at the ith position.
Now given N, how many beautiful arrangements can you construct?

Example 1:
Input: 2
Output: 2
Explanation:

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
Note:
N is a positive integer and will not exceed 15.
"""


class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.count = 0

        def permute(nums, current_index):
            # basecase
            if current_index == len(nums) - 1:
                index = 0
                while index < len(nums):
                    real_index = index + 1
                    if nums[index] % real_index != 0 and real_index % nums[index] != 0:
                        break
                    index += 1
                if index == len(nums):
                    self.count += 1
            for index in range(current_index, len(nums)):
                nums[index], nums[current_index] = nums[current_index], nums[index]
                permute(nums, current_index + 1)
                nums[index], nums[current_index] = nums[current_index], nums[index]

        nums = [index + 1 for index in range(N)]
        permute(nums, 0)
        return self.count


class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        self.count = 0

        def permute(nums, current_index):
            if current_index == len(nums):
                self.count += 1
            for index in range(current_index, len(nums)):
                nums[index], nums[current_index] = nums[current_index], nums[index]
                real_index = current_index + 1
                if nums[current_index] % real_index == 0 or real_index % nums[current_index] == 0:
                    permute(nums, current_index + 1)
                nums[index], nums[current_index] = nums[current_index], nums[index]

        nums = [index + 1 for index in range(N)]
        permute(nums, 0)
        return self.count


class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        def calculate(position):
            if position > N:
                self.count += 1
            for index in range(1, N + 1):
                if not visited[index] and (position % index == 0 or index % position == 0):
                    visited[index] = True
                    calculate(position + 1)
                    visited[index] = False

        self.count = 0
        visited = [False for _ in range(N + 1)]
        calculate(1)
        return self.count
