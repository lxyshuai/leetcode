# coding=utf-8
# http://www.cnblogs.com/grandyang/p/6854825.html


def binary_search(nums, target):
    left = 0
    right = len(nums)
    while left < right:
        middle = left + (right - left) / 2
        if nums[middle] == target:
            return middle
        elif target > nums[middle]:
            left = middle + 1
        else:
            # 因为结束循环的条件时 left >= right.
            # 如果这里写成right = middle - 1 = left，就会跳过left=right的时候的判断
            right = middle
    return -1


def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = left + (right - left) / 2
        if nums[middle] == target:
            return middle
        elif target > nums[middle]:
            left = middle + 1
        else:
            right = middle - 1
    return -1


# 变种
# 第二类： 查找第一个不小于目标值的数，可变形为查找最后一个小于目标值的数
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = left + (right - left) / 2
        if target > nums[middle]:
            left = middle + 1
        else:
            right = middle - 1
    # right是最后一个小于目标值的数的下标， right+1是第一个不小于目标值的数的下标
    return right


# 第三类： 查找第一个大于目标值的数，可变形为查找最后一个不大于目标值的数
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        middle = left + (right - left) / 2
        if target >= nums[middle]:
            left = middle + 1
        else:
            right = middle - 1
    # left是第一个大于目标值的数， left - 1是第一个不大于目标值的数的下标
    return left


if __name__ == '__main__':
    print binary_search([2, 4, 5, 6, 9], 3)
