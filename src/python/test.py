
class MockBrickPi:
	def testOneParam(self, arg):
		return arg

	def testArgs(self, *args):
		return args

	def testKwArgs(self, **kwargs):
		return kwargs

	def get42(self):
		return 42

	def getList(self):
		return [self.get42()]

	def add(self, x, y):
		return x + y


class TestClass:
	def __init__(self):
		self.mbp = MockBrickPi()
		methodNames = [m for m in dir(self.mbp) if not m.endswith('__')]
		print("Available method names: " + ", ".join(methodNames))

	def doBPMethod(self, methodname, *args):
		isMethodNameSafe = not (methodname.startswith('__') or methodname.endswith('__'))
		isCallable = callable(getattr(self.mbp, methodname, False))
		if isMethodNameSafe and isCallable:
			method = getattr(self.mbp, methodname)

			if args:
				return method(*args)
			else:
				return method()
		elif not isMethodNameSafe:
			raise Exception("Method name not permitted: " + methodname)
		else:
			raise Exception("Unknown method name: " + methodname)


o = TestClass()
methodTuples = [
	("testOneParam", [None]),
	("get42", [None]),
	("getList", [None]),
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
for k, v in methodTuples:
	try:
		message = f'{k}({v})'
		result = o.doBPMethod(k, *v)
		message = message + f' = {result}'
		print(message)
	except Exception as e:
		print("ERROR:", e)
