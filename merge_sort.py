# coding=utf-8
def merge_sort(array):
    def merge(array, left, middle, right):
        help = []
        left_current = left
        right_current = middle + 1
        while left_current <= middle and right_current <= right:
            if array[left_current] > array[right_current]:
                help.append(array[right_current])
                right_current += 1
            else:
                help.append(array[left_current])
                left_current += 1
        if left_current <= middle:
            help.extend(array[left_current: middle + 1])
        if right_current <= right:
            help.extend(array[right_current: right + 1])
        array[left: right + 1] = help

    def split(array, left, right):
        if left == right:
            return
        middle = left + (right - left) / 2
        split(array, left, middle)
        split(array, middle + 1, right)
        merge(array, left, middle, right)

    split(array, 0, len(array) - 1)


if __name__ == '__main__':
    a = 1  # type: int
    alist = [54, 26, 93, 77, 44, 31, 44, 55, 20]  # type: List[int]
    print(u"原列表为：%s" % alist)
    merge_sort(alist)
    print(u"新列表为：%s" % alist)
