#!/usr/bin/env python		
#coding:utf-8

"""
算法: 35.搜索插入位置

Referer:
https://leetcode-cn.com/problems/search-insert-position/
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """最简单暴力的方法，时间复杂度未O(n)
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index, value in enumerate(nums):
        	if value < target:
        		continue
        	elif value == target:
        		return index
        	elif value > target:
        		return index
        return len(nums)

    def searchInsert(self, nums, target):
    	"""二分查找
    	"""
    	size = len(nums)
    	# 特判
    	if size ==0: return 0
    	if nums[size-1] < target: return size
    	left, right = 0, size - 1
    	while left < right:
    		mid = (left + right) / 2
    		if nums[mid] < target:
    			left = mid + 1
    		else:
    			right = mid
    	return left



if __name__ == '__main__':
	s = Solution()
	nums, target = [1,3,5,6], 7
	print s.searchInsert(nums, target)