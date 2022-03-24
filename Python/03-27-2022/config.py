#!/usr/bin/env python
# coding=utf-8
# 游戏Squish的配置文件
# -----------------------------
# 可根据偏好随意修改配置变量
# 如果游戏的节奏太快或太慢,可尝试修改与速度相关的变量
# 要在这个游戏中使用其他图像,可修改这些变量:
banana_image = 'banana.png'
weight_image = 'weight.png'
splash_image = 'weight.png'

# 这些配置决定了游戏的总体外观
screen_size = 800, 600
backgroud_color = 255, 255, 255
margin = 30
full_screen = 1
font_size = 48

# 这些设置决定了游戏的行为
drop_speed = 1
banana_speed = 10
speed_increase = 1
weights_per_level = 10
banana_pad_top = 40
banana_pad_side = 20
