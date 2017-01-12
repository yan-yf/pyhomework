# -*- coding:utf-8 -*-
'''使用list实现队列，支持push(element), pop(), top()方法'''
class queue():
	def __init__(self):
		self.list = []
	def push(self,element):
		self.list.append(element)
	def pop(self):
		print self.list[0]
		del(self.list[0])
	def top(self):
		print self.list[0]

q = queue()
q.push(1)
q.pop()
q.push(2)
q.push(3)
q.top()
q.pop()