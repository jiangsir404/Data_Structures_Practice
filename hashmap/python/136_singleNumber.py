#!/usr/bin/env python		
#coding:utf-8

"""
136. 只出现一次的数字

https://leetcode-cn.com/problems/single-number/
"""

class Solution(object):
    def singleNumber(self, nums):
        """

        思路: 使用异或 时间复杂度O(n) 空间复杂度O(1) 
		0 ^ i = i
		i ^ i = 0
		0 ^ j ^ i ^ i = j

        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in nums:
            i = i ^ j
        return i