#!/usr/bin/env python
#coding:utf-8
import math
import time

import xlwt
import sys
import numpy as np
from numpy import ma
#sys.path.append('/opt/deeproute/control/lib/python2.7/dist-packages')
#sys.path.append('/opt/ros/kinetic/lib/python2.7/dist-packages')
# import rospy
import rosbag
import matplotlib.pyplot as plt

#sys.path.append('/opt/deeproute/control/lib/control_common_tmp/')
import car_state_pb2
# import control_command_pb2
# import path_pb2
import car_info_pb2
import path_pb2

import Bag_path

car_state = car_state_pb2.CarState()
# control_command = control_command_pb2.ControlCommand()
# path = path_pb2.Path()
car_info = car_info_pb2.CarInfo()
path = path_pb2.Path()

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


actual_angle = []
lead_vehicle_position_x = []
lead_vehicle_position_y = []
lead_vehicle_velocity_x = []
lead_vehicle_velocity_y = []
has_lead_vehicle = []
hazard_ctrl_signal = []
brake_rp = []


# *********************************************************
# *********************************************************
bag = rosbag.Bag(Bag_path.car_follow_stop_and_go)
WriteFilePath = '/home/dr/datasheet/{0}.xls'.format("car_follow_stop_and_go-" + time.strftime(Bag_path.TimeFormat, Bag_path.TimeLocal))


for topic, msg, t in bag.read_messages(topics=['/sensors/gnss/gnss']):
    timegnss.append(msg.time_meas)
    longitude.append(msg.longitude_deg)  # 12
    latitude.append(msg.latitude_deg)  # 13

for topic, msg, t in bag.read_messages(topics=['/canbus/car_info']):
    car_info.ParseFromString(msg.data)
    timeinfo.append(car_info.time_meas)
    beam.append(car_info.misc.beam)  # 6 7
    throttle.append(car_info.throttle_report.actual_pedal)  # 8
    brake.append(car_info.brake_report.pedal_cmd_enabled)  # 9
    # print car_info
    actual_angle.append(car_info.steer_report.actual_angle)  # 15
    # print len(actual_angle)
    brake_rp.append(car_info.brake_report.actual_pedal)  # 21
    # print car_info.brake_report.actual_pedal


for topic, msg, t in bag.read_messages(topics=['/canbus/car_state']):
    car_state.ParseFromString(msg.data)
    timestate.append(car_state.time_meas)
    drivingmode.append(car_state.driving_mode)  # 1 2 3
    gear.append(car_state.gear)  # 4
    turnsignal.append(car_state.turn_signal)  # 5
    speed.append(car_state.speed)  # 14
    # hazard_ctrl_signal.append(car_state.hazard_ctrl_signal)
    #print car_state.time_meas

for topic, msg, t in bag.read_messages(topics=['/planner/path']):
    path.ParseFromString(msg.data)
    hazard_ctrl_signal.append(path.hazard_ctrl_signal)  # 16
    if path.HasField("lead_vehicle"):
        has_lead_vehicle.append(1)
        lead_vehicle_position_x.append(path.lead_vehicle.position.x)  # 17
        lead_vehicle_position_y.append(path.lead_vehicle.position.y)  # 18
        lead_vehicle_velocity_x.append(path.lead_vehicle.velocity.x)  # 19
        lead_vehicle_velocity_y.append(path.lead_vehicle.velocity.y)  # 20
    else:
        has_lead_vehicle.append(0)
        lead_vehicle_position_x.append(0)  # 17
        lead_vehicle_position_y.append(0)  # 17
        lead_vehicle_velocity_x.append(0)
        lead_vehicle_velocity_y.append(0)





# *********************************************************
# *********************************************************
timestate0 = []
# for i in range(0, len(timestate)):
#     timestate0.append(timestate[i] / 1e6 - timestate[0] / 1e6)
i = 0
while i < len(timestate):
    timestate0.append(timestate[i])
    i += 5

timeinfo0 = []
for i in range(0, len(timeinfo)):
    timeinfo0.append(timeinfo[i] / 1e6 - timeinfo[0] / 1e6)

