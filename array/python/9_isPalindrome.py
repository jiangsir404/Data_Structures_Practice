#!/usr/bin/env python		
#coding:utf-8

"""
9.算法: 回文数

https://leetcode-cn.com/problems/palindrome-number/
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x) 
        return s[::-1] == s


if __name__ == '__main__':
	s = Solution()
	s.isPalindrome(-121)