#!/usr/bin/env python
# coding:utf-8
import time

import xlwt
import sys
import numpy as np
from numpy import ma
# sys.path.append('/opt/deeproute/control/lib/python2.7/dist-packages')
# sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
# import rospy
import rosbag
import matplotlib.pyplot as plt

# sys.path.append('/opt/deeproute/control/lib/control_common_tmp/')
import car_state_pb2
# import control_command_pb2
# import path_pb2
import car_info_pb2

import Bag_path

car_state = car_state_pb2.CarState()
# control_command = control_command_pb2.ControlCommand()
# path = path_pb2.Path()
car_info = car_info_pb2.CarInfo()
steer_report = car_info_pb2.SteerReport()

timestate = []
timeinfo = []
timegnss = []
drivingmode = []
gear = []
turnsignal = []
beam = []
throttle = []
brake = []
speed = []
acc = []
longitude = []
latitude = []

actual_bool = []
actual_angle = []

direction = []
# *********************************************************
# *********************************************************
# bag = rosbag.Bag('/home/dr/data/0712_test_chongqing/down1.bag')
bag = rosbag.Bag(Bag_path.pull_over_emergency_cq)
# fpath = '/home/chendong/data/0712_test_chongqing/excel/down1.xls'
fpath = '/home/dr/down1.xls'
WriteFilePath = '/home/dr/datasheet_cq_auto_driver_up/{0}.xls'.format(
    "pull_over_emergency_cq-" + time.strftime(Bag_path.TimeFormat, Bag_path.TimeLocal))

for topic, msg, t in bag.read_messages(topics=['/sensors/gnss/gnss']):
    timegnss.append(msg.time_meas)
    longitude.append(msg.longitude_deg)  # 12经度
    # print msg.longitude_deg
    latitude.append(msg.latitude_deg)  # 13纬度

index = 0
curr_time = 0
for topic, msg, t in bag.read_messages(topics=['/canbus/car_info']):
    car_info.ParseFromString(msg.data)
    if car_info.time_meas < timegnss[0]:
        continue

    if car_info.time_meas > timegnss[len(timegnss) - 1]:
        break

    curr_time = timegnss[index]
    if car_info.time_meas > curr_time:
        # print car_info
        timeinfo.append(car_info.time_meas)
        beam.append(car_info.misc.beam)  # 6 7
        throttle.append(car_info.throttle_report.actual_pedal)  # 8
        brake.append(car_info.brake_report.pedal_cmd_enabled)  # 9
        actual_angle.append(car_info.steer_report.actual_angle)  # 15
        index += 1
        continue

index = 0
curr_time= 0
for topic, msg, t in bag.read_messages(topics=['/canbus/car_state']):
    car_state.ParseFromString(msg.data)
    if car_state.time_meas < timegnss[0]:
        continue

    if car_state.time_meas > timegnss[len(timegnss) - 1]:
        break

    curr_time = timegnss[index]
    if car_state.time_meas > curr_time:
        timestate.append(car_state.time_meas)
        drivingmode.append(car_state.driving_mode)  # 1 2 3
        gear.append(car_state.gear)  # 4
        turnsignal.append(car_state.turn_signal)  # 5
        speed.append(car_state.speed)  # 14
        direction.append(car_state.roll_pitch_yaw.z)
        index += 1
        continue

print('longitude size %f' % len(longitude))
print('latitude size %f' % len(latitude))
print('beam size %f' % len(beam))
print('throttle size %f' % len(throttle))
print('brake size %f' % len(brake))
print('actual_angle size %f' % len(actual_angle))
print('direction size %f' % len(direction))
print('drivingmode size %f' % len(drivingmode))
print('gear size %f' % len(gear))
print('turnsignal size %f' % len(turnsignal))
print('speed size %f' % len(speed))
# *********************************************************
# *********************************************************
timestate0 = []
for i in range(0, len(timestate)):
    # timestate0.append(timestate[i] / 1e6 - timestate[0] / 1e6)
    timestate0.append(timestate[i] / 1e6 - timestate[i -1] / 1e6)
    # print timestate0

timeinfo0 = []
for i in range(0, len(timeinfo)):
    timeinfo0.append(timeinfo[i] / 1e6 - timeinfo[0] / 1e6)

timegnss0 = []
for i in range(0, len(timegnss)):
    timegnss0.append(timegnss[i] / 1e6 - timegnss[0] / 1e6)

# 10 == 1

# 1
# 2
# 3
data1 = []
data2 = []
data3 = []
for i in range(0, len(drivingmode)):
    if drivingmode[i] > 0:
        data1.append(1)  # 驾驶模式
        data2.append(0)  # 数据记录系统
        data3.append(1)  # 自动驾驶系统状态
    else:
        data1.append(0)
        data2.append(1)
        data3.append(0)

# 4
data4 = []
for i in range(0, len(gear)):  # 档位
    if gear[i] == 1:
        data4.append(0)
    if gear[i] == 5:
        data4.append(1)
    if gear[i] == 2:
        data4.append(2)
    if gear[i] == 3:
        data4.append(3)
    if gear[i] == 4:
        data4.append(4)
    if gear[i] == 0:
        data4.append("none")
    # else:
    #     if i % 50 == 0:
    #         data4.append(0)

