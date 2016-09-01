class Cat:
	def __init__(self, name):
		self.name = name
	
	def meow(self):
		print(self.name + ' Meow!')
		
	def __str__(self):
		return 'Cat: ' + self.name
		
cat1 = Cat('Kelly')
cat1.meow()

cat2 = Cat('Tom')
cat2.meow()

print(cat1)
print(cat2)
