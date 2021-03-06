# 排序算法 - (一)
[TOC]
Referer:
- https://time.geekbang.org/column/article/41802

## 一、如何分析一个“排序算法”？
衡量一个算法的好坏可以从算法的时间复杂度，空间复杂度以及算法稳定性来判断。
### 1.1 排序算法的执行效率
对于排序算法执行效率的分析，我们一般会从这几个方面来衡量
1. 最好情况、最坏情况、平均情况时间复杂度
2. 时间复杂度的系数、常数 、低阶
3. 比较次数和交换（或移动）次数

按照时间复杂度可以简单把常用经典排序算法分为以下三类:
![image](DF96E1367E66471DA1C460AC30581DBB)


### 1.2 排序算法的内存消耗
算法的内存消耗可以通过空间复杂度来衡量，排序算法也不例外。不过，针对排序算法的空间复杂度，我们还引入了一个新的概念，原地排序（Sorted in place）。原地排序算法，就是特指空间复杂度是 O(1) 的排序算法。
### 1.3 排序算法的稳定性
算法的稳定性
: 即排序前后两个相同的值的位置不变

比如我们有一组数据 2，9，3，4，8，3，按照大小排序之后就是 2，3，3，4，8，9。这组数据里有两个 3。经过某种排序算法排序之后，如果两个 3 的前后顺序没有改变，那我们就把这种排序算法叫作稳定的排序算法；如果前后顺序发生变化，那对应的排序算法就叫作不稳定的排序算法。

综合排序算法的时间复杂度，空间复杂度以及稳定性，我们可以对比以下各个排序算法的优劣
![image](DD8A2D606F4442EA9F46BBDCD86D0C90)

## 二、冒泡，插入和选择排序
### 2.1 冒泡排序
**2.1.1 算法描述**
1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。在这一点，最后的元素应该会是最大的数。
3. 针对所有的元素重复以上的步骤，除了最后一个。
4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较

![image](4904D2256CB94CE3B35BE662B185CD0D)

优化1:某一趟遍历如果没有数据交换，则说明已经排好序了，因此不用再进行迭代了。 #用一个标记记录这个状态即可。

优化2: 记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序了。 因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。


**2.1.2 算法实现:**

```python
# python
def bubble_sort(nums):
	"""冒泡排序"""
	for i in range(len(nums)-1):
		for j in range(len(nums)-i-1):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
		print nums

	return nums

def bubble_sort1(nums):
	"""冒泡排序优化1"""
	for i in range(len(nums)-1):
		swap_count = 0 # 记录每次冒泡交换的次数
		for j in range(len(nums)-i-1):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1] = nums[j+1], nums[j]
				swap_count += 1
		print nums, swap_count
		if swap_count == 0:
			break

	return nums

def bubble_sort2(nums):
	"""冒泡排序优化1"""
	k =  len(nums) - 1 #k为每次冒泡循环的范围
	for i in range(len(nums) - 1):
	    flag = True
	    for j in range(0,k):        #只遍历到最后交换的位置即可
	        if  nums[j] > nums[j+1] :
	            nums[j+1],nums[j] = nums[j],nums[j+1]
	            k = j               #记录最后交换的位置
	            flag = False
	    print nums
	    if flag :
	        break
	return nums
>>>
[4, 5, 3, 2, 1, 6]
[4, 3, 2, 1, 5, 6]
[3, 2, 1, 4, 5, 6]
[2, 1, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
bubble sort optimize 1
[3, 4, 1, 2, 5, 6] 3
[3, 1, 2, 4, 5, 6] 2
[1, 2, 3, 4, 5, 6] 2
[1, 2, 3, 4, 5, 6] 0
bubble sort optimize 2
[3, 4, 1, 2, 5, 6]
[3, 1, 2, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
```


```c++
# c++
void bubble_sort(int a[],int n)
{
	int i,j;
	for(i=0;i<n&&flag;i++)//循环n次,若没有发现一个逆序对，就可以直接结束整个排序过程 
	{
		flag=0;
		for(j=0;j<n-i;j++)//j是从(0,n-i)，n-i后面是已经排好了序 
		{
			if(a[j]>a[j+1])//交换逆序对 
			{
				int t=a[j];
				a[j]=a[j+1];
				a[j+1]=t;
				flag=1;
			}
		}
	}
}
```

**2.1.3 算法性能**
1. 空间复杂度: 冒泡过程只涉及相邻两个元素的交换，只需要常量级的临时空间(交换用), 所以空间复杂度为O(1), 是一个原地排序算法
2. 稳定性: 相邻元素相等时不会做交换，因此冒泡排序是稳定的算法。
3. 时间复杂度, 最后的情况数据有序，只需要一次冒泡即可(优化1), 最好时间复杂度为O(n), 最坏的情况倒序时我们需要进行n次冒泡, 最坏时间复杂度为O(n**2),平均时间复杂度可通过求概率的方式得出为O(n**2)


### 2.2 插入排序
**2.2.1 算法描述**
1. 首先，我们将数组中的数据分为两个区间，已排序区间和未排序区间。初始已排序区间只有一个元素，就是数组的第一个元素。
2. 取未排序区间中的元素，在已排序区间中找到合适的插入位置将其插入
3. 取未排序区间中的元素，在已排序区间中找到合适的插入位置将其插入

