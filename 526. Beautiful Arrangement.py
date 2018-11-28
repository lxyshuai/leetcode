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

if __name__ == '__main__':
    print Solution().countArrangement(10)