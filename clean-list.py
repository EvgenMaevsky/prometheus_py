import sys

my_list = ''.join(sys.argv[1:])
my_list = my_list.replace("[", "").replace("]", "").split(",")

def clean_list(some_list):
	new_list = []
	for i in some_list:
		if i not in new_list:
			new_list.append(i)	
	return new_list

print(clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5]))