timegnss0 = []
for i in range(0, len(timegnss)):
    timegnss0.append(timegnss[i] / 1e6 - timegnss[0] / 1e6)

# 10 == 1

# 1驾驶模式
# 2
# 3
data1 = []
data2 = []
data3 = []
# for i in range(0, len(drivingmode)):
#     if drivingmode[i] > 0:
#         data1.append(1)
#         data2.append(0)
#         data3.append(1)
#     else:
#         data1.append(0)
#         data2.append(1)
#         data3.append(0)
i = 0
while i < len(drivingmode):
    if drivingmode[i] > 0:
        data1.append(1)
        data2.append(0)
        data3.append(1)
    else:
        data1.append(0)
        data2.append(1)
        data3.append(0)
    i += 5




# 4
data4 = []
# for i in range(0, len(gear)):
#     if gear[i] == 1:
#         data4.append(0)
#     if gear[i] == 5:
#         data4.append(1)
#     if gear[i] == 2:
#         data4.append(2)
#     if gear[i] == 3:
#         data4.append(3)
#     if gear[i] == 4:
#         data4.append(4)
    # else:
    #     if i % 50 == 0:
    #         data4.append(0)
i = 0
while i < len(gear):
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
    i += 5


# 5
data5 = []
# for i in range(0, len(turnsignal)):
#     data5.append(turnsignal[i])
i = 0
while i < len(turnsignal):
    data5.append(turnsignal[i])
    i += 5

# 6
# 7
data6 = []
data7 = []
# for i in range(0, len(beam)):
#     if beam[i] == 2:
#         data6.append(1)
#     if beam[i] == 3:
#         data7.append(1)
#     else:
#         data6.append(0)
#         data7.append(0)

i = 0
while i < len(beam):
    if beam[i] == 2:
        data6.append(1)
    if beam[i] == 3:
        data7.append(1)
    else:
        data6.append(0)
        data7.append(0)
    i += 5

# 8
data8 = []
# for i in range(0, len(throttle)):
#     # data8.append(throttle[i]*100)
#     data8.append(throttle[i])
i = 0
while i < len(throttle):
    data8.append(throttle[i])
    i += 5

# 9
data9 = []
# for i in range(0, len(brake)):
#     data9.append(brake[i])
while i < len(brake):
    data9.append(brake[i])
    i += 5

# 10 11
data10 = []
data11 = []
# for i in range(0, len(timestate0)):
#     data10.append(1)
#     data11.append(2)
i = 0
while i < len(timestate0):
    data10.append(1)
    data11.append(2)
    i += 5

# 12 13经纬度遍历
data12 = []
data13 = []
for i in range(0, len(longitude)):
    data12.append(longitude[i])
    data13.append(latitude[i])

# 14车速遍历
data14 = []
# for i in range(0, len(speed)):
#     data14.append(speed[i])
i = 0
while i < len(speed):
    data14.append(speed[i])
    i += 5

# 15转向角度遍历
data15 = []
# for i in range(0, len(actual_angle)):
#     data15.append(actual_angle[i])
i = 0
while i < len(actual_angle):
    data15.append(actual_angle[i])
    i += 5

# 16报警信息
data16 = []
for i in range(0, len(hazard_ctrl_signal)):
    if hazard_ctrl_signal[i] == 2:
        data16.append(1)
    else:
        data16.append(0)

# 17目标识别列表
data17 = []
data18 = []
data19 = []
data20 = []
# for i in range(0, len(lead_vehicle_position_x)):
#     for j in  range(0, len(lead_vehicle_position_y)):
#         data17.append(math.sqrt(lead_vehicle_position_x[i] ** 2 +lead_vehicle_position_y[j]** 2))


for i in range(0, len(has_lead_vehicle)):
    if (has_lead_vehicle[i] == 1):
        data17.append(lead_vehicle_position_x[i])
        data18.append(lead_vehicle_position_y[i])
        data19.append(lead_vehicle_velocity_x[i])
        data20.append(lead_vehicle_velocity_y[i])
        # data19.append(math.sqrt(lead_vehicle_velocity_x[i]**2))
        # data20.append(math.sqrt(lead_vehicle_velocity_y[i]**2))
        # data17.append(math.sqrt(lead_vehicle_position_x[i] **2 +lead_vehicle_position_y[i]** 2))
        # data18.append(math.sqrt(lead_vehicle_velocity_x[i] ** 2 + lead_vehicle_velocity_y[i] ** 2))
        # data17.append('car')
    elif (has_lead_vehicle[i] == None):
        data17.append("no object")

