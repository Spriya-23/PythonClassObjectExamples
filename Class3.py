class Employee:
	name = None
	ID = None
	HRA = None
	DA = None
	basic=None
	sal = None
	
	def _init_(obj,name,ID,basic):
		obj.name = name
		obj.ID = ID
		obj.basic=basic
		
	def calcSal(obj,hra,da):
		obj.HRA = obj.basic*hra/100
		obj.DA = obj.basic*da/100
		obj.sal=obj.HRA+obj.DA+obj.basic
	
	def printEmp(obj):
		print(obj.name)
		print(obj.ID)
		print(obj.HRA)
		print(obj.DA)
		print(obj.sal)
		
e1 = Employee("Priya",123,10000)
e1.calcSal(5,15)
e1.printEmp()
