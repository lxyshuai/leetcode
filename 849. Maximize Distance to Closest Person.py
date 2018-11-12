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
        first = 0
        last = 0
        max_count = 0
        while last != len(seats):
            if seats[last] == 1:
                first = last
                last += 1
            else:
                max_count = max(last - first, max_count)
                last += 1
        return max((max_count + 1) / 2, seats.index(1), seats[::-1].index(1))
