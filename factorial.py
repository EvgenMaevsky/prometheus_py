import sys

def factorial(n):
	if n > 0:
		return n * factorial(n - 1)
	else:
		return 1
n = int(sys.argv[1])


print(factorial(n))