data21 = []
# for i in range(0, len(brake_rp)):
#     data21.append(brake_rp[i])
i = 0
while i < len(brake_rp):
    data15.append(brake_rp[i])
    i += 5


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
sheet1.col(15).width = (15 * 256)
sheet1.col(16).width = (15 * 256)
sheet1.col(17).width = (15 * 256)
sheet1.col(18).width = (15 * 256)
sheet1.col(19).width = (15 * 256)
sheet1.col(20).width = (15 * 256)

count = 0
old_heads = ['时间', '驾驶模式', '数据记录系统状态', '自动驾驶控制系统状态', '档位', '转向灯状态', '远光灯', '近光灯', '加速踏板行程值', '制动踏板状态', '启动状态', '环境感知传感器状态', '速度', '时间', '经度', '纬度']
heads = ['时间', '驾驶模式', '数据记录系统状态', '自动驾驶控制系统状态', '档位', '转向灯状态', '远光灯',
         '近光灯', '加速踏板行程值', '制动踏板状态', '启动状态', '环境感知传感器状态', '车速', '转向角度', '报警信号', '目标位置识别x', '目标位置识别y','目标速度识别x','目标速度识别y', '制动踏板行程值']

print('......')
for head in heads:
    sheet1.write(0, count, head)
    count += 1
i = 1
for data in timestate0:
    sheet1.write(i, 0, data)
    i += 1
i = 1
for data in data1:
    sheet1.write(i, 1, data)
    i += 1
i = 1
for data in data2:
    sheet1.write(i, 2, data)
    i += 1
i = 1
for data in data3:
    sheet1.write(i, 3, data)
    i += 1
i = 1
for data in data4:
    sheet1.write(i, 4, data)
    i += 1
i = 1
for data in data5:
    sheet1.write(i, 5, data)
    i += 1
i = 1
for data in data6:
    sheet1.write(i, 6, data)
    i += 1
i = 1
for data in data7:
    sheet1.write(i, 7, data)
    i += 1
i = 1
for data in data8:
    sheet1.write(i, 8, data)
    i += 1
i = 1
for data in data9:
    sheet1.write(i, 9, data)
    i += 1
i = 1
for data in data10:
    sheet1.write(i, 10, data)
    i += 1
i = 1
for data in data11:
    sheet1.write(i, 11, data)
    i += 1
i = 1
for data in data14:
    sheet1.write(i, 12, data)
    # sheet1.write(i, 12, data*3.6/0.1)
    i += 1
i = 1
# for data in timegnss0:
#     sheet1.write(i, 13, data)
#     i += 1
# i = 1 时间写入
# for data in data12:
#     sheet1.write(i, 14, data*1e6)
#     i += 1
# i = 1 经度写入
# for data in data13:
#     sheet1.write(i, 15, data*1e6)
#     i += 1  纬度写入

# ******新加******

for data in data15:
    sheet1.write(i, 13, data)
    i += 1
i = 1  # 15转向角度写入


for data in data16:
    sheet1.write(i, 14, data)
    i += 1
i = 1  # 16报警信息写入

for data in data17:
    sheet1.write(i, 15, data)
    i += 1
i = 1  # 17目标位置信息x写入

for data in data18:
    sheet1.write(i, 16, data)
    i += 1
i = 1  # 18目标位置信息y写入

for data in data19:
    sheet1.write(i, 17, data)
    i += 1
i = 1  # 19目标速度信息x写入

for data in data20:
    sheet1.write(i, 18, data)
    i += 1
i = 1  # 20目标速度信息y写入

for data in data21:
    sheet1.write(i, 19, data)
    i += 1  # 21制动阀值写入

book.save(WriteFilePath)
print('OK')
bag.close()
