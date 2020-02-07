#!/usr/bin/env python		
#coding:utf-8

"""
算法：移动零
Desc: 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
Example:
	输入: [0,1,0,3,12]
	输出: [1,3,12,0,0]
要求:
	1. 必须在原数组上操作，不能拷贝额外的数组。
	2. 尽量减少操作次数。

Referer:
- leetcode中文版: https://leetcode-cn.com/problems/move-zeroes/
- leetcode国际版: https://leetcode.com/problems/move-zeroes/
- 极客时间视频讲解: https://u.geekbang.org/lesson/7?article=159526
"""

class Solution(object):
    def moveZeroes(self, nums):
        """快慢双指针法
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        Desc: 再数组内创建一个指向下一个非零元素的索引来实现，整个过程时间复杂度为O(n)
        """
        nextNoneZeroIndex = 0 # 下一个非零元素的索引
        for i in range(len(nums)):
        	if nums[i] != 0:
        		nums[nextNoneZeroIndex] = nums[i]
	        	if i != nextNoneZeroIndex: 
	        		nums[i] = 0 
	        	nextNoneZeroIndex += 1 # 指向下一个非零元素

    def moveZeroes2(self, nums):
        """
        Desc: 第一次遇到非零元素，将非零元素与数组nums[0]互换，第二次遇到非零元素，将非零元素与nums[1]互换，第三次遇到非零元素，将非零元素与nums[2]，以此类推，直到遍历完数组
        """
        nextNoneZeroIndex = 0 # 下一个非零元素的索引
        for i in range(len(nums)):
        	if nums[i] != 0:
        		nums[nextNoneZeroIndex], nums[i] = nums[i], nums[nextNoneZeroIndex]
        		nextNoneZeroIndex += 1
        

    def moveZeroes3(self, nums):
    	"""
    	Desc: 1.遍历整个数组 2. 遇0删除并再在列表最后添加0
    	该方法时间复杂度为O(n^2), 因为nums.remove(0)的操作是O(n)时间复杂度
    	"""
        for i in nums[:]:
            if i==0:
                nums.append(0)
                nums.remove(0)

if __name__ == '__main__':
	s = Solution()
	nums = [0,1,0,3,12]
	s.moveZeroes3(nums)
	print nums
