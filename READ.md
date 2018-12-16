## Array
### 数组的全排列
* 用递归进行全排列(667, 526)
### 数组的全组合
* 用递归要或不要
### 构造特定数列
* 先找规律(667)
### 股票问题
[链接](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems/111002?page=3)
> 第一个变量表示股市(0代表没有股市)，第二个变量表示最大交易次数，第三个变量表示手中股票库存
> Base cases:
> T[0][k][0] = 0 # 没有股市的时候没有利润
> T[i][0][0] = 0 # 没有交易的时候没有利润
> T[0][k][1] = -Infinity # 强调1如果没有库存或不允许交易，我们无法拥有库存
> T[i][0][1] = -Infinity # 强调1如果没有库存或不允许交易，我们无法拥有库存
>
> Recurrence relations:
> T[i][k][0] = max(T[i-1][k][0], T[i-1][k][1] + prices[i])
> T[i][k][1] = max(T[i-1][k][1], T[i-1][k-1][0] - prices[i])
> 每个交易的特点是两个动作成对出现 - 买入和卖出，并且由于“无多重交易”限制，这两者之间不能有其他行为交错。我们可以假设只有行动购买才会改变允许的最大交易数量,
> 为了找到最后一天结束时的最大利润，我们可以简单地遍历prices数组T[i][k][0]并T[i][k][1]根据上面的重复关系进行更新。最终的答案是T[i][k][0]（如果最终掌握0库存，我们总会有更大的利润）。
### 二分查找
* 二分查找的middle取的是下中位数，所有确认(=)边界条件的地方都要举特例来确认，排除特殊情况。
[链接](http://www.cnblogs.com/grandyang/p/6854825.html)
>注意二分查找法的写法并不唯一，主要可以变动地方有四处：
>第一处是right的初始化，可以写成 nums.size() 或者 nums.size() - 1
>
>第二处是left和right的关系，可以写成 left < right 或者 left <= right
>
>第三处是更新right的赋值，可以写成 right = mid 或者 right = mid - 1
>
>第四处是最后返回值，可以返回left，right，或right - 1
>
>但是这些不同的写法并不能随机的组合，像博主的那种写法，若right初始化为了nums.size()，那么就必须用left < right，而最后的right的赋值，用哪个都可以，博主偷懒就不写-1了。但是如果我们right初始化为 nums.size() - 1，那么就必须用 left <= right，并且right的赋值要写成 right = mid - 1，不然就会出错。
[left<right right=middle; left<=right right = middle - 1](https://blog.csdn.net/shuiyuejihua/article/details/81166069)
### 矩阵
* 观察坐标间的关系(48)

### 取余+除法
* ``商, 余数 = divmod(被除数, 除数)``

### 高度平衡BST
* 用递归划分一半

### python的交换有坑
* 在x, y = y, x的背后都发生了些什么呢？
一般情况下Python语句是从左到右解析一个语句的，但在赋值操作的时候，因为是右值具有更高的计算优先级，所以需要从右向左解析。
对于x, y = y, x，它的执行顺序如下：
先计算右值y , x(这里是简单的原值，但可能会有表达式或者函数调用的计算过程)， 在内存中创建元组(tuple)，存储y, x分别对应的值；
计算左边的标识符，元组被分别分配给左值，通过解包(unpacking)，元组中第一个标示符对应的值(y)，分配给左边第一个标示符(x)，然后元组中第二个标示符对应的值(x)，分配给左边第二个标示符(y)，完成了x和y的值交换。
* `` head, head.next = head.next, None``和``head.next, head = None, head.next``，
如果``head.next==None``时第一个会出错，head赋值为None后，head.next报错，所以要看好先后顺序


### 链表环
[链接](http://www.cnblogs.com/hiddenfox/p/3408931.html)
[链接](http://www.cnblogs.com/wuyuegb2312/p/3183214.html)

### 求分部分的时候快排的partitaion

### 如果数组有排序，考虑二分查找

### 如果找特例，可以考虑下位运算（出现次数的问题很好用， Single Number）

### python负数二进制有坑（https://www.jianshu.com/p/96ea0b077051）