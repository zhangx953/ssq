#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
    程序名称：ssq.py
    功    能：随机选择双色球，双色球号码录入，双色球记录统计。
    作    者：张   鑫
    创建时间：2019-08-18
    程序版本：Ver 1.0.0
"""

import random


def random_red():
    red = []
    i = 6
    while i > 0:
        temp = random.choice(range(1, 33, 1))
        if temp in red:
            continue
        else:
            red.append(temp)
            i = i - 1
        red.sort()
    return red


def random_blue():
    blue = []
    blue.append(random.choice(range(1, 13, 1)))
    return blue 


def select():
    times = raw_input("输入投注数:")
    i = 0
    while i < int(times):
        red = random_red()
        blue = random_blue()
        print("red:" + str(red) + ", blue:" + str(blue))
        i = i + 1


def ssq():
    while True:
        select()
        yn = raw_input("是否继续投注（Y/N)？")
        if yn == 'N' or yn == 'n':
            break


def input_num():
    print("输入号码！！")


def count_num():
    print("统计号码！！")


if __name__ == '__main__':
    while True:
        print("*****1) 随机选择")
        print("*****2) 号码录入")
        print("*****3) 号码统计")
        yn = input("请选择功能编号(1-3）：")
        if yn == 1:
            ssq()
        elif yn == 2:
            input_num()
        elif yn == 3:
            count_num()
        else:
            break
