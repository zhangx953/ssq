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
    red_ball = []
    i = 6
    while i > 0:
        temp = random.choice(range(1, 33, 1))
        if temp in red_ball:
            continue
        else:
            red_ball.append(temp)
            i = i - 1
        red_ball.sort()
    return red_ball


def random_blue():
    blue_ball = []
    blue_ball.append(random.choice(range(1, 13, 1)))
    return blue_ball


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
    red_num = input("请输入6个红球号码，中间用逗号间隔：")
    red_num = list(red_num)
    red_num.sort()
    if len(red_num) != 6:
        print("您输入的红球位数不正确！！！")
        return
    for i in red_num:
        if i > 36:
            print("您输入的%d红球号码超出范围！！"%i )
            return
    blue_num = input("请输入蓝球号码：")
    if blue_num > 16:
        print("您输入的蓝球号码超出范围！！！")
        return
    red_num.append(blue_num)
    num = red_num
    openfile = open('ssq.txt', 'a')
    openfile.write(str(num) + '\n')
    openfile.close()


def count_num():
    openfile = open('ssq.txt', 'r')
    str_num = openfile.readlines()
    for i in str_num:
        line = i.split(',')
        print line


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
            print("请输入正确的编号！！！")
