class A:
	__x = None
	y = None
	def _init_(obj,x,y):
		obj.__x = x
		obj.y = y
	
	def __printx(obj):
		print(obj.__x)
	
	def printy(obj):
		print(obj.y)
	
class B(A):
	def _init_(obj,a,b):
		obj.__x = a
		obj.y = b

bobj = B(1,2)
bobj.__printx()
bobj.printy()