# 5
data5 = []
for i in range(0, len(turnsignal)):
    data5.append(turnsignal[i])  # 转向灯状态

# 6
# 7
data6 = []
data7 = []
for i in range(0, len(beam)):
    if beam[i] == 2:  # 远光灯开启
        data6.append(1)
    if beam[i] == 3:  # 近光灯开启
        data7.append(1)
    else:
        data6.append(0)
        data7.append(0)

# 8
data8 = []
for i in range(0, len(throttle)):  # 加速踏板进程值
    data8.append(throttle[i] * 100)

# 9
data9 = []
for i in range(0, len(brake)):  # 制动踏板状态
    data9.append(brake[i])

# 10 11
data10 = []
data11 = []
data19 = []
data20 = []
for i in range(0, len(timestate0)):
    data10.append(1)  # 启动状态
    data11.append(0)  # 环境感知传感状态
    # data11.append(2)
    data19.append(0)  # 遥控泊车
    data20.append(1)  # 人工接管提醒　todo 遥控泊车目前没有,暂时赋１,人工接管提醒目前没有可取,暂时赋１,

# 12 13
data12 = []
data13 = []
for i in range(0, len(longitude)):
    data12.append(longitude[i])  # 经度
    data13.append(latitude[i])  # 纬度

# 14
data14 = []
for i in range(0, len(speed)):
    data14.append(speed[i])  # 车速

# 15
data15 = []
for i in range(0, len(direction)):
    data15.append(direction[i])  # 方向

# 16
data16 = []
for i in range(0, len(direction)):
    data16.append(direction[i] * 14.8)  # 方向盘角度


# data17 = []
# for i in range(0, len(speed)):  # 纵向加速度生成
#     print i
#     data17.append(speed[i + 1] - speed[0] / timestate0[i+1] - timestate0[i])


# print len(speed)
# print len(timestate0)

data18 = []
for i in range(0, len(speed)):  # 仪表车速
    data18.append(speed[i] + 4)
    # print data18



# plt.figure(1)
# plt.title('Plot 1', size=14)
# plt.xlabel('x', size=14)
# plt.ylabel('y', size=14)
# plt.plot(timestate0, speed, marker='o', color='r')
#
# plt.show()
# *********************************************************
# *********************************************************

book = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet1 = book.add_sheet('sheet1', cell_overwrite_ok=True)
sheet1.col(0).width = (15 * 256)
sheet1.col(1).width = (15 * 256)
sheet1.col(2).width = (15 * 256)
sheet1.col(3).width = (15 * 256)
sheet1.col(4).width = (15 * 256)
sheet1.col(5).width = (15 * 256)
sheet1.col(6).width = (15 * 256)
sheet1.col(7).width = (15 * 256)
sheet1.col(8).width = (15 * 256)
sheet1.col(9).width = (15 * 256)
sheet1.col(10).width = (15 * 256)
sheet1.col(11).width = (15 * 256)
sheet1.col(12).width = (15 * 256)
sheet1.col(13).width = (15 * 256)
sheet1.col(14).width = (15 * 256)

count = 0

heads = ["驾驶模式", "数据记录系统状态", "档位", "转向灯状态", "远光灯", "近光灯", "制动踏板状态",
         "启动状态", "环境感知传感器状态", "人工接管提醒", "遥控泊车", "自动驾驶控制系统系统状态", ]


print('......')
for head in heads:
    sheet1.write(0, count, head)
    count += 1
i = 1
for data in data1:  # 驾驶模式写入
    sheet1.write(i, 0, data)
    i += 1
i = 1
for data in data2:  # 数据记录系统状态写入
    sheet1.write(i, 1, data)
    i += 1
i = 1
for data in data4:  # 档位写入
    sheet1.write(i, 2, data)
    i += 1
i = 1
for data in data5:  # 转向灯状态写入
    sheet1.write(i, 3, data)
    i += 1
i = 1
for data in data6:  # 远光灯写入
    sheet1.write(i, 4, data)
    i += 1
i = 1
for data in data7:  # 近光灯写入
    sheet1.write(i, 5, data)
    i += 1
i = 1
for data in data9:  # 制动踏板状态写入
    sheet1.write(i, 6, data)
    i += 1
i = 1
for data in data10:  # 启动状态写入
    sheet1.write(i, 7, data)
    i += 1
i = 1
for data in data11:  # 环境感知传感器状态写入
    sheet1.write(i, 8, data)
    i += 1
i = 1
for data in data20:  # 人工接管提醒写入
    sheet1.write(i, 9, data)
    i += 1
i = 1
for data in data19:  # 遥控泊车写入
    sheet1.write(i, 10, data)
    i += 1
i = 1
for data in data3:  # 自动驾驶系统系统状态写入
    sheet1.write(i, 11, data)
    i += 1
i = 1


book.save(WriteFilePath)
print('OK')

bag.close()
