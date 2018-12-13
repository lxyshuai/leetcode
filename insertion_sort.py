# coding=utf-8

def insertion_sort(array):
    # type: (list[int]) -> None
    """
    第1轮下标为1的数字开始向0-0已排序的数组插入该数字
    第2轮下标为2的数字开始向0-1以排序以排序数组插入该数字
    第len(array)-2轮下标为len(array)-1的数字开始向0-len(array)-2
    插入排序
    时间复杂度:O(N^2)
    额外空间复杂度:O(1)
    """
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
            else:
                break


if __name__ == '__main__':
    alist = [54, 26, 93, 77, 44, 31, 44, 55, 20]
    print("原列表为：%s" % alist)
    insertion_sort(alist)
    print("新列表为：%s" % alist)
