#!/usr/bin/env python		
#coding:utf-8

"""
1047. 删除字符串中的所有相邻重复项

https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string/
"""

class Solution(object):
	def removeDuplicates(self, S):
		"""
		:type S: str
		:rtype: str

		思路:
		1. 遍历字符串，并且和栈顶元素做比较,如果重复则删除。
		"""
		stack = []
		for i in S:
			if stack and stack[-1] == i:
				stack.pop()
			else:
				stack.append(i)
		return "".join(stack)


if __name__ == '__main__':
	s = Solution()
	string = "abbaca"
	print s.removeDuplicates(string)

