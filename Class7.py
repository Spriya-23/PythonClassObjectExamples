class A:
	__x = 12
	y = None
	def _init_(obj,x,y):
		obj.__x = x
		obj.y = y
	
	def _printx(obj):
		print(obj.__x)
	
	def printy(obj):
		print(obj.y)
	
class B(A):
	def _init_(obj,a,b):
		obj.__x = a
		obj.y = b

bobj = B(1,2)
bobj._printx()
bobj.printy()
