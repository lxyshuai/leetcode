# coding=utf-8
def selection_sort(array):
    """
    选择排序
    时间复杂度:O(N^2)
    额外空间复杂度:O(1)
    第1轮将第1小的放到0位置
    第2轮将第2小的放到1位置
    第3轮将第3小的放到2位置
    第len(array) - 1轮将第 len(array) - 1小的放到len(array) - 2小的位置
    Args:
        array:

    Returns:
    """
    for i in range(0, len(array) - 1):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]



if __name__ == '__main__':
    alist = [54, 26, 93, 77, 44, 31, 44, 55, 20]
    print("原列表为：%s" % alist)
    selection_sort(alist)
    print("新列表为：%s" % alist)
