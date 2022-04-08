#!/usr/bin/env python
# coding=utf-8
from ustc_auto_report import USTCAutoHealthReport


bot = USTCAutoHealthReport()
# 登录
bot.login('BA20004011', 'password')
# 打卡
bot.daily_clock_in('post.json')
# 报备
# bot.weekly_report()
# 进出校申请
# bot.stayinout_apply('apply.json', t="3")
