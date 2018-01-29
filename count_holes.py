def count_holes(n):
	hole = 0
	holes = 0
	n = str(n).strip("-") 

	if "." in n:
		return "ERROR"
	elif n.isdigit():
		n = int(n)
	else:
		return "ERROR"



	for num in str(n):
		num = int(num)
		if num == 4 or num == 6 or num == 9 or num == 0:
			hole = 1
		elif num == 8:
			hole = 2			
		else:
			hole = 0

		holes += hole

	return holes

print(count_holes(-8))
