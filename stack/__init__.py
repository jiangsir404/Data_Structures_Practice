#!/usr/bin/env python        
#coding:utf-8

"""
    Stack based upon linked list
    基于链表实现的栈
    
    Author: Wenru
"""

class Node(object):
    def __init__(self, data, next=None):
        self._data = data
        self._next = next

class LinkedStack(object):
    """用链表实现的链式栈
    """
    def __init__(self):
        """只需要一个栈顶指针即可"""
        self._top = None

    def push(self, value):
        new_top = Node(value)
        new_top._next = self._top # 新元素指向栈下面一个元素
        self._top = new_top #就栈顶指针赋值给新的元素

    def pop(self):
        if self._top:
            value = self._top._data
            self._top = self._top._next # 栈往下移一位
            return value

    def __repr__(self):
        current = self._top
        nums = []
        while current:
            nums.append(current._data)
            current = current._next
        return " ".join("%s"% num for num in nums)

def test_linkedstack():
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(3):
        stack.pop()
    print(stack)

class ListStack(object):
    """使用List数据结构实现的顺序栈"""
    def __init__(self, ):
        self._items = []

    def push(self, value):
        """入栈"""
        self._items.append(value)

    def pop(self):
        """弹出栈顶元素"""
        if len(self._items) >0:
            return self._items.pop()
        else:
            return None

    def peek(self):
        """返回栈顶元素"""
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def __repr__(self):
        return " ".join("%s" % i for i in self._items)

def test_arraystack():
    stack = ListStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    for _ in range(10):
        print stack.pop()
    # print(stack)
    # print(stack.peek())

if __name__ == '__main__':
    #test_linkedstack()
    test_arraystack()

