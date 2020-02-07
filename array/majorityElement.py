#!/usr/bin/env python		
#coding:utf-8

"""
算法: 多数元素
Desc: 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

示例 1:
	输入: [3,2,3]
	输出: 3
示例 2:
	输入: [2,2,1,1,1,2,2]
	输出: 2

Referer:
- https://leetcode-cn.com/problems/majority-element/
"""

from collections import Counter

class Solution(object):
    def majorityElement(self, nums):
        """使用collections的Counter结构来计数
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        max_count =  sorted(counter.values())[-1]
        for key, value in counter.items():
        	if value == max_count:
        		return key

   	def majorityElement2(self, nums):
   		"""统计每个数出现次数和记录最大出现次数的元素
   		"""
   		dict = {}
   		max_num = nums[0]
   		for i in nums:
   			if i in dict:
   				dict[i] += 1
   				if dict[i] > dict[max_num]:
   					max_num = i
   			else:
   				dict[i] = 1
   		return max_num

   	def majorityElement3(self, nums):
   		"""众数是出现次数超过一半的数，所以排序后中间的数就是众数
   		"""
   		return sorted(nums)[len(nums) // 2]


if __name__ == '__main__':
	s = Solution()
	print s.majorityElement2([1,2,3,4,4,4,3])
	print s.majorityElement2([3,3,4])