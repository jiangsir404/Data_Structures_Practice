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

from collections import deque
import heapq
class Queue(object):
	"""使用deque双端队列的数据结构实现的队列"""
	def __init__(self, maxsize=0):
		self.queue = deque()
	def put(self, item):
		"""入队"""
		self.queue.append(item)
	def get(self):
		"""出队"""
		return self.queue.popleft()
	def qsize(self):
		return len(self.queue)

class PriorityQueue(object):
	"""优先级队列"""
	def __init__(self, maxsize=0):
		self.queue = []
	def put(self, item, heappush=heapq.heappush):
		"""入队"""
		heappush(self.queue, item)
	def get(self, heappop=heapq.heappop):
		"""出队，每次返回最小的元素"""
		return heappop(self.queue)
	def __repr__(self):
		return " ".join("%s" % i for i in self.queue)

class LifoQueue(object):
    '''Variant of Queue that retrieves most recently added entries first.'''

    def _init(self, maxsize=0):
        self.queue = []

    def _qsize(self, len=len):
        return len(self.queue)

    def _put(self, item):
        self.queue.append(item)

    def _get(self):
        return self.queue.pop()


def test_Queue():
	"""测试Queue, PriorityQueue, LifoQueue"""
	q1 = Queue()
	q1.put(1)
	q1.put(2)
	assert q1.qsize() ==2 and q1.get() == 1

	# 测试PriorityQueue
	q2 = PriorityQueue()
	q2.put(1),q2.put(5),q2.put(4),q2.put(2),q2.put(3)
	print 'q2:',q2
	assert q2.get() == 1 and q2.get()== 2 and  q2.get() == 3



if __name__ == '__main__':
	test_Queue()