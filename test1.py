import sys

text = sys.argv[1]

key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

text = text.replace(" ", "")
new_text = []
for i in text:
	if i.islower():
		new_text.append("a")
	else:
		new_text.append("b")
#text = "".join(new_text)

count = 5;

def group(iterable, count):
    """ Группировка элементов последовательности по count элементов """ 
    return zip(*[iter(iterable)] * count)
new_text = list(group(new_text, 5))
text = []

for i in new_text:
	i = "".join(i)
	text.append(i)
res = []
for i in text:
	found = key.find(i)
	if found > 0:
		res.append(alphabet[found])

print("".join(res))