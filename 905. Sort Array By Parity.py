# coding=utf-8
"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.



Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.


Note:

1 <= A.length <= 5000
0 <= A[i] <= 5000
"""


class Solution1(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_list = list()
        odd_list = list()
        for number in A:
            if number % 2 == 0:
                even_list.append(number)
            else:
                odd_list.append(number)
        even_list.extend(odd_list)
        return even_list


class Solution2(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # 遍历一次数组将所有偶数放前面，用index记录不是偶数数组的下一个数
        index = 0
        for i in range(len(A)):
            if A[i] & 1 == 0:
                A[i], A[index] = A[index], A[i]
                index += 1
        return A


if __name__ == '__main__':
    print Solution1().sortArrayByParity([3, 1, 2, 4])
