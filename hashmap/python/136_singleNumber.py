#!/usr/bin/env python		
#coding:utf-8

"""
136. 只出现一次的数字

https://leetcode-cn.com/problems/single-number/
"""

class Solution(object):
    def singleNumber(self, nums):
        """
        思路1： 使用哈希表，时间复杂度O(n), 空间复杂度O(n)

        :type nums: List[int]
        :rtype: int
        """
        nums_map = {}
        for i in nums:
            if i in nums_map:
                nums_map[i] += 1
            else:
                nums_map[i] = 1
        for key, value in nums_map.items():
            if value == 1:
                return key

    def singleNumber2(self, nums):
        """
        思路2： 使用异或， 时间复杂度O(n), 空间复杂度O(1)

        因为题目描述是某个元素出现一次，其他元素都出现两次，那么我们就可以让0和nums每个元素都异或一次，就会得到
        那个只出现一次的元素，因为相同元素的值异或为0.

        0 ^ i = i
        i ^ i = 0
        0 ^ j ^ i ^ i = j
        """
        i = 0
        for j in nums:
            i = i ^ j
        return i


if __name__ == '__main__':
    s = Solution()
    nums  = [2,2,1]
    print s.singleNumber2(nums)