def super_fibonacci(n,m):
	fibonacci_list=[]
	for step in range(m):
	    fibonacci_list.append(1)
	for j in range(n+1):
	    last_element = 0
	    for i in range(m):
	        last_element+=fibonacci_list[i+j]
	    fibonacci_list.append(last_element)
	return(fibonacci_list[n-1])

print(super_fibonacci(9, 3))