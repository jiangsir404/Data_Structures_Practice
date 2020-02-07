#!/usr/bin/env python		
#coding:utf-8

"""
算法: 两数之和

示例： 
	给定 nums = [2, 7, 11, 15], target = 9

	因为 nums[0] + nums[1] = 2 + 7 = 9
	所以返回 [0, 1]

> 返回下标会比返回值的难度要大。没法用排序的思路来做。

Referer:
- https://leetcode-cn.com/problems/two-sum/
"""

class Solution(object):
    def twoSum(self, nums, target):
        """先排序 + 首尾递进查找， 复杂度: O(n*logn+n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        Notice: 返回下标排序时需要保存原来位置，建议使用位置来排序，而不是值排序
        """
        i = 0
        j = len(nums) - 1
        sorted_num = sorted(range(len(nums)), key=lambda x: nums[x]) #对位置进行排序，而不是对值进行排序，复杂度O(n*logn)
        while i < j:
        	sums = nums[sorted_num[i]] + nums[sorted_num[j]]
        	if sums > target:
        		j -= 1
        	elif sums < target:
        		i += 1
        	elif sums == target:
        		return [sorted_num[i], sorted_num[j]]

    def twoSum(self, nums, target):
    	"""利用字典哈希表，时间复杂度: O(n)
    	"""
    	hashmap = {}
    	for index, value in enumerate(nums):
    		diff = target - value
    		if diff in hashmap:
    			return [hashmap.get(diff), index]
    		hashmap[value] = index

if __name__ == '__main__':
	s = Solution()
	nums = [2, 7, 11, 15]
	print s.twoSum(nums, 9)
	nums = [3,2,4]
	print s.twoSum(nums, 6)
	nums = [3,3]
	print s.twoSum(nums, 6)