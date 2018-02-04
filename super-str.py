class SuperStr(str):
	def __init__(self, s):
		self.s = s

	def is_repeatance(self, some):
		res1 = False
		if not isinstance(some, str) or self == "":
			res1 = False
		else:
			self_len = len(self)
			s_len = len(some)
			times = int(self_len / s_len)
			if self == some * times:
				res1 = True
		return res1
	

	def is_palindrom(self):
		res = False
		s = self.s.lower()
		if s == "":
			res = True
		count = 0
		for i in s:
			count += 1
			len_s = len(s)
			if i == s[-count]:
				res = True
				continue
			else:
				res = False
				break
		return res

s0 = SuperStr("")
print(s0.is_repeatance("a"))
print(s0.is_palindrom())
print(s0)