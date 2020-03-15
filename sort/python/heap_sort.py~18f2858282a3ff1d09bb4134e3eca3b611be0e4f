#!/usr/bin/env python		
#coding:utf-8

"""
堆排序: 可以通过将所有值推入堆中然后每次弹出一个最小值项来实现。
"""

from heapq import heappush, heappop

def heapsort(nums):
	min_heap = []
	for i in nums:
		heappush(min_heap, i) # 默认构建最小堆
	return [heappop(min_heap) for i in range(len(min_heap))]

def test_heap():
	nums = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
	assert heapsort(nums) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if __name__ == '__main__':
	test_heap()