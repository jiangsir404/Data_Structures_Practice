#!/usr/bin/env python		
#coding:utf-8

"""
冒泡排序:

1. 比较相邻的元素。交换逆序对
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。 最后一趟可以确定最后一个为最大元素
3. 对[0, max-i] 的元素集重复上述操作

优化1：某一趟遍历如果没有数据交换，则说明已经排好序了，直接break退出排序，用一个标记记录这个状态即可。

优化2: 记录某次遍历时最后发生数据交换的位置，这个位置之后的数据显然已经有序了。 因此通过记录最后发生数据交换的位置就可以确定下次循环的范围了。
"""

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

def test_bubble_sort():
	nums = [4, 5, 6, 3, 2, 1]
	assert bubble_sort(nums) == [1, 2, 3, 4, 5, 6]

	print 'bubble sort optimize 1'
	nums = [3, 5, 4, 1, 2, 6]
	assert bubble_sort1(nums) == [1, 2, 3, 4, 5, 6]

	print 'bubble sort optimize 2'
	nums = [3, 5, 4, 1, 2, 6]
	assert bubble_sort2(nums) == [1, 2, 3, 4, 5, 6]

if __name__ == '__main__':
	test_bubble_sort()