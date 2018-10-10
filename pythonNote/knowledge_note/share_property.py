class Borg(object):
	_state = {"a":1}
	def __new__(cls):
		ob = object.__new__(cls)  # ob = super(Borg,cls).__new__(cls)
		ob.__dict__ = cls._state
		return ob

b = Borg()
c = Borg()
print(b.a,c.a)
