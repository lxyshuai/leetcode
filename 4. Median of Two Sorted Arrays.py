# coding=utf-8
"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def find_k_th_smallest(nums1, nums2, k):
            if len(nums1) > len(nums2):
                return find_k_th_smallest(nums2, nums1, k)
            if nums1 == []:
                return nums2[k - 1]
            elif nums2 == []:
                return nums1[k - 1]
            elif k == 1:
                return min(nums1[0], nums2[0])
            else:
                # 不能超过数组长度
                nums1_part = min(k / 2, len(nums1))
                nums2_part = k - nums1_part
                if nums1[nums1_part - 1] == nums2[nums2_part - 1]:
                    return nums1[nums1_part - 1]
                elif nums1[nums1_part - 1] > nums2[nums2_part - 1]:
                    return find_k_th_smallest(nums1[:], nums2[nums2_part:], k - nums2_part)
                elif nums1[nums1_part - 1] < nums2[nums2_part - 1]:
                    return find_k_th_smallest(nums1[nums1_part:], nums2[:], k - nums1_part)

        length_sum = len(nums1) + len(nums2)
        if length_sum % 2 == 0:
            return (find_k_th_smallest(nums1, nums2, length_sum / 2) + find_k_th_smallest(nums1, nums2,
                                                                                          length_sum / 2 + 1)) / 2
        else:
            return find_k_th_smallest(nums1, nums2, length_sum / 2 + 1)


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def find_k_th_smallest(nums1, nums2, k):
            # 我们假设nums1的长度大于nums2，否则调换nums1和nums2，这样可以避免很多特殊情况
            if len(nums2) > len(nums1):
                return find_k_th_smallest(nums2, nums1, k)
            if nums2 == []:
                return nums1[k - 1]
            # 当k=1的时候，下面的比较流程会有问题
            if k == 1:
                return min(nums1[0], nums2[0])
            nums2_part = min(len(nums2), k / 2)
            nums1_part = k - nums2_part
            if nums1[nums1_part - 1] == nums2[nums2_part - 1]:
                return nums1[nums1_part - 1]
            elif nums1[nums1_part - 1] > nums2[nums2_part - 1]:
                return find_k_th_smallest(nums1, nums2[nums2_part:], k - nums2_part)
            else:
                return find_k_th_smallest(nums1[nums1_part:], nums2, k - nums1_part)

        length_sum = len(nums1) + len(nums2)
        if length_sum % 2 == 0:
            return 1.0 * (find_k_th_smallest(nums1, nums2, length_sum / 2) + find_k_th_smallest(nums1, nums2,
                                                                                                length_sum / 2) + 1) / 2
        else:
            return find_k_th_smallest(nums1, nums2, length_sum / 2 + 1)


if __name__ == '__main__':
    print Solution().findMedianSortedArrays([1, 2, 2.5], [3, 5])
