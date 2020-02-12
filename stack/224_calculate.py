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
					
		bug: "(5-(1+(5)))" 输入会报错
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
				# print 'test',c, 
				if c > 0 and s[c-1].isdigit() and nums:
					j = nums.pop() + j
					nums.append(j)
				else:
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
		while len(nums) >= 2 and operator:
			op = operator.pop()
			num1, num2 = nums.pop(), nums.pop()
			op_res = switch[op](num2, num1)
			nums.append(str(op_res))
		return nums[0]


	def calculate2(self, s):
		"""解法2：因为该题只设计=,-两种运算，因此可以把他们当作正负号而不是运算符来处理，这样就只需要一个操作数栈即可。

		算法:
			1. 正序迭代字符串。
			2. 操作数可以由多个字符组成，字符串 "123" 表示数字 123，它可以被构造为：123 >> 120 + 3 >> 100 + 20 + 3。如果我们读取的字符是一个数字，则我们要将先前形成的操作数乘以 10 并于读取的数字相加，形成操作数。
			3. 每当我们遇到 + 或 - 运算符时，我们首先将表达式求值到左边，然后将正负符号保存到下一次求值。
			4. 如果字符是左括号 (，我们将迄今为止计算的结果和符号添加到栈上，然后重新开始进行计算，就像计算一个新的表达式一样。
			5. 如果字符是右括号 )，则首先计算左侧的表达式。则产生的结果就是刚刚结束的子表达式的结果。如果栈顶部有符号，则将此结果与符号相乘。
			
		"""
		stack = [] # 操作数栈
		operand = 0
		res = 0 #
		sign = 1 # 1表示正好+, -1表示符号-

		for ch in s:
			if ch.isdigit():
				# 构造操作数, 可能会进位
				operand = (operand * 10) + int(ch)
			elif ch == '+':
				res += sign * operand
				# 保存+符号
				sign = 1
				# 重置操作数
				operand = 0
			elif ch == '-':
				res += sign * operand
				sign = -1
				operand = 0
			elif ch == '(':
				# 依次将计算结果和符合入栈
				stack.append(res)
				stack.append(sign)
				# 充值sign和res
				sign = 1
				res = 0
			elif ch == ')':
				res += sign * operand
				res *= stack.pop() # *sign
				res += stack.pop() # +operand

				operand = 0
		return res + sign * operand

if __name__ == '__main__':
	s = Solution()
	string = "1+2-(44)"
	print s.calculate2(string)