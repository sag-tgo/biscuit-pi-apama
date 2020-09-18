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
	def __init__(self):
		self.mbp = MockBrickPi()
		# Print available method names for this object (filtering out 'magic' objects)
		methodNames = [m for m in dir(self.mbp) if not m.endswith('__')]
		print("Available method names: " + ", ".join(methodNames))

	def doBPMethod(self, methodname, *args):
		isMethodNameSafe = not methodname.endswith('__')  # filter out 'magic' objects
		method = getattr(self.mbp, methodname, None)
		isCallable = callable(method)
		if isMethodNameSafe and isCallable:
			if args:
				return method(*args)
			else:
				return method()
		elif not isMethodNameSafe:
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
