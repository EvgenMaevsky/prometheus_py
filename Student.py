class Student(object):
	name = ""
	conf = { 'exam_max': None, 'lab_max': None, 'lab_num': None, 'k': None }
	exam = 0
	suma = 0

	def __init__(self, name, conf):
	    self.name = name
	    self.conf = conf
	    self.mark = []
	    for i in range(self.conf['lab_num']):
	        self.mark.append(0)
	def make_lab(self, m = 0, n = None):

	    if m > self.conf['lab_max']:
	        m = self.conf['lab_max']
	    if n == None:
	        n = self.mark.index(0)
	        self.mark[n] = m
	    elif n < self.conf['lab_num']:
	        self.mark[n] = m
	    return self

	def make_exam(self, m):
	    if m > self.conf['exam_max']:
	        m = self.conf['exam_max']
	    self.exam = m
	    return self
	def  is_certified(self):
	    self.suma = sum(self.mark) + self.exam
	    if (self.suma / (self.conf['exam_max'] + (self.conf['lab_max'] * self.conf['lab_num']))) >= self.conf['k']:
	        return (self.suma, True)
	    else:
	        return (self.suma, False)
		

#control
conf = {
 'exam_max': 30,
 'lab_max': 7,
 'lab_num': 10,
 'k': 0.61
 }

oleg = Student('Oleg', conf)

oleg.make_lab(1).\
make_lab(8,0).\
make_lab(1).\
make_lab(10,7).\
make_lab(4,1).\
make_lab(5).\
make_lab(6.5).\
make_exam(32)
print(oleg.is_certified()) # (59.5, False)

oleg.make_lab(7,1) # labs: 7 7 5 6.5 0 0 0 7 0 0, exam: 30
print(oleg.is_certified()) # (62.5, True)

conf1 = {'exam_max': 20,'lab_max': 40,'lab_num': 2,'k': 0.75}
o3 = Student('Oleg', conf1)
o3.make_lab(50,2)
print(o3.is_certified())