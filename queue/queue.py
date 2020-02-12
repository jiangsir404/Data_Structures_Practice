#!/usr/bin/env python		
#coding:utf-8

"""
编写Queue模块的类的实现原理: 队列(Queue)，优先级队列(PriorityQueue)，先进后出队列(LifoQueue)
"""


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