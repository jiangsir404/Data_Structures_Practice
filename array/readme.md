# 数组和列表
Refer: 
- https://pegasuswang.github.io/python_data_structures_and_algorithms/02_%E6%95%B0%E7%BB%84%E5%92%8C%E5%88%97%E8%A1%A8/array_and_list/
- 数组：为什么很多编程语言中数组都从0开始编号？ https://time.geekbang.org/column/article/40961

## 数组
1. 基本定义

数组（Array）
: 是一种线性表数据结构。它用一组连续的内存空间，来存储一组具有相同类型的数据。

数组(array)在数据结构中是最基本一种线性结构, 其实python有内置array模块，但基本上很少用，Python 的 array 是内存连续、存储的都是同一数据类型的结构，而且只能存数值和字符。

线性表结构
: 顾名思义, 线性表就是数据排成像一条线一样的结构。每个线性表上的数据最多只有前和后两个方向, 常见的数组，链表，队列，栈等都是线性表结构。与之对应的是非线性表结构，例如二叉树，堆，图等。

2. 数组的特点: `连续的内存空间` 和 `相同类型的数据`

正是因为这两个限制，它才有了一个堪称“杀手锏”的特性：“随机访问”。但有利就有弊，这两个限制也让数组的很多操作变得非常低效，比如要想在数组中删除、插入一个数据，为了保证连续性，就需要做大量的数据搬移工作。

> 链表适合插入、删除，时间复杂度 O(1)；数组支持随机访问，根据下标随机访问的时间复杂度为 O(1)。


## 列表
列表(list) 是Python的一种基本数据结构，list 其实和 C++ STL（标准模板库）中的 vector 很类似。

列表的操作时间复杂度分析: 
```
操作	平均时间复杂度
list[index]	O(1)
list.append	O(1)
list.insert	O(n)
list.pop(index), default last element	O(1)
list.remove	O(n)
```