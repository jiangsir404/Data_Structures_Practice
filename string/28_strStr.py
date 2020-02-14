#!/usr/bin/env python		
#coding:utf-8

"""
算法: 28. 实现 strStr()

https://leetcode-cn.com/problems/implement-strstr/submissions/
"""

class Solution(object):
	def strStr(self, haystack, needle):
		"""遍历匹配, 暴力解法，时间复杂度最高
		:type haystack: str
		:type needle: str
		:rtype: int
		"""
		if needle not in haystack:
		    return -1

		sublen = len(needle)
		for i in range(0, len(haystack)-len(needle)+1):
		    print haystack[i:i+sublen], needle
		    if haystack[i:i+sublen] == needle:
		        return i
		return 0

	def strStr(self, haystack, needle):
		"""利用字符串函数find()
		"""
		return haystack.find(needle)

if __name__ == '__main__':
	s = Solution()
	h, n = "mississippi", "pi"
	print s.strStr(h, n)