## 二分查找
- bisect --- 数组二分查找算法 https://docs.python.org/zh-cn/3/library/bisect.html

python内置了一个二分查找的模块 bisect

bisect.bisect_left(a, x, lo=0, hi=len(a))
: 在 a 中找到 x 合适的插入点以维持有序。参数 lo 和 hi 可以被用于确定需要考虑的子集；如果 x 已经在 a 里存在，那么插入点会在已存在元素之前（也就是左边）。如果 a 是列表（list）的话，返回值是可以被放在 list.insert() 的第一个参数的。
- a: array, 即有序数组
- x: 待插入元素

bisect.bisect_right(a, x, lo=0, hi=len(a))
bisect.bisect(a, x, lo=0, hi=len(a))
: 类似于 bisect_left()，但是返回的插入点是 a 中已存在元素 x 的右侧。

```
import bisect
>>> a = range(10)
>>> bisect.bisect_left(a, 2.5)
3
```

具体实现可以参考bisect的源码: https://github.com/python/cpython/blob/3.8/Lib/bisect.py