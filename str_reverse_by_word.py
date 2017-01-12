# -*- coding:utf-8 -*-
'''字符串按单词反转（必须保留所有空格）。\' I love china!   \'转化为\'\'   china! love I \''''
def reverse(strr, start, ends):
	while start < ends:
		strr[start], strr[ends] = strr[ends], strr[start]
		start += 1
		ends -= 1

strr = ' I love china!   '
strr_list = list(strr)
i = 0
while i < len(strr_list):
	if strr_list[i] != ' ':
		start = i
		end = start + 1
		while end < len(strr_list) and strr_list[end] != ' ':
			end += 1
		reverse(strr_list, start, end - 1)
		i = end
	else:
		i += 1
strr_list.reverse()
strr_result = ''.join(strr_list)
print strr_result