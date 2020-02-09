#!/usr/bin/env python		
#coding:utf-8

"""
374. 猜数字大小

https://leetcode-cn.com/problems/guess-number-higher-or-lower/submissions/
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        print guess(n)
        left, right = 1, n
        while left <= right:
            mid = left + (right - left) // 2
            res = guess(mid)
            if res == 0:
                return mid
            if res == 1:
                left = mid + 1
            elif res == -1:
                right = mid - 1
