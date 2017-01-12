# -*- coding:utf-8 -*-
'''实现一个函数支持可变参数'''
def func(strr, *args, **dkv):
	print args
	print dkv

func('yan.yf', [1, 2, 3, 4], 66, 77, c1 = 'one', two = 2)
func('yyf', *(1, 2, 3, 4, [9, 8], [6, 7]), **{'c1': 1, 'c2': 2})

def func2(name, **dkv):
	print name
	print dkv

func2('yan.yf', china = 'BJ', UK = 'LD')