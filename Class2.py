class demo2:
	name=None
	phone=None
	def _init_(obj, name,phone):
		obj.name=name
		obj.phone=phone
	
	def printDetails(obj):
		print("Name", obj.name)
		print("Phone",obj.phone)
	
obj1 = demo2("Priya",9884788356)
obj2 = demo2("Valli",123456)

obj1.printDetails()
obj2.printDetails()
