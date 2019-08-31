# A02YYUW for Pi 

This RaspberryPi expansion board can communicate with RaspberryPi via UART. <br>
This is a ranging sensor. <br>
Its' rang is 0 to 4500 mm <br>

To provide a Raspberry Pi library for DFRobot A02YYUW

## Table of Contents

* [Summary](#summary)
* [Feature](#feature)
* [Installation](#installation)
* [Methods](#methods)
* [Credits](#credits)

## Summary

Ranging sensor.

## Feature

1. Ranging range: 0~4500mm. <br>
2. Set the range of ranging. <br>
3. Get ranging distance. <br>

## Installation

This sensor should work with DFRobot_A02_Distance on RaspberryPi. <br>
Run the program:

```
$> python2 demo_get_distance.py
```

## Methods

```py

class DFRobot_A02_Distance:

  ''' Board status '''
  STA_OK = 0x00
  STA_ERR_CHECKSUM = 0x01
  STA_ERR_SERIAL = 0x02
  STA_ERR_CHECK_OUT_LIMIT = 0x03
  STA_ERR_CHECK_LOW_LIMIT = 0x04

  ''' last operate status, users can use this variable to determine the result of a function call. '''
  last_operate_status = STA_OK

  ''' variable '''
  distance = 0

  '''Maximum range'''
  distance_max = 4500
  distance_min = 0

  def __init__(self):
    '''
      @brief    Board init
    '''

  def check_sum(self, list):
    '''
      @brief    Ranging packet verification
      @param list: list    distance data
      @return Packet checksum
    '''

  set_dis_range(self, min, max):
    '''
      @brief    set distance range.
      @param min: int(0~4500)    Minimum threshold  min < max 
      @param max: int(0~4500)    Maximum threshold  min < max
    '''

  def measure(self):
    '''
      @brief    Start ranging
    '''

  def getDistance(self):
    '''
      @brief    Get measured distance
      @return    measured distance
    '''

```

## Credits

·author [Arya xue.peng@dfrobot.com]
