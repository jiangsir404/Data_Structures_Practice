#!/usr/bin/env python		
#coding:utf-8

"""
算法: 26.删除排序数组中的重复项

https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """双指针解法，快慢指针
        :type nums: List[int]
        :rtype: int

        数组完成排序后，我们可以防止两个指针i,j.其中i是慢指针，而j是快指针，只要nums[i]==nums[j],我们就增加j以跳过重复项。
        和移动零有点类似
        """
        if len(nums) == 0:return 0;
        i = 0
        for j in range(1, len(nums)):
        	if nums[i] != nums[j]:
        		i += 1
        		nums[i] = nums[j]
        	j += 1
        return i+1


if __name__ == '__main__':
	s = Solution()
	nums = [1,1,2]
	print s.removeDuplicates(nums), nums
