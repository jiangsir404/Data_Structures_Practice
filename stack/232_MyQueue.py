#!/usr/bin/env python		
#coding:utf-8

"""
232.用栈实现队列

https://leetcode-cn.com/problems/implement-queue-using-stacks/solution/bzhan-tu-jie-leetcode-232-yong-zhan-mo-ni-dui-lie-/
"""

class MyQueue(object):
	"""用两个栈的搬移来实现队列先进先出操作"""
	def __init__(self):
		"""
		Initialize your data structure here.
		"""
		self._A = []
		self._B = []


	def push(self, x):
		"""
		Push element x to the back of queue.
		:type x: int
		:rtype: None
		"""
		self._A.append(x)


	def pop(self):
		"""
		Removes the element from in front of queue and returns that element.
		:rtype: int
		"""
		while len(self._A) != 0:
			self._B.append(self._A.pop())
		rets = self._B.pop()
		while len(self._B) != 0:
			self._A.append(self._B.pop())
		return rets


	def peek(self):
		"""
		Get the front element.
		:rtype: int
		"""
		while len(self._A) != 0:
			self._B.append(self._A.pop())
		rets = self._B[-1]
		while len(self._B) != 0:
			self._A.append(self._B.pop())
		return rets		


	def empty(self):
		"""
		Returns whether the queue is empty.
		:rtype: bool
		"""
		return len(self._A) == 0

	def __repr__(self):
		return " ".join("%s" % i for i in self._A)



if __name__ == '__main__':
# Your MyQueue object will be instantiated and called as such:
	obj = MyQueue()
	obj.push(1)
	obj.push(2)
	param_2 = obj.pop()
	param_3 = obj.peek()
	param_4 = obj.empty()
	print param_2, param_3, param_4
	print obj.pop(), obj.empty()