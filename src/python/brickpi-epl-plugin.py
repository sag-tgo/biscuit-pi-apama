# Copyright (c) 2020 Software AG, Darmstadt, Germany and/or its licensors
# 
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 
#   http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
#

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''
from apama.eplplugin import EPLPluginBase
from apama.eplplugin import EPLAction
import brickpi3 # import the BrickPi3 drivers


class BrickPiPlugin(EPLPluginBase):

    def __init__(self, init):
        super(BrickPiPlugin, self).__init__(init)
        self.getLogger().info("defining self.bp...")
        self.bp = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. bp will be the BrickPi3 object.
        self.getLogger().info(self.bp)

        # Configure sensor/port mappings
        TOUCH_SENSOR1_PORT = self.bp.PORT_3  # limit sensor
        TOUCH_SENSOR2_PORT = self.bp.PORT_4  # e-stop sensor
        GYRO_SENSOR_PORT = self.bp.PORT_2    # arm angle/height
        COLOUR_SENSOR_PORT = self.bp.PORT_1  # biscuit colour

        # Configure motor/port mappings
        MOTOR_ARM_GRABBER = self.bp.PORT_A
        MOTOR_ARM_VERTICAL = self.bp.PORT_B
        MOTOR_ARM_ROTATE   = self.bp.PORT_C

        # Configure BrickPi sensors
        self.bp.set_sensor_type(TOUCH_SENSOR1_PORT, self.bp.SENSOR_TYPE.EV3_TOUCH)
        self.bp.set_sensor_type(GYRO_SENSOR_PORT, self.bp.SENSOR_TYPE.EV3_GYRO_ABS_DPS)
        self.bp.set_sensor_type(COLOUR_SENSOR_PORT, self.bp.SENSOR_TYPE.EV3_COLOR_COLOR)

        # Configure BrickPi motors
        # TODO!

        color = ["?", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

        self.COLOUR_SENSOR_CHANNEL = "COLOUR_CHANNEL"

    @EPLAction("action<>")
    def testAction(self):
        self.getLogger().info("Hello from BrickPiPlugin!")

    @EPLAction("action<string, sequence<any>> returns any")
    def doBPMethod(self, methodname, args):
        return self.doBPMethodArgs(methodname, *args)

    def doBPMethodArgs(self, methodname, *args):
        self.getLogger().info(f"doBPMethod( {methodname}, {str(*args)} )")
        isMethodNameSafe = not methodname.endswith('__')  # filter out 'magic' objects
        method = getattr(self.bp, methodname, None)
        isCallable = callable(method)
        if isMethodNameSafe and isCallable:
            return method(*args)
        elif not isMethodNameSafe:
            raise Exception("Method name not permitted: " + methodname)
        else:
            raise Exception("Unknown method name: " + methodname)
