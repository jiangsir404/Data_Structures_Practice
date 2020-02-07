#!/usr/bin/env python		
#coding:utf-8

"""
示例代码
"""


def binary_search1(sorted_array, val):
	"""二分查找， 使用left <= right作为循环进行的条件
	"""
	if not sorted_array:
	    return -1

	left, right = 0, len(sorted_array) - 1

	while left <= right:
	    mid = (left + right) // 2  # left + (right-left)/2， 为了屏蔽 python 2/3 差异我用了强转
	    if sorted_array[mid] == val:
	        return mid
	    elif sorted_array[mid] > val:
	        right = mid - 1
	    else:
	        left = mid + 1
	return -1


def test_binary_search1():
    a = list(range(10))

    # 正常值
    assert binary_search1(a, 1) == 1
    assert binary_search1(a, -1) == -1

    # 异常值
    assert binary_search1(None, 1) == -1

    # 边界值
    assert binary_search1(a, 0) == 0

def binary_search2(nums, val):
	"""二分查找, 使用left < right作为循环进行的条件
	"""
	# 特例判断
	if not nums or val not in nums:
		return -1
	left, right = 0, len(nums) - 1
	while left < right:
		mid = (left + right) // 2
		if nums[mid] < val:
			left = mid + 1
		else:
			right = mid
	return left

def test_binary_search2():
    a = list(range(10))

    # 正常值
    assert binary_search2(a, 1) == 1
    assert binary_search2(a, -1) == -1

    # 异常值
    assert binary_search2(None, 1) == -1

    # 边界值
    assert binary_search2(a, 0) == 0

    a = [5,7,7,8,8,10]
    print binary_search1(a, 8)
    print binary_search2(a, 8)


if __name__ == '__main__':
	test_binary_search1()
	test_binary_search2()