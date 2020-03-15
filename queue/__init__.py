#!/usr/bin/env python		
#coding:utf-8


"""
用数组实现的队列
"""
class ArrayQueue(object):
	def __init__(self, capacity):
		self._items = []
		self._capacity = capacity
		self._head = 0
		self._tail = 0

	def enqueue(self, item):
		"""入队操作
		"""
		# tail == capacity表示队列末尾没有空间了
		if self._tail == self._capacity:
			# tail == capacity && head==0表示整个队列都占满了
			if self._head == 0:
				return False
			else:
				# 执行数据搬移操作
				for i in range(0, self._tail - self._head):
					self._items[i] = self._items[i + self._head]
				# 更新head和tail
				self._tail = self._tail - self._head
				self._head = 0
		self._items.insert(self._tail, item)
		self._tail += 1
		return True

	def dequeue(self):
		# 出队操作dequeue()的队空的条件是队头下标等于队尾下标。
		if self._head != self._tail:
			item = self._items[self._head]
			self._head += 1
			return item
		else:
			return None

	def __repr__(self):
		return " ".join("%s" % item for item in self._items[self._head : self._tail])


class ListQueue(object):
	"""使用List数据结构实现的简单版队列"""
	def __init__(self, n):
		self._items = []

	def enqueue(self, item):
		"""入队"""
		self._items.insert(0, item)

	def dequeue(self):
		"""出队"""
		# 队头在右边，因此pop()即为弹出队头
		return self._items.pop()
	def __repr__(self):
		return " ".join("%s" % i for i in self._items)

def test_ArrayQueue():
	queue = ArrayQueue(10)
	queue.enqueue(1)
	queue.enqueue(2)
	print queue
