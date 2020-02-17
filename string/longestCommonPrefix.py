#!/usr/bin/env python		
#coding:utf-8

"""
14. 最长公共前缀

https://leetcode-cn.com/problems/longest-common-prefix/submissions/
"""

class Solution(object):
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if not strs:
		    return ""
		min_str = min(strs, key=lambda x:len(x))
		min_len = len(min_str)
		for i in range(min_len):
		    chars = strs[0][i]
		    for s in strs:
		        if s[i] != chars:
		            #print i
		            return s[:i]
		return min_str

if __name__ == '__main__':
	s = Solution()
	strs = ["a","b"]
	print s.longestCommonPrefix(strs)
          