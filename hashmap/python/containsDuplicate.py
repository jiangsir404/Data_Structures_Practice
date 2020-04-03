#!/usr/bin/env python		
#coding:utf-8

"""
217. 存在重复元素

https://leetcode-cn.com/problems/contains-duplicate/
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_dic = {}
        for i in nums:
            if i in num_dic:
                return True
            else:
                num_dic[i] = 1;
        
        return False