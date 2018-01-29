def counter(a ,b):
	a = str(a)
	b = str(b)
	count = 0
	new_b = []
	for i in b:
		if i not in new_b:
			new_b.append(i)
			if i in a:
				count += 1
	return count
print(counter(12345, 567))
print(counter(1233211, 12128))
print(counter(123, 45))