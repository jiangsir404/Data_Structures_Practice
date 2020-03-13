#!/usr/bin/env python		
#coding:utf-8

"""
算法: 27.移除元素

https://leetcode-cn.com/problems/remove-element/
"""

class Solution(object):
    def removeElement(self, nums, val):
        """快慢双指针解法
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in nums:
        	if j != val:
        		nums[i] = j
        		i += 1
        return i

if __name__ == '__main__':
	s = Solution()
	nums = [0,1,2,2,3,0,4,2]
	val = 2
	print s.removeElement(nums, val), nums