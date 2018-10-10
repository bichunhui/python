class SingleCase(object):
	_instance = None
	def __new__(cls):
		if cls._instance == None:
			cls._instance = object.__new__(cls)
		return cls._instance

singleCase1 = SingleCase()
singleCase2 = SingleCase()
print(id(singleCase1),"---",id(singleCase2))
