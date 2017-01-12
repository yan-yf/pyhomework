# -*- coding:utf-8 -*-
'''螺旋矩阵：给定一个m * n要素的矩阵。按照螺旋顺序，返回该矩阵的所有要素。'''
def func(li):
	lr = []
	n = 0
	for i in li:
		if n % 2 == 0:
			lr.extend(i)
		else:
			lr.extend(i[::-1])
		n += 1
	return lr

li = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
li = func(li)
print li