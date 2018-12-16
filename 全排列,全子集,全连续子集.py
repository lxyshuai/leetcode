# coding=utf-8
class Solution(object):
    def permutation(self, nums):
        """
        全排列
        """

        def process(index, nums):
            # 这里len(nums)或者len(nums)-1都可以
            if index == len(nums) - 1:
                self.result.append(nums[:])
                return
            for current_index in range(index, len(nums)):
                nums[index], nums[current_index] = nums[current_index], nums[index]
                process(index + 1, nums)
                nums[index], nums[current_index] = nums[current_index], nums[index]

        self.result = []
        process(0, nums)
        return self.result


print Solution().permutation([1, 2, 3])


class Solution(object):
    """
    全子集
    """

    def combination(self, nums):
        def process(index, before_array, nums):
            if index == len(nums):
                self.result.append(before_array)
                return
            process(index + 1, before_array + [nums[index]], nums)
            process(index + 1, before_array, nums)

        self.result = []
        process(0, [], nums)
        return self.result


print Solution().combination([1, 2, 3])


class Solution(object):
    """
    全连续子集
    """

    def continuous_combination(self, nums):
        result = []
        for begin in range(len(nums)):
            for end in range(begin, len(nums)):
                result.append(nums[begin:end + 1])
        return result


print Solution().continuous_combination([1, 2, 3])
