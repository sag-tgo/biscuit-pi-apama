# Class that we want to invoke methods on by name
class MockBrickPi:
	def testOneParam(self, arg):
		return arg

	def testArgs(self, *args):
		return args

	def get42(self):
		return 42

	def getList(self):
		return [self.get42()]

	def add(self, x, y):
		return x + y


# Class to test invoking methods by name on a MockBrickPi instance.
class TestClass:
	# These Map method names onto bound methods of MockBrickPi 
	callables = {}
	restricted = {}

	def __init__(self):
		self.mbp = MockBrickPi()

		# Establish the methods can be called by name via doBPMethod
		for m in dir(self.mbp):
			method = getattr(self.mbp, m, None)	
			if method and callable(method):
				if not m.endswith('__'):
					self.callables[m]=method
				else:
					self.restricted[m]=method
		
		# Print available method names for this object (filtering out 'magic' objects)
		print("Available method names: " + ", ".join(self.callables.keys()))

	def doBPMethod(self, methodname, *args):
		if methodname in self.callables:
			return self.callables[methodname](*args)
		elif methodname in self.restricted:
			raise Exception("Method name not permitted: " + methodname)
		else:
			raise Exception("Unknown method name: " + methodname)


# Create an instance of TestClass and try invoking MockBrickPi methods by name.
o = TestClass()
methodTuples = [
	("testOneParam", [None]),
	("get42", []),
	("getList", []),
	("testOneParam", [1]),
	("testOneParam", ["Alan!"]),
	("testOneParam", [[1, 2, 3]]),
	("testOneParam", [{"sky": "blue"}]),
	("testArgs", [["one", 2]]),
	("add", [2, 2]),
	# Expected errors:
	("blah", [None]),  # Unknown method name: blah
	("__init__", [None]),  # Method name not permitted: __init__
	("get42", ["nope!"])  # takes 1 positional argument but 2 were given
]
# For each method and args pair, invoke that method and print out methodName(params) = result
for methodName, args in methodTuples:
	try:
		message = f'{methodName}({args})'
		result = o.doBPMethod(methodName, *args)
		message = message + f' = {result}'
		print(message)
	except Exception as e:
		print("ERROR:", e)
