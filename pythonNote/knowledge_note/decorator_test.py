def sayHello():
	print("---hello---")

def sayMore(sayHello):
	def say():
		sayHello()
		print("---my name is jeff---")
	return say

sayHello = sayMore(sayHello)
sayHello()
