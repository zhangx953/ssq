#!/usr/bin/env python
# -*- coding:utf-8 -*-

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


def select_1():
    red = random_red()
    blue = random_blue()
    print("red:" + str(red) + ", blue:" + str(blue))


def select_n():
    times = raw_input("输入投注数:")
    i = 0
    while i < int(times):
        select_1()
        i = i + 1


def ssq():
    while True:
        select_n()
        yn = raw_input("是否继续投注（Y/N)？")
        if yn == 'N' or yn == 'n':
            break


def input_num():
    print("输入号码！！")


def count_num():
    print("统计号码！！")


if __name__ == '__main__':
    while True:
        print("1) 随机选择")
        print("2) 号码录入")
        print("3) 号码统计")
        yn = input("请输入编号：")
        if yn == 1:
            ssq()
        elif yn == 2:
            input_num()
        elif yn == 3:
            count_num()
        else:
            break

