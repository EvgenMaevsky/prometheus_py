
path = [ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py']
some_file = 'hereiam.py'


def file_search(folder, filename):
	result = False
	path = folder[0]
	if filename in folder:
		result = path + '/' + filename
	else:
		for item in folder[1:]:
		  if type(item) == list:
		    item[0] = folder[0] + '/' + item[0]
		    result = result or file_search(item, filename) # Результат нам не цікавий???
	return result 		

print(file_search(path, some_file))
