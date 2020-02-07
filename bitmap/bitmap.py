#!/usr/bin/env python		
#coding:utf-8

"""
python实现BitMap数据结构
"""

class BitMap1():
	"""使用列表实现的bitmap位图功能, 不节省空间，只为了直观展示理解用途"""
	def __init__(self, nbits):
		self.nbits = nbits
		self.bytes = [0] * (nbits + 1)

	def set(self, k):
		if k > self.nbits:
			return
		self.bytes[k] = self.bytes[k] | 1

	def get(self, k):
		if k > self.nbits:return false;
		res = self.bytes[k] & 1 != 0
		return res

class BitMap2():
	"""将数据存储有符号整数的前31位上面(兼容其他语言的整数最大表示大小，python已经不限制了)"""
	def __init__(self, m):
		"""
		:param m: max size
		"""
		self.max_size = m
		self.array = [0] * int((m + 31 -1) / 31) #多个整数来表示，防止大小不够

	def bit_index(self, k):
		"""获取第k个位置位索引下标
		"""
		return k % 31

	def set(self, k):
		"""设置第k个索引位置为1
		"""
		if k > self.max_size: return
		array_index = k // 31 # 获取数组索引，即第k的位置落在数组第几个元素上
		bit_index = self.bit_index(k) # 获取位索引
		self.array[array_index] = self.array[array_index] | (1 << bit_index)

	def get(self, k):
		"""验证第k的索引位置是否为1
		"""
		if k > self.max_size: return false
		array_index = k // 31
		bit_index = self.bit_index(k)
		return self.array[array_index] & (1 << bit_index) != 0 


def test_bitmap1():
	bit_map = BitMap1(100)
	bit_map.set(5)
	print bit_map.bytes
	print bit_map.get(5)
	print bit_map.get(4)

def test_bitmap2():
	bit_map = BitMap2(128)
	# 存储字符串
	string1 = "http://www.baidu.com"
	for c in string1:
		bit_map.set(ord(c))
	print bit_map.array

	# 验证字符串
	string2 = "https://www.baidu.com"
	flag = True
	for c in string2:
		flag = flag & bit_map.get(ord(c))
	if flag:
		print True
	else:
		print False


if __name__ == '__main__':
	test_bitmap2()
