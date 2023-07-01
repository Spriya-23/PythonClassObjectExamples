class A:
	__x = 10
	def _init_(obj,a):
		obj.__x=a
	
	def print(obj):
		print(obj.__x*10)

class B(A):
	def _init_(obj,a):
		super()._init_(a)

bobj = B(50)
bobj.print()
