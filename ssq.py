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
    if blue_num > 16 or blue_num < 0:
        print("您输入的蓝球号码超出范围！！！")
        return
    red_num.append(blue_num)
    num = str(red_num)

    openfile = open('ssq.txt', 'a')
    openfile.write(num[1:-1] + '\n')
    openfile.close()


def count_num():
    openfile = open('ssq.txt', 'r')
    str_num = openfile.readlines()
    RB1 = []
    RB2 = []
    RB3 = []
    RB4 = []
    RB5 = []
    RB6 = []
    BB = []
    for i in str_num:
        temp = i[:-1].split(',')
        RB1.append(int(temp[0]))
        RB2.append(int(temp[1]))
        RB3.append(int(temp[2]))
        RB4.append(int(temp[3]))
        RB5.append(int(temp[4]))
        RB6.append(int(temp[5]))
        BB.append(int(temp[6]))
    print('红球第一位数：' + str(RB1))
    print('红球第二位数：' + str(RB2))
    print('红球第三位数：' + str(RB3))
    print('红球第四位数：' + str(RB4))
    print('红球第五位数：' + str(RB5))
    print('红球第六位数：' + str(RB6))
    print('篮球：' + str(BB))



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
