#!/usr/bin/env python		
#coding:utf-8

"""
算法: 三数之和 
Desc: 给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意: 答案中不可以包含重复的三元组。

Examples:
	输入: [-1, 0, 1, 2, -1, -4]
	输出: 
		[
		  [-1, 0, 1],
		  [-1, -1, 2]
		]

"""

class Solution(object):
    def threeSum(self, nums):
        """自己写的算法
        Desc: 
        	1. 3重循环暴力解法
        	2. 每次循环只往后循环，不需要往前循环即可达到i,j,k互不相同的效果。
            3. 利用set的无序性对重复元素进行去重
        """
        rets = []
        value_duplicate = [] # 值去重数组，保存已经检测过的值序列
        for i in range(len(nums)):
        	for j in range(i+1, len(nums)):
        		for k in range(j+1, len(nums)):
        			if nums[i] + nums[j] + nums[k] == 0:
        				x = set([nums[i], nums[j], nums[k]])
        				if x not in value_duplicate: # 利用set的无序性对重复元素进行去重
	    					value_duplicate.append(x)
	    					rets.append([nums[i], nums[j], nums[k]])

        return rets

    def threeSum2(self, nums):
    	"""排序+双指针解法
		
		暴力法搜索为 O(N^3) 时间复杂度，我们可以将三数之和转换为两数之和等于第三数，每次固定一个数，移动另外两个指针找到两数之和等于第三数

		双指针法铺垫： 先将给定 nums 排序，复杂度为 O(NlogN).
		双指针法思路:
			1. 设置三个指针k,i,j = 0, k+1, len(nums)-1, 每次固定k, 移动i和j, 记录所有满足nums[k]=nums[i]+nums[j]的i和j组合
			2. 当k>0且nums[k] == nums[k-1], 则跳过该k, 因为结果num[k-1]以及记录过了
			3. 固定k时，移动i,j两端，计算s=nums[k]+nums[i]+nums[j] 移动规则如下
				- 当 s<0时，i+=1,且跳过重复的nums[i]
				- 当s>0时，j-=1,且跳过重复的nums[j]
				- 当s=0时，记录组合[k,i,j]到res,执行i+=1,j-=1,并且跳过所有重复的nums[i],nums[j]

		复杂度分析:
		时间复杂度 O(N^2)其中固定指针k循环复杂度 O(N)，双指针 i，j 复杂度 O(N)
		空间复杂度 O(1)：指针使用常数大小的额外空间。
    	"""
    	nums.sort()
    	res, k = [], 0
    	for k in range(0, len(nums)-2): 
    		if nums[k] > 0: break # nums[k] < nums[i] < nums[j]
    		if k > 0 and nums[k] == nums[k-1]: continue # skip the same nums[k]
    		i, j = k + 1, len(nums) - 1

    		while i < j: # doule pointer
    			s = nums[i] + nums[j] + nums[k]
    			if s < 0:
    				i += 1
    				while i < j and nums[i] == nums[i-1]: i += 1 # skip same nums[i]
    			if s > 0:
    				j -= 1
    				while i < j and nums[j] == nums[j+1]: j -= 1 # skip same nums[j]
    			if s == 0:
    				res.append([nums[k], nums[i], nums[j]])
    				i += 1
    				j -= 1
    				while i < j and nums[i] == nums[i-1]: i += 1 # skip same nums[i]
    				while i < j and nums[j] == nums[j+1]: j -= 1 # skip same nums[j]
    	return res








if __name__ == '__main__':
	s = Solution()
	nums = [-1,0,1,2,-1,-4]
	res = s.threeSum2(nums)
	print res
	nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
	res = s.threeSum2(nums)
	print res
