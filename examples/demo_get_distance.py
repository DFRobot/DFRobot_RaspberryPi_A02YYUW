# -*- coding:utf-8 -*-

'''!
  @file demo_get_distance.py
  @brief Get ranging data.
  @n Connect board with raspberryPi.
  @n --------------------------------------------
  @n sensor pin |         raspberry pi          |
  @n     VCC    |            5V/3V3             |
  @n     GND    |             GND               |
  @n     RX     |          (BCM)14 TX           |
  @n     TX     |          (BCM)15 RX           |
  @n --------------------------------------------
  @n
  @Copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
  @license     The MIT License (MIT)
  @author [Arya](xue.peng@dfrobot.com)
  @version  V1.0
  @date  2019-8-31
  @url https://github.com/DFRobot/DFRobot_RaspberryPi_A02YYUW
'''

import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from DFRobot_RaspberryPi_A02YYUW import DFRobot_A02_Distance as Board

board = Board()

def print_distance(dis):
  if board.last_operate_status == board.STA_OK:
    print("Distance %d mm" %dis)
  elif board.last_operate_status == board.STA_ERR_CHECKSUM:
    print("ERROR")
  elif board.last_operate_status == board.STA_ERR_SERIAL:
    print("Serial open failed!")
  elif board.last_operate_status == board.STA_ERR_CHECK_OUT_LIMIT:
    print("Above the upper limit: %d" %dis)
  elif board.last_operate_status == board.STA_ERR_CHECK_LOW_LIMIT:
    print("Below the lower limit: %d" %dis)
  elif board.last_operate_status == board.STA_ERR_DATA:
    print("No data!")

if __name__ == "__main__":
  #Minimum ranging threshold: 0mm
  dis_min = 0 
  #Highest ranging threshold: 4500mm  
  dis_max = 4500 
  board.set_dis_range(dis_min, dis_max)
  while True:
    distance = board.getDistance()
    print_distance(distance)
    #Delay time < 0.6s
    time.sleep(0.3) 
