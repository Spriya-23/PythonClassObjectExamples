class Vehicle:
	name=None
	brand=None
	noofwheels=None
	def _init_(obj,name,brand,noofwheels):
		obj.name=name
		obj.brand=brand
		obj.noofwheels=noofwheels
		
	def doesusefuel(obj,type):
		if(type == "fuel"):
			return True
		else:
			return False

class car(Vehicle):
			gear=None
			fueldetail=None
			def _init_(obj,name,brand,noofwheels,gear,fueldetail):
				obj.name=name
				obj.brand=brand
				obj.noofwheels=4
				obj.gear=gear
				obj.fueldetail=fueldetail
			
			def printCar(obj):
				print("Name",obj.name)
				print("Brand",obj.brand)
				print("No of Wheels",obj.noofwheels)
				print("Does Use Fuel",obj.doesusefuel(obj.fueldetail))
				print("Gear Available",obj.gear)
			

obj1= car("M5","Maruthi",4,True,"fuel")
obj1.printCar()


obj2=car("Alcazar","Hyundai",4,True,"fuel")
obj2.printCar()

obj3=car("MEz", "MIG",4,True,"electric")
obj3.printCar()
