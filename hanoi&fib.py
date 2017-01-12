def hanoi(n, A, B, C):
	if n == 1:
		print A, '->', B
	else:
		hanoi(n - 1, A, C, B)
		print A, '->', B
		hanoi(n - 1, C, B, A)
hanoi(5, 'A', 'B', 'C')

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n - 1) + fib (n - 2)

print fib(6)