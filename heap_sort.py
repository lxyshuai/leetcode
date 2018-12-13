# coding=utf-8
"""
堆排序：不稳定

用数组实现完全二叉树
根节点从0开始计算
i节点的左节点为2i+1(设i在第j层，i的左子节点在第j+1层，
                 j层最左的节点为a = 0+2^0+2^1+...+2^j,j+1层最左的节点为b = 0+2^0+2^1+...+2^j+2^(j+1),
                 j的左子节点为b + (i - a) * 2 = b - 2a + 2i = 2i + 1
i节点的右节点为2i+2
i节点的父节点为(i-1)/2

N个节点的完全二叉树，高度是logN
建立大根堆的过程：将第1个数放入节点数为0的大根堆，将第2个数放入节点数为1的大根堆...将第i个数放入节点数为n-1的大根堆中
建立大根堆的时间复杂度：log0+log1+...+log(i-1) = O(N)
"""


############
# 插入型做法 #
############


def heap_sort(array):
    if not array:
        return array
    else:
        build_max_heap1(array)
        last_index = len(array) - 1
        for _last_index in range(last_index, 0, -1):
            array[0], array[_last_index] = array[_last_index], array[0]
            heapify_nonrecursive(array, 0, _last_index - 1)


def heap_insert(array, index):
    parent_index = (index - 1) / 2
    while parent_index >= 0 and array[index] > array[parent_index]:
        array[index], array[parent_index] = array[parent_index], array[index]
        index = parent_index
        parent_index = (index - 1) / 2


def build_max_heap1(array):
    """
    插入法建堆,时间复杂度:O(nlogn)
    @param array:
    @return:
    """
    for index in range(0, len(array)):
        heap_insert(array, index)


def heapify_nonrecursive(array, index, last_index):
    left_child_index = index * 2 + 1
    right_child_index = index * 2 + 2
    while left_child_index <= last_index:
        # 找出三个数中最小值
        largest_index = index
        if array[left_child_index] > array[largest_index]:
            largest_index = left_child_index
        if right_child_index <= last_index and array[right_child_index] > array[largest_index]:
            largest_index = right_child_index
        if largest_index != index:
            array[index], array[largest_index] = array[largest_index], array[index]
            index = largest_index
            left_child_index = index * 2 + 1
            right_child_index = index * 2 + 2
        else:
            break


def heapify_recursive(array, index, last_index):
    left_child_index = index * 2 + 1
    right_child_index = index * 2 + 2
    largest_index = index
    if array[left_child_index] > array[largest_index]:
        largest_index = left_child_index
    if right_child_index <= last_index and array[right_child_index] > array[largest_index]:
        largest_index = right_child_index
    if largest_index != index:
        array[index], array[largest_index] = array[largest_index], array[index]
        heapify_recursive(array, largest_index, last_index)


def build_max_heap2(array):
    """
    初始化建堆只需要对二叉树的非叶子节点调用adjusthead()函数，由下至上，由右至左选取非叶子节点来调用adjusthead()函数。那么倒数第二层的最右边的非叶子节点就是最后一个非叶子结点。
　　 假设高度为k，则从倒数第二层右边的节点开始，这一层的节点都要执行子节点比较然后交换（如果顺序是对的就不用交换）；
    倒数第三层呢，则会选择其子节点进行比较和交换，如果没交换就可以不用再执行下去了。如果交换了，那么又要选择一支子树进行比较和交换；高层也是这样逐渐递归。
    @param array:
    @return:
    """
    # 从第一个非叶节点开始
    last_index = len(array) - 1
    first_non_leaf_node_index = (last_index - 1) / 2
    for index in range(first_non_leaf_node_index, -1, -1):
        heapify_recursive(array, index, last_index)


if __name__ == '__main__':
    array = range(100, -1, -1)
    # build_max_heap2(array)
    print array
    heap_sort(array)
    print array
