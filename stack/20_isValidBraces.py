#!/usr/bin/env python		
#coding:utf-8

"""
20.有效的括号

https://leetcode-cn.com/problems/valid-parentheses/
"""

class ListStack(object):
    """使用List数据结构实现的顺序栈"""
    def __init__(self, ):
        self._items = []

    def push(self, value):
        """入栈"""
        self._items.append(value)

    def pop(self):
        """弹出栈顶元素"""
        if len(self._items) >0:
            return self._items.pop()
        else:
            return None

    def empty(self):
        return len(self._items) == 0

    def __repr__(self):
        return " ".join("%s" % i for i in self._items)

class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool

		思路:
			 1. 遍历字符串,遇到左括号压入栈中，遇到右括号则弹出栈顶进行匹配
			 2. 如果匹配失败，或者栈中没有数据，则返回False
			 3. 遍历完后，如果栈为空，返回True, 如果栈中还有数据，返回False
		"""
		stack = ListStack()
		for i in s:
			# 遇到左括号压入栈中，遇到右括号则弹出栈顶
			if i in ['(','[','{']:
				stack.push(i)
			elif i in [')',']','}']:
				# 如果匹配失败或者栈为空，返回False
				if stack.empty():
					return False
				left_brace = stack.pop()
				if not self.isMached(left_brace, i):
					return False

		if stack.empty():
			return True
		else:
			return False

	def isMached(self, left, right):
		"""左右括号是否匹配"""
		if left == '(' and right == ')':
			return True
		elif left == '[' and right == ']':
			return True
		elif left == '{' and right == '}':
			return True
		return False

	def isValid2(self, s):
		"""解法2，利用Python的数据结构的极简写法
		"""
		dic = {'}': '{', ']':'[', ')':'('}
		stack = []
		for i in s:
			if i not in dic:
				stack.append(i)
			elif i in dic:
				if not stack:
					return False
				if stack.pop() != dic[i]:
					return False
		return len(stack) == 0


if __name__ == '__main__':
	s = Solution()
	string = "()[]{}"
	print s.isValid2(string)


