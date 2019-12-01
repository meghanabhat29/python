class Person:
	def __init__(self,name,age): #constructor
		self.name=name
		self.age=age
p1=Person('Dumbledore',102)   #object instantiation
p2=Person('Snape',45)

print("The name of the first person is :",p1.name)
print("The age of the first person is ",p1.age)

print("The name of the first person is ",p2.name)
print("The age of the person is ",p2.age)

p2.age=10

print("The modified age of the person is ",p2.age)

del p1.age
print("The age attribute of {} has been deleted".format(p1.name))

del p1
print("The attributes of the first person have been removed")
#inner classes are possible here
