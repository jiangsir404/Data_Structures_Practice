#!/usr/bin/env python		
#coding:utf-8

"""
344. 反转字符串

https://leetcode-cn.com/problems/reverse-string/
https://leetcode-cn.com/problems/reverse-string/solution/fan-zhuan-zi-fu-chuan-by-leetcode/
"""

class Solution(object):
	def reverseString(self, s):
		"""python简要解法
		:type s: List[str]
		:rtype: None Do not return anything, modify s in-place instead.
		"""
		return s.reverse()

	def reverseString2(self, s):
		"""递归解法

		算法:我们实现递归函数 helper，它接受两个参数：left 左指针和 right 右指针。
			1. 如果 left>=right，不做任何操作。
			2. 否则交换 s[left] 和 s[right] 和调用 helper(left + 1, right - 1)。
			3. 首次调用函数我们传递首尾指针反转整个字符串 return helper(0, len(s) - 1)。
		
		时间复杂度: O(N), 执行了N/2次交换
		空间复杂度:O(N), 递归过程中使用了堆栈空间
		"""
		def helper(left, right):
			if left < right:
				s[left], s[right] = s[right], s[left]
				helper(left + 1, right - 1)
		helper(0, len(s) - 1)

	def reverseString3(self, s):
		"""双指针法
		
f		算法: 
			1. 将 left 指向首元素，right 指向尾元素。
			2. 当 left<right:
				- 交换 s[left] 和 s[right]。
				- left ++
				- right ++

		时间复杂度：O(N)。执行了 N/2N/2 次的交换。
		空间复杂度：O(1)，只使用了常数级空间。
		"""
		left, right = 0, len(s) - 1
		while left < right:
			s[left], s[right] = s[right], s[left]
			left += 1
			right -= 1
		return s



if __name__ == '__main__':
	s = Solution()
	string = ['H','e','l','l','o']
	print s.reverseString3(string)