#!/usr/bin/env python		
#coding:utf-8

"""
选择排序:

算法描述:
	每一次从待排序的数据元素中选出最小（或最大）的一个元素，存放在序列的起始位置，直到全部待排序的数据元素排完。

记忆诀窍
	1. 划分左有序区间和右无序区间range(0,n-1)->range(i+1,n), 第一次遍历空出第一个元素，否则第二次遍历会溢出
	2. 在未排序区间找到最小值, 先让min指针指向第一个元素j, 然后遍历range(j+1,n)依次比较即可。
"""

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

	return nums

def test_select_sort():
	nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
	assert select_sort(nums) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == '__main__':
	test_select_sort()