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
    blue = list()
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
        YN = raw_input("是否继续投注（Y/N)？")
        if YN == 'N' or YN == 'n':
            break


if __name__ == '__main__':
    ssq()
