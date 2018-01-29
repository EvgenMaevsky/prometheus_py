https://github.com/mebius01/prometheus/blob/master/job-6-modul.py
def convert_n_m_m(x, n, m):
	import math
	x=str(x);x=x.upper(); ret_string=''
	def convert_in_10(x, y): # конвертирует из 2-9 в 10-чную
		x=str(x); z=1
		lett={'0':0, '1':1, '2':2, '3':3, '4':4, 
			'5':5, '6':6, '7':7, '8':8, '9':9, 
			'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 
			'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 
			'K':20, 'L':21, 'M':22, 'N':23, 'O':24, 
			'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 
			'U':30, 'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35}
		rec=(int(lett.get((x[0]))))
		while z < len(x):
			rec=(rec*y+(int(lett.get((x[z])))))
			z+=1
		return rec

	def convert_from_10(x, y): # конвертирует из 10-чной в 2-9
		list_10=[]; fract=None; s=''
		lett={0:'0', 1:'1', 2:'2', 3:'3', 4:'4', 
			5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 
			10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 
			15:'F', 16:'G', 17:'H', 18:'I', 19:'J', 
			20:'K', 21:'L', 22:'M', 23:'N', 24:'O', 
			25:'P', 26:'Q', 27:'R', 28:'S', 29:'T', 
			30:'U', 31:'V', 32:'W', 33:'X', 34:'Y', 35:'Z'}
		def f(i, l):
			if i in l:
				return l.get(i)
		def u(f, d):
			return(int(round(f*d)))
		while x >= y:
			x=float(x)
			fract=math.modf(x/y)[0] 
			x=math.modf(x/y)[1] 
			list_10.append(f(u(fract, y), lett))
			if x < y:
				list_10.append(f(int(x), lett)); list_10.reverse()
		for i in list_10:
			s=s+i
		return s
	try:
		try:
			while (x[0]=='0'):
				x=x[1:]
		except IndexError:
			return '0'
		if x=='0': return '0'
		elif m == 1:
			for i in range(convert_in_10(x, n)):
				ret_string+='0'
			return ret_string
		elif n == m:
			return str(x)
		elif convert_from_10(convert_in_10(x, n), n) == str(x):
			return convert_from_10(convert_in_10(x, n), m)
		else:
			return False
	except TypeError:
		return False


print(convert_n_m_m(123, 4, 1))