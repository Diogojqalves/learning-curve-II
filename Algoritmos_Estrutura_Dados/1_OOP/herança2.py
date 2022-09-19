###########################
#Herança multipla avo
###########################

class Base(object):
	
	# Constructor
	def __init__(self, name):
		self.name = name

	# To get name
	def getName(self):
		return self.name


# Inherited or Sub class (Note Person in bracket)
class Filho(Base):
	
	# Constructor
	def __init__(self, name, age):
		Base.__init__(self, name)
		self.age = age

	# To get name
	def getAge(self):
		return self.age

# Inherited or Sub class (Note Person in bracket)
class Neto(Filho):
	
	# Constructor
	def __init__(self, name, age, address):
		Filho.__init__(self, name, age)
		self.address = address

	# To get address
	def getAddress(self):
		return self.address	

# get Age é do constutor
# estudante
g = Neto("Ricardo", 23, "Maia")
print(g.getName(), g.getAge(), g.getAddress())