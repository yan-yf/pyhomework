# -*- coding:utf-8 -*-
'''翻转单向链表'''
class ListNode:
	def __init__(self, val, next = None):
		self.val = val
		self.next = next

def disNode(head):
	vals = []
	while head:
		vals.append(str(head.val))
		head = head.next
	else:
		print '->'.join(vals)

def reverseNode(head):
	new_head = None
	while head:
		node = head
		head = head.next
		node.next = new_head
		new_head = node
	return new_head

l_5 = ListNode(5)
l_4 = ListNode(4, l_5)
l_3 = ListNode(3, l_4)
l_2 = ListNode(2, l_3)
l_1 = ListNode(1, l_2)
disNode(l_1)
disNode(reverseNode(l_1))