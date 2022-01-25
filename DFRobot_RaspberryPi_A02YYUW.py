# -*- coding:utf-8 -*-

'''!
  @file DFRobot_RaspberryPi_A02YYUW.py
  @brief Ranging distance sensor。
  @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author      Arya(xue.peng@dfrobot.com)
  @version     V1.0
  @date        2021-08-30
  @url https://github.com/DFRobot/DFRobot_RaspberryPi_A02YYUW
'''

import serial

import time

class DFRobot_A02_Distance:

  ## Board status 
  STA_OK = 0x00
  STA_ERR_CHECKSUM = 0x01
  STA_ERR_SERIAL = 0x02
  STA_ERR_CHECK_OUT_LIMIT = 0x03
  STA_ERR_CHECK_LOW_LIMIT = 0x04
  STA_ERR_DATA = 0x05

  ## last operate status, users can use this variable to determine the result of a function call. 
  last_operate_status = STA_OK

  ## variable 
  distance = 0

  ## Maximum range
  distance_max = 4500
  distance_min = 0
  range_max = 4500

  def __init__(self):
    '''
      @brief    Sensor initialization.
    '''
    self._ser = serial.Serial("/dev/ttyAMA0", 9600)
    if self._ser.isOpen() != True:
      self.last_operate_status = self.STA_ERR_SERIAL

  def set_dis_range(self, min, max):
    self.distance_max = max
    self.distance_min = min

  def getDistance(self):
    '''
      @brief    Get measured distance
      @return    measured distance
    '''
    self._measure()
    return self.distance
  
  def _check_sum(self, l):
    return (l[0] + l[1] + l[2])&0x00ff

  def _measure(self):
    data = []
    i = 0
    timenow = time.time()
    while self._ser.inWaiting() == 0:
      i += 1
      time.sleep(0.05)
      if i > 4:
        break
    i = 0
    while self._ser.inWaiting() > 0:
      rlt = self._ser.read()
      try:
        data.append(ord(rlt))
      except:
        data.append(rlt[0])
      i += 1
      if data[0] != 0xff:
        i = 0
        data = []
      if i == 4:
        break
    #self._ser.read(self._ser.inWaiting()) 
    if i == 4:
      sum = self._check_sum(data)
      if sum != data[3]:
        self.last_operate_status = self.STA_ERR_CHECKSUM
      else:
        self.distance = data[1]*256 + data[2]
        self.last_operate_status = self.STA_OK
      if self.distance > self.distance_max:
        self.last_operate_status = self.STA_ERR_CHECK_OUT_LIMIT
        self.distance = self.distance_max
      elif self.distance < self.distance_min:
        self.last_operate_status = self.STA_ERR_CHECK_LOW_LIMIT
        self.distance = self.distance_min
    else:
      self.last_operate_status = self.STA_ERR_DATA