![image](D4B092040019436CA69ACA5449A83B9B)

**2.2.2 算法实现**
```python
# python
def insert_sort(nums):
	if len(nums) <=1:
		return nums
	for i in range(1, len(nums)):
		value = nums[i]
		j = i - 1
		# 查找插入位置

		for j in range(i-1, -2, -1):
			if nums[j] > value:
				nums[j+1] = nums[j] # 数据往后搬移
			else:
				break

		nums[j+1] = value #j+1就是插入点
		print nums

	return nums

```

```
# c
void InsertSort(int a[],int n)
{
	int i,j;
	for(i=2;i<=n;i++)//第一个元素不用动 
	{
		if(a[i]<a[i-1])//和前一个元素比较是否右逆序对
		{
			a[0]=a[i];
			a[i]=a[i-1];
			for(j=i-2;j&&a[0]<a[j];j--)//i=2 j=i-2 
			{
				a[j+1]=a[j];//记录后移 
			}
			a[j+1]=a[0];//退出循环j多减了1 
		}
		
	}
}
```

**2.2.3 算法性能**
1. 空间复杂度: 插入排序不需要额外的空间，空间复杂度为O(1),是一个原地排序算法
2. 稳定性: 对于值相同的元素，我们可以选择将后面出现的元素，插入到前面出现元素的后面，这样就可以保持原有的前后顺序不变，所以插入排序是稳定的排序算法
3. 时间复杂度，同冒泡排序一样，最好是O(n),最坏是O(n**2), 平均O(n**2)

### 2.3 选择排序
**2.3.1 算法描述**

它的工作原理是每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完。 

![image](304912A6B1E04C0FBC2AFFCA2BB9DEB6)

> 选择排序（Selection sort）是一种简单直观的排序算法。缺点是不稳定的排序方法（比如序列[5， 5， 3]第一次就将第一个[5]与[3]交换，导致第一个5挪动到第二个5后面）。

**2.3.2 算法实现**
```
def select_sort(nums):
	if len(nums) <= 1:
		return nums
	for j in range(0, len(nums)-1):
		# 在待排序的数据中找出最小的元素
		min = j
		for i in range(j+1, len(nums)):
			if nums[i] < nums[min]:
				min = i

		# 存放到序列的起始位置
		if min != j:
			nums[j],nums[min] = nums[min], nums[j]
		print nums
```

比较: 总的来说，冒泡排序最好理解，代码简洁，其次是选择排序，插入排序不太好理解，涉及到寻找插入点以及数据搬移的操作。代码需要考虑的边界条件容易写错。

**2.3.3 算法性能**
1. 空间复杂度: 选择排序空间复杂度为 O(1)，是一种原地排序算法
2. 稳定性: 选择排序是一种不稳定的排序算法。从我前面画的那张图中，你可以看出来，选择排序每次都要找剩余未排序元素中的最小值，并和前面的元素交换位置，这样破坏了稳定性。
3. 时间复杂度: 选择排序的最好情况时间复杂度、最坏情况和平均情况时间复杂度都为 O(n2)

## 三、总结
1. 通过对比我们看到选择排序无论从时间复杂度上还是从稳定性上都不如冒泡和选择，因此用的不多。

2. **为什么插入排序要比冒泡排序更受欢迎**

冒泡排序无论怎么优化，元素交换d的次数是一个固定值，就是原始数据的逆序度，插入排序同样无论怎么优化，元素移动的次数也等于原始数据的逆序度。

但是，从代码实现上来看，冒泡排序的数据交换要比插入排序的数据移动要复杂，冒泡排序需要 3 个赋值操作，而插入排序只需要 1 个。我们来看这段操作：
```

冒泡排序中数据的交换操作：
if (a[j] > a[j+1]) { // 交换
   int tmp = a[j];
   a[j] = a[j+1];
   a[j+1] = tmp;
   flag = true;
}

插入排序中数据的移动操作：
if (a[j] > value) {
  a[j+1] = a[j];  // 数据移动
} else {
  break;
}
```
假设分别用冒泡排序和插入排序对同一个逆序度是 K 的数组进行排序。用冒泡排序，需要 K 次交换操作，每次需要 3 个赋值语句，所以交换操作总耗时就是 3*K 单位时间。而插入排序中数据移动操作只需要 K 个单位时间。

实际测试也会发现插入排序会比冒泡排序算法的耗时更低，效率更好。插入排序算法还有很大的优化空间，比如希尔排序就是对插入排序的优化。

3. 三种排序算法的对比

![image](6A960D52B2394803B371586D4FA8AF4B)

4. 三种排序算法都是基于数组实现的，如果是链表实现的数据，一般而言，考虑只能改变节点位置，冒泡排序相比于数组实现，比较次数一致，但交换时操作更复杂；插入排序，比较次数一致，不需要再有后移操作，找到位置后可以直接插入，但排序完毕后可能需要倒置链表；选择排序比较次数一致，交换操作同样比较麻烦。综上，时间复杂度和空间复杂度并无明显变化，若追求极致性能，冒泡排序的时间复杂度系数会变大，插入排序系数会减小，选择排序无明显变化。

因此插入排序更适合基于链表的数据进行排序。