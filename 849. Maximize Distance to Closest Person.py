"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized.

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation:
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: [1,0,0,0]
Output: 3
Explanation:
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
"""


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        N = len(seats)
        left, right = [N] * N, [N] * N

        for i in range(N):
            if seats[i] == 1:
                left[i] = 0
            elif i > 0:
                left[i] = left[i - 1] + 1

        for i in range(N - 1, -1, -1):
            if seats[i] == 1:
                right[i] = 0
            elif i < N - 1:
                right[i] = right[i + 1] + 1
        return max(min(left[i], right[i]) for i, seat in enumerate(seats) if seats != 1)


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        result = 0

        people = (index for index, seat in enumerate(seats) if seat == 1)
        left_index, right_index = None, next(people)

        for index, seat in enumerate(seats):
            if seat == 1:
                left_index = index
            else:
                while right_index is not None and index > right_index:
                    right_index = next(people, None)

                left_distance = float('inf') if left_index is None else index - left_index
                right_distance = float('inf') if right_index is None else right_index - index
                result = max(result, min(left_distance, right_distance))
        return result


class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        max_zero_group_count = 0
        result = 0
        zero_group_start_index = None
        current_index = 0
        while current_index < len(seats):
            if seats[current_index] == 1:
                zero_group_start_index = current_index
            else:
                if zero_group_start_index is not None:
                    max_zero_group_count = max(max_zero_group_count, current_index - zero_group_start_index)
            current_index += 1
        return max((max_zero_group_count + 1) / 2, seats.index(1), seats[::-1].index(1))


if __name__ == '__main__':
    print Solution().maxDistToClosest([1, 0, 0, 0, 1, 0, 1])
