
class MockBrickPi:
	def testClassMethod(self, **kwargs):
		print("hello from testClassMethod")

	def testClassMethod2(self, **kwargs):
		print("hello from testClassMethod2")


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
				print('calling ' + methodname + ' with params ' + str(params))
				return method(params)
			else:
				print('calling ' + methodname + '()')
				return method()
		elif not isMethodNameSafe:
			raise Exception("Method name not permitted: " + methodname)
		else:
			raise Exception("Unknown method name: " + methodname)


o = TestClass()
o.doBPMethod("testClassMethod")
o.doBPMethod("testClassMethod2")
try:
	o.doBPMethod("blah")
except Exception as e:
	print(e)

try:
	o.doBPMethod("__init__")
except Exception as e:
	print(e)
