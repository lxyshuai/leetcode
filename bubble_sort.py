# coding=utf-8
def bubble_sort(array):
    """
    第一轮从len(array)-1开始上上浮到0
    第二轮从len(array)-1开始上上浮到1
    ...
    最后一轮从len(array)-1开始上上浮到len(array)-2
    @param array:
    @type array:
    @return:
    @rtype:
    """
    for i in range(0, len(array)):
        for j in range(len(array) - 1, i, - 1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]


if __name__ == '__main__':
    alist = [54, 26, 93, 77, 44, 31, 44, 55, 20]
    print("原列表为：%s" % alist)
    bubble_sort(alist)
    print("新列表为：%s" % alist)
