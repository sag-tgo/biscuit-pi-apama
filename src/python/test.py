
class MockBrickPi:
	def testClassMethod(self, **kwargs):
		print("hello from testClassMethod")

	def testClassMethod2(self, **kwargs):
		print("hello from testClassMethod2")

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

	def doBPMethod(self, methodname, params=None):
		isMethodNameSafe = not (methodname.startswith('__') or methodname.endswith('__'))
		isCallable = callable(getattr(self.mbp, methodname, False))
		if isMethodNameSafe and isCallable:
			method = getattr(self.mbp, methodname)

			if params:
				return method(params)
			else:
				return method()
		elif not isMethodNameSafe:
			raise Exception("Method name not permitted: " + methodname)
		else:
			raise Exception("Unknown method name: " + methodname)


o = TestClass()
methodTuples = [
	("testClassMethod", None),
	("testClassMethod2", None),
	("get42", None),
	("getList", None),
	# Expected errors:
	("blah", None),
	("__init__", None),
	("get42", "nope!")
]
for k, v in methodTuples:
	try:
		message = f'{k}({v})'
		result = o.doBPMethod(k, v)
		message = message + f' = {result}'
		print(message)
	except Exception as e:
		print("ERROR:", e)
