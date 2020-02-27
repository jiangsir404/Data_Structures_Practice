#!/usr/bin/env python		
#coding:utf-8

"""
面试题40. 最小的k个数

https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/
"""

from heapq import heappush, heappop
class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]

        解法1: 直接利用py的heapq构建最小堆即可 时间复杂度: n * logk
        """
        if not arr:
            return -1
        min_heap = [] # 最小堆
        rets = []
        for i in arr:
            heappush(min_heap, i)
        for j in range(k):
            rets.append(heappop(min_heap))
        return rets

if __name__ == '__main__':
	s = Solution()
	nums = [4,5,1,6,2,7,3,8]
	print(s.getLeastNumbers(nums, 4))