#!/usr/bin/env python		
#coding:utf-8

"""
287. 寻找重复数

https://leetcode-cn.com/problems/find-the-duplicate-number/
"""

class Solution(object):
	def findDuplicate(self, nums):
		"""
		:type nums: List[int]
		:rtype: int

		快慢指针思想, fast 和 slow 是指针, nums[slow] 表示取指针对应的元素
        注意 nums 数组中的数字都是在 1 到 n 之间的(在数组中进行游走不会越界),
        因为有重复数字的出现, 所以这个游走必然是成环的, 环的入口就是重复的元素, 
        即按照寻找链表环入口的思路来做

        这种技巧过于trick
		"""
		fast, slow = 0, 0
		while True:
			fast = nums[nums[fast]]
			slow = nums[slow]
			if slow == fast:
				fast = 0
				while nums[slow] != nums[fast]:
					fast = nums[fast]
					slow = nums[slow]
				return nums[slow]


if __name__ == '__main__':
	s = Solution()
	nums = [3,1,3,4,2]
	print s.findDuplicate(nums)