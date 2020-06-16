from apama.eplplugin import EPLPluginBase,EPLAction
'''    
class CountPlugin(EPLPluginBase):
  def __init__(self, init):
    super(CountPlugin, self).__init__(init)
    self.count = 0
  @EPLAction("action<integer>", "increment") # override name
  def incrementCount(self, number):
    self.count = self.count + number
  @EPLAction("action<> returns integer")
  def getCount(self):
    return self.count
'''
import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

class SensorPlugin(EPLPluginBase):
  
  def __init__(self, init):
    super(SensorPlugin, self).__init__(init)
    
    
  @EPLAction("action<integer>", "") # override name
  def incrementCount(self, number):
    self.count = self.count + number
  
  @EPLAction("action<> returns integer")
  def getCount(self):
    return self.count