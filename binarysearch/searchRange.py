#!/usr/bin/env python		
#coding:utf-8

"""
算法: 在排序数组中查找元素的第一个和最后一个位置

https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/


排除法二分查找在寻找第一个等于target索引以及最后一个target的索引中的应用。

原理: 当mid被分到左区间时，搜索到的是第一个target索引。
当mid被分到右区间时， 搜索到的是最后一个target索引。
"""

class Solution(object):
	def searchRange(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		if not nums or target not in nums:
			return [-1, -1]
		first = self.findFirstIndex(nums, target)
		last = self.findLastIndex(nums, target)
		return [first, last]


	def findFirstIndex(self, nums, target):
		"""中位数被分到左区间，因此搜索到的一定是第一个元素的下标

		Example:
			>>>[5,7,7,8,8,10], 8
			0 2 5
			3 4 5
			3 3 4
			[3, 4]
		"""
		left, right = 0, len(nums) - 1
		while left < right:
			mid = left + (right - left) // 2
			#print left, mid, right
			if nums[mid] < target:
				# mid在左边区间，下一次搜索区间在[mid+1, right]
				left = mid + 1
			else:
				# nums[mid] >= target, 搜索区间在[left, mid]
				right = mid
		return left 

	def findLastIndex(self, nums, target):
		"""中位数被分到右区间，因此搜索到的是最后元素的下标
		
		Example:
			>>>[5,7,7,8,8,10], 8
			0 3 5
			3 4 5
			4 5 5
			[3, 4]		
		"""
		left, right = 0, len(nums) - 1
		while left < right:
			# left=mid, 中位数需要向上取整
			mid = left + (right - left + 1) // 2
			print left, mid, 
			if nums[mid] > target:
				# mid在右边区间
				right = mid - 1
			else:
				left = mid
		return left


if __name__ == '__main__':
	s = Solution()
	nums, target = [5,7,7,8,8,10], 8
	print s.searchRange(nums, target)