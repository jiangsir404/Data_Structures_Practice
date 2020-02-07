#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-27 16:41:55
# @Author  : 江sir (2461805286@qq.com)
# @Link    : http://www.blogsir.com.cn
# @Version : v1.0

import sys
import argparse

# 归并排序
def merge_sort(ary):
	if len(ary) <= 1:return ary 
	num = int(len(ary)/2)
	left = merge_sort(ary[:num])#对左半边递归
	right = merge_sort(ary[num:]) #对右半边递归
	print 'left:',left ,'right:',right,'result:',
	return merge(left,right)

def merge(left,right):
	'''
		合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
	l,r = 0,0
	result = []
	while l<len(left) and r<len(right):
		if left[l] < right[r]:
			result.append(left[l])
			l += 1
		else:
			result.append(right[r])
			r += 1
	# print result
	result += left[l:]
	result += right[r:]
	print result
	return result


# 快速排序

def quick_sort(ary):
	return qsort(ary,0,len(ary)-1)

def qsort(ary,left,right):
	#快排函数,ary为待排序数组，left为待排序的左边界，right为右边界
	if left >= right:return ary 
	key = ary[left] 
	lp = left 
	rp = right 
	while lp < rp:
		while ary[rp] > key:
			rp -= 1
		ary[lp],ary[rp] = ary[rp],ary[lp]
		while ary[lp] < key:
			lp += 1
		ary[lp],ary[rp] = ary[rp],ary[lp]
	print 'key:',key,'left:',str(left)+'~'+str(lp),'right:',str(rp+1)+'~'+str(right),ary
	qsort(ary,left,lp-1)
	qsort(ary,rp+1,right)
	
	return ary

#冒泡排序
def bubble_sort(ary):
	bound = len(ary)-1#bound 不是长度，是下标的范围
	while bound > 1:
		last_index = 1
		for j in range(bound):
			if ary[j+1] < ary[j]:#冒泡排序是和前一位比较
				ary[j+1],ary[j] = ary[j],ary[j+1]
				last_index = j
				print j,

		bound = last_index
		print 'bound:',bound,
		print ary
	return ary

#插入排序
def insert_sort(ary):
	n = len(ary)
	for i in range(1,n):
		if ary[i] < ary[i-1]:#存在逆序对,选择排序是和前一位比较
			tmp = ary[i]
			index = i 
			for j in range(i-1,-1,-1):
				if ary[j] > tmp: #存在逆序对
					ary[j+1] = ary[j]
					index = j
				else:
					break
			ary[index] = tmp 
		print 'i:',i,ary
	return ary


#堆排序算法
def heap_sort(ary):
	n = len(ary)
	first = int(n/2-1) #最后一个非叶子节点
	print '构造最大堆:'
	for start in range(first,-1,-1):		
		max_heapify(ary,start,n-1)
	print '堆排序:'
	for end in range(n-1,0,-1):		
		ary[end],ary[0] = ary[0],ary[end]#每次将根节点和最后一个元素交换后再次调整大根堆
		max_heapify(ary,0,end-1)
	return ary 

def max_heapify(ary,start,end):
	root = start 
	while True:
		child = root*2 + 1 #注意root是从0下标开始的,因此加一是左孩子
		if child>end:break 
		if child + 1<=end and ary[child]<ary[child+1]:
			child = child +1 #取较大的字节点
		if ary[root]<ary[child]: #较大的字节点成为父节点
			ary[root],ary[child] = ary[child],ary[root]
			root = child 
		else:
			break 
	print 'start~-end:',str(start)+'~'+str(end),ary





if __name__ == '__main__':
	ary = [1,5,3,4,2,6,8,9,7]
	# help='ms:merge_sort,qs:quick_sort,bs:bubble_sort,is:insert_sort,hs:heap_sort'
	sort = sys.argv[-1]
	sort = "ms"
	if sort == 'ms':
		print merge_sort(ary)
	elif sort == 'qs':
		print quick_sort(ary)
	elif sort == 'bs':
		bubble_sort(ary)
	elif sort == 'is':
		insert_sort(ary)
	elif sort == 'hs':
		heap_sort(ary)
	else:
		print 'usage %s [ms|qs|bs|is|hs]'%sys.argv[0]

