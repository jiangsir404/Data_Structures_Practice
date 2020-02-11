#!/usr/bin/env python		
#coding:utf-8

"""
224. 基本计算器

https://leetcode-cn.com/problems/basic-calculator/
"""

class Solution(object):
	def calculate(self, s):
		"""
		:type s: str
		:rtype: int

		思路:
		通过两个栈来实现，一个保存运算符的栈，另一个保存操作数的栈。从左到右遍历表达式，
		遇到操作数，就压入操作数栈，遇到运算符，就与运算符栈的栈顶元素进行比较:
			1. 如果比运算符栈顶元素的优先级高，就将当前运算符压入栈
			2. 如果比运算符栈顶元素的优先级低或者相同，从运算符栈中取栈顶运算符，从操作数栈顶取2个操作符，然后计算后把计算结果压入操作数栈，继续比较。
					
		"""
		operator = []
		nums = []
		operator_dic = {'+': 0, '-': 1, '*': 3, '/': 2} #运算符的优先级
		switch = {
			"+": lambda x, y:int(x) + int(y),
			"-": lambda x, y:int(x) - int(y),
			"*": lambda x, y:int(x) * int(y),
			"/": lambda x, y:int(x) / int(y),
		}
		brances_dic = {'}': '{', ']':'[', ')':'('}

		for c, i in enumerate(s):
			if i.isdigit():
				j = i
				while True:			
					print 'test',c, operator, nums	
					c = c -1 

					if c == -1 or not s[c].isdigit():
						nums.append(j)
						break
					if s[c].isdigit():
						
						j =  nums.pop() + j
						nums.append(j)

			elif i in ['(','{','[']:
				nums.append(i)
			elif i == " ":
				continue
			else:
				if not operator and i in operator_dic:
					operator.append(i)
				elif i in brances_dic:
					while True:
						num1 = nums.pop()
						if num1 in ['(','{','[']:
							break
						num2 = nums.pop()
						if num2 in ['(','{','[']:
							nums.append(num1)
							break
						else:
							op = operator.pop()
							op_res = switch[op](num2, num1)
							print 'debug', op_res
							nums.append(str(op_res))
							#assert nums.pop() in ['(','{','[']

				elif operator_dic[i] >= operator_dic[operator[-1]]:
					operator.append(i)
				elif operator_dic[i] < operator_dic[operator[-1]]:
					op = operator.pop()
					num1, num2 = nums.pop(), nums.pop()
					op_res = switch[op](num2, num1)
					nums.append(str(op_res))
					operator.append(i)
			print i, operator, nums
		if len(nums) ==2 and operator:
			op = operator.pop()
			num1, num2 = nums.pop(), nums.pop()
			op_res = switch[op](num2, num1)
			nums.append(str(op_res))
		return "".join(nums)



if __name__ == '__main__':
	s = Solution()
	string = "1213234"
	print s.calculate(string)