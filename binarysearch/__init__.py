#!/usr/bin/env python		
#coding:utf-8

"""
示例代码
"""


def binary_search1(sorted_array, val):
	"""二分查找， 使用left <= right作为循环进行的条件
	"""
	if not sorted_array:
	    return -1

	left, right = 0, len(sorted_array) - 1

	while left <= right:
	    mid = (left + right) // 2  # left + (right-left)/2， 为了屏蔽 python 2/3 差异我用了强转
	    if sorted_array[mid] == val:
	        return mid
	    elif sorted_array[mid] > val:
	        right = mid - 1
	    else:
	        left = mid + 1
	return -1

def binary_search2(nums, val):
	"""二分查找, 使用left < right作为循环进行的条件
	"""
	# 特例判断
	if not nums or val not in nums:
		return -1
	left, right = 0, len(nums) - 1
	while left < right:
		mid = (left + right) // 2
		if nums[mid] < val:
			left = mid + 1
		else:
			right = mid
	return left

def test_binary_search():
	"""二分查找测试"""
	a = list(range(10))

	# 正常值
	assert binary_search1(a, 1) == 1
	assert binary_search1(a, -1) == -1
	assert binary_search2(a, 1) == 1
	assert binary_search2(a, -1) == -1
	# 异常值
	assert binary_search1(None, 1) == -1
	assert binary_search2(None, 1) == -1
	# 边界值
	assert binary_search1(a, 0) == 0
	assert binary_search2(a, 0) == 0


# -------二分查找变形问题---------

class BinarySearch(object):
	def findFirstIndex(self, nums, target):
		"""查找第一个值等于给定值的元素

		中位数被分到左区间，因此搜索到的一定是第一个元素的下标

		Example:
			>>>[5,7,7,8,8,10], 8
			0 2 5
			3 4 5
			3 3 4
			[3, 4]
		"""
		# 特例
		if target not in nums:
			return -1
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
		"""查找最后一个值等于给定值的元素

		中位数被分到右区间，因此搜索到的是最后元素的下标
		
		Example:
			>>>[5,7,7,8,8,10], 8
			0 3 5
			3 4 5
			4 5 5
			[3, 4]		
		"""
		# 特例
		if target not in nums:
			return -1
		left, right = 0, len(nums) - 1
		while left < right:
			# left=mid, 中位数需要向上取整
			mid = left + (right - left + 1) // 2
			if nums[mid] > target:
				# mid在右边区间
				right = mid - 1
			else:
				left = mid
		return left

	def findFirstLarge(self, nums, target):
		"""查找第一个大于等于给定值的元素

		Example
			>>>[3，4，6，7，10], 5
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
		# 特例判断
		if nums[left] >= target:
			return left
		else:
			return -1

	def findLastSmall(self, nums, target):
		"""查找最后一个小于等于给定值的元素
		"""
		left, right = 0, len(nums) - 1
		while left < right:
			# left=mid, 中位数需要向上取整
			mid = left + (right - left + 1) // 2
			if nums[mid] > target:
				# mid在右边区间
				right = mid - 1
			else:
				left = mid
		if nums[left] <= target:
			return left
		else:
			return -1


def test_search_range():
	"""测试二分查找的范围变形问题"""
	search = BinarySearch()
	# 正常值
	nums, target = [5,6,6,8,8,8,10], 8
	assert search.findFirstIndex(nums, target) == 3
	assert search.findLastIndex(nums, target) == 5
	assert search.findFirstLarge(nums, 7) == 3
	assert search.findLastSmall(nums, 7) == 2

	# 异常值
	nums, target = [5,6,6,8,8,8,10], 12
	assert search.findFirstIndex(nums, target) == -1
	assert search.findLastIndex(nums, target) == -1
	assert search.findFirstLarge(nums, target) == -1
	assert search.findLastSmall(nums, target) == 6

	# 边界值
	nums, target = [5,6,6,8,8,8,10], 10
	assert search.findFirstIndex(nums, target) == 6
	assert search.findLastIndex(nums, target) == 6
	assert search.findFirstLarge(nums, target) == 6
	assert search.findLastSmall(nums, target) == 6

if __name__ == '__main__':
	test_binary_search()
	test_search_range()