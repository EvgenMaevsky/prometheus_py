class Human:
	name = None
	sex = None
	birth_year = None

	def get_age(self):
		if type(self.birth_year) == int:
			return 2017 - self.birth_year
		return None

class Student:
	pass

vova = Human()

vova.birth_year = 1986
age = vova.get_age()
print(age)

vova.name = "Vladimir"

print(vova.name)