class Student:
	name=""
	age=0
	sub=[]
	def __init__(self,x,y,l):
		self.name=x
		self.age=y
		self.sub=l
	def accept(self):
		self.name=input("Enter name: ")
		self.age=input("Enter age: ")
		s=input("Enter subjects: ")
		lis = s.split(" ")
		x=[]
		for some in lis:
			x.append(some)
		self.sub=x
	def display(self):
		print("Name: ",self.name)
		print("Age: ",self.age)
		print("Subjects: ",self.sub)

s1 = Student("asdd",21,["abc","def","ghi"])
s1.display()
s2 = Student("asdad",21,["abc","def","ghi"])
s2.accept()
s2.display()