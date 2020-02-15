#!/usr/bin/env python		
#coding:utf-8

"""
插入排序

算法思路:
1. 首先，我们将数组中的数据分为两个区间，已排序区间和未排序区间。初始已排序区间只有一个元素，就是数组的第一个元素。
2. 取未排序区间中的元素，在已排序区间中找到合适的插入位置将其插入
3. 重复这个过程，直到未排序区间中元素为空，算法结束。
"""

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


def test_insert_sort():
	nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
	print insert_sort(nums)
	#assert insert_sort(nums) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


if __name__ == '__main__':
	test_insert_sort()