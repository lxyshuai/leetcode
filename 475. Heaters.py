# coding=utf-8
"""
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.
Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.
Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.
"""


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        """
        求最小的半径，必须使每个house都被cover到。而每个house应该由它左边或者右边的heater cover到，所以我们需要在heater中找到每一个house的最后一个小于house的heater的下标和第一个不小于house的heater的下标(binary sort)
        """
        min_radius = 0
        heaters.sort()
        for house in houses:
            left = 0
            right = len(heaters) - 1
            while left <= right:
                middle = left + (right - left) / 2
                if heaters[middle] < house:
                    left = middle + 1
                elif heaters[middle] >= house:
                    right = middle - 1
            left_distance = float('inf') if right == -1 else house - heaters[right]
            right_distance = float('inf') if right == len(heaters) - 1 else heaters[right + 1] - house
            min_radius = max(min_radius, min(left_distance, right_distance))
        return min_radius
