# coding=utf-8



def merge(array, left, middle, right):
    """
    根据大小将左右数组合并,最后放回原数组
    @param array:
    @type array:
    @param left:
    @type left:
    @param middle:
    @type middle:
    @param right:
    @type right:
    @return:
    @rtype:
    """
    left_current = left
    right_current = middle + 1
    help = []
    while left_current <= middle and right_current <= right:
        if array[left_current] < array[right_current]:
            help.append(array[left_current])
            left_current += 1
        else:
            help.append(array[right_current])
            right_current += 1
    if left_current <= middle:
        help.extend(array[left_current: middle + 1])
    if right_current <= right:
        help.extend(array[right_current: right + 1])
    array[left: right + 1] = help

def merge_sort_process(array, left, right):
    """
    如果left==right,只剩下一个数,无需划分.否则继续划分
    @param array:
    @type array:
    @param left:
    @type left:
    @param right:
    @type right:
    @return:
    @rtype:
    """
    if left == right:
        return
    middle = left + (right - left) / 2
    merge_sort_process(array, left, middle)
    merge_sort_process(array, middle + 1, right)
    merge(array, left, middle, right)

def merge_sort(array):
    """
    归并排序主方法
    Args:
        array:

    Returns:

    """
    if not array:
        return
    merge_sort_process(array, 0, len(array) - 1)


if __name__ == '__main__':
    a = 1  # type: int
    alist = [54, 26, 93, 77, 44, 31, 44, 55, 20]  # type: List[int]
    print(u"原列表为：%s" % alist)
    merge_sort(alist)
    print(u"新列表为：%s" % alist)
