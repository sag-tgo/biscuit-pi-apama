#!/usr/bin/env python
#
# https://www.dexterindustries.com/BrickPi/
# https://github.com/DexterInd/BrickPi3
#
# Copyright (c) 2016 Dexter Industries
# Released under the MIT license (http://choosealicense.com/licenses/mit/).
# For more information, see https://github.com/DexterInd/BrickPi3/blob/master/LICENSE.md
#
# This code is an example for reading an EV3 color sensor connected to PORT_1 of the BrickPi3
# 
# Hardware: Connect an EV3 or NXT touch sensor to BrickPi3 Port 1.
# 
# Results:  When you run this program, you should see a 0 when the touch sensor is not pressed, and a 1 when the touch sensor is pressed.

from __future__ import print_function # use python 3 syntax but make it compatible with python 2
from __future__ import division       #                           ''
from apama.eplplugin import EPLPluginBase
from apama.eplplugin import EPLAction
from apama.eplplugin import Correlator

import time     # import the time library for the sleep function
import brickpi3 # import the BrickPi3 drivers

class BiscuitRobot(EPLPluginBase):

    def __init__(self):
        super(BiscuitRobot, self).__init__()
        self.bp = brickpi3.BrickPi3() # Create an instance of the BrickPi3 class. bp will be the BrickPi3 object.

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
        self.bp.set_sensor_type(TOUCH_SENSOR1_PORT, bp.SENSOR_TYPE.EV3_TOUCH)
        self.bp.set_sensor_type(GYRO_SENSOR_PORT, bp.SENSOR_TYPE.EV3_GYRO_ABS_DPS)
        self.bp.set_sensor_type(COLOUR_SENSOR_PORT, bp.SENSOR_TYPE.EV3_COLOR_COLOR)

        # Configure BrickPi motors
        # TODO!

        color = ["?", "Black", "Blue", "Green", "Yellow", "Red", "White", "Brown"]

        self.COLOUR_SENSOR_CHANNEL = "COLOUR_CHANNEL"

	@EPLAction("sortBiscuits", "action<>")
    def sortBiscuits(self):
        while True:
            colour = self.bp.get_sensor(self.COLOUR_SENSOR_PORT)
            Correlator.sendTo(self.COLOUR_SENSOR_CHANNEL, f'ColourSensorReading("{colour}")')
            time.sleep(0.02)
            # TODO: 
            # motor reading etc 






"""
    try:
        #bp.set_motor_position_relative(MOTOR_GRABBER_PORT, 45)
        #bp.set_motor_position_relative(MOTOR_ARM_ROTATE, -45)
        #bp.set_motor_position_relative(MOTOR_ARM_VERTICAL, 45)
        # todo print get position
        
        motor = MOTOR_ARM_ROTATE    
        print(bp.get_motor_status(motor))
    # print(bp.get_motor_status(MOTOR_ARM_VERTICAL))
        #print(bp.get_motor_status(MOTOR_GRABBER_PORT))
        
        #bp.set_motor_power(motor,100)
        
        bp.set_motor_dps(motor, -45)
        time.sleep(6.0)
        print(bp.get_motor_status(motor))
        bp.set_motor_dps(motor, 45)
        time.sleep(6.0)
        bp.set_motor_dps(motor, 0)
        print(bp.get_motor_status(motor))
        '''
        while True:    
                                
            try:
                touchSensor1Val = bp.get_sensor(TOUCH_SENSOR1_PORT)
                print(touchSensor1Val)
                    
                #touchSensor2Val = bp.get_sensor(TOUCH_SENSOR2_PORT)
                #print(touchSensor2Val)
                    
                gyroSensorVal = bp.get_sensor(GYRO_SENSOR_PORT)
                print(gyroSensorVal)
                    
                colourSensorVal = bp.get_sensor(COLOUR_SENSOR_PORT)
                print(color[colourSensorVal])
                    
                    
                    
            except brickpi3.SensorError as error:
                print(error)
                
            time.sleep(0.02)  # delay for 20ms to reduce the Raspberry Pi CPU load.
    '''
    except KeyboardInterrupt: # except the program gets interrupted by Ctrl+C on the keyboard.
        bp.reset_all()        # Unconfigure the sensors, disable the motors, and restore the LED to the control of the BrickPi3 firmware.
"""
