#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
    程序名称：ssq.py
    功    能：随机选择双色球，双色球号码录入，双色球数据统计。
    作    者：张   鑫
    创建时间：2019-08-18
    修改时间：2019-09-08 10:20
    程序版本：Ver 1.0.0
"""

import random
from pyecharts import Bar
from pyecharts import Pie


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
    blue_ball = list()
    blue_ball.append(random.choice(range(1, 13, 1)))
    return blue_ball


def random_select():
    times = raw_input("输入投注数:")
    if times.isdigit():
        i = 0
        red_str = []
        blue_str = []
        while i < int(times):
            red = random_red()
            for r in red:
                if r <= 9:
                    red_str.append("0" + str(r))
                else:
                    red_str.append(str(r))
            blue = random_blue()
            for b in blue:
                if b <= 9:
                    blue_str.append('0' + str(b))
                else:
                    blue_str.append(str(b))
            print("red:" + str(red_str) + ", blue:" + str(blue_str))
            red_str = []
            blue_str = []
            i = i + 1
    else:
        print("请输入数字！！")


def ssq_select():
    while True:
        random_select()
        yn1 = raw_input("是否继续投注（Y/N)？")
        if yn1 == 'N' or yn1 == 'n':
            break


def input_num():
    temp = raw_input("请输入6个红球号码，中间用逗号间隔：")
    temp = list(temp.split(','))
    if len(temp) != 6:
        print("您输入的红球位数不正确！！！")
        return
    for t in temp:
        if not t.isdigit():
            print("您输入的不全为数字！！！")
            return
    red_num = []
    for r in temp:
        if int(r) <= 9:
            red_num.append('0' + r)
        else:
            red_num.append(r)
    red_num.sort()
    if len(red_num) != 6:
        print("您输入的红球位数不正确！！！")
        return
    for i in red_num:
        if int(i) > 36:
            print("您输入的%d红球号码超出范围！！"%i )
            return
    blue_num = raw_input("请输入蓝球号码：")
    if not blue_num.isdigit():
        print ("请输入数字！！！")
        return
    if int(blue_num) > 16 or int(blue_num) <=0:
        print("您输入的蓝球号码超出范围！！！")
        return
    if int(blue_num) <= 9:
        blue_num = '0' + blue_num

    red_num.append(blue_num)
    num = red_num
    """
    temp = []
    for i in num:
        if int(i) <= 9:
            temp.append('0' + str(i))
        else:
            temp.append(str(i))
    num = temp
    """
    openfile = open('ssq.txt', 'r')
    lines = openfile.readlines()
    last_line = lines[-1]
    qi_num = int(last_line[:5]) + 1
    openfile.close()
    openfile = open('ssq.txt', 'a')
    openfile.write( str(qi_num) + ":" + str(num) + '\n')
    openfile.close()


def count_num():
    openfile = open('ssq.txt', 'r')
    str_num = openfile.readlines()
    openfile.close()

    RB1 = []    # 红球第一个数
    RB2 = []    # 红球第二个数
    RB3 = []    # 红球第三个数
    RB4 = []    # 红球第四个数
    RB5 = []    # 红球第五个数
    RB6 = []    # 红球第六个数
    BB = []     # 蓝球

    for i in str_num:
        # 取出7位号码的字符串
        temp = i.split(':')
        temp = temp[1][1:-2]

        # 把读取的数据添加到对应的数据位中
        RB1.append(temp[1:3])
        RB2.append(temp[7:9])
        RB3.append(temp[13:15])
        RB4.append(temp[19:21])
        RB5.append(temp[25:27])
        RB6.append(temp[31:33])
        BB.append(temp[37:39])

    # 按位统计显示
    print("*****统计总期数为：")
    print("%d期" % len(BB))
    print("*****数值分布情况：")
    print('红球第一位数：' + str(RB1))
    print('红球第二位数：' + str(RB2))
    print('红球第三位数：' + str(RB3))
    print('红球第四位数：' + str(RB4))
    print('红球第五位数：' + str(RB5))
    print('红球第六位数：' + str(RB6))
    print('篮球号码统计：' + str(BB))

    # 统计各期数值求和
    i = 0
    TT = []
    while i < len(RB1):
        TT.append(int(RB1[i]) + int(RB2[i]) + int(RB3[i]) + int(RB4[i]) + int(RB5[i]) + int(RB6[i]) + int(BB[i]))
        i += 1
    print("*****各期红、蓝球数值求和分布：")
    print TT
    i = 0
    while i < len(TT):
        print("第%d期和值为：%d      " % (i+1, TT[i])),
        if (i+1) % 6 == 0:
            print
        i += 1
    print
    lower = 0
    middle = 0
    higher = 0
    for i in TT:
        if i <= 80:
            lower += 1
        elif (i > 80) and (i < 110):
            middle += 1
        elif i >= 110:
            higher += 1
    print("*低区：（和值小于等于80）：%d次  " % lower),
    print("*中区：（和值大于80小于110）：%d次  " % middle),
    print("*高区：（和值大于等于110）：%d次" % higher)

    # 统计每个球出现的次数
    RB = RB1 + RB2 + RB3 + RB4 + RB5 + RB6
    RT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    BT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in RB:
        if int(i) == 1:
            RT[1] += 1
        elif int(i) == 2:
            RT[2] += 1
        elif int(i) == 3:
            RT[3] += 1
        elif int(i) == 4:
            RT[4] += 1
        elif int(i) == 5:
            RT[5] += 1
        elif int(i) == 6:
            RT[6] += 1
        elif int(i) == 7:
            RT[7] += 1
        elif int(i) == 8:
            RT[8] += 1
        elif int(i) == 9:
            RT[9] += 1
        elif int(i) == 10:
            RT[10] += 1
        elif int(i) == 11:
            RT[11] += 1
        elif int(i) == 12:
            RT[12] += 1
        elif int(i) == 13:
            RT[13] += 1
        elif int(i) == 14:
            RT[14] += 1
        elif int(i) == 15:
            RT[15] += 1
        elif int(i) == 16:
            RT[16] += 1
        elif int(i) == 17:
            RT[17] += 1
        elif int(i) == 18:
            RT[18] += 1
        elif int(i) == 19:
            RT[19] += 1
        elif int(i) == 20:
            RT[20] += 1
        elif int(i) == 21:
            RT[21] += 1
        elif int(i) == 22:
            RT[22] += 1
        elif int(i) == 23:
            RT[23] += 1
        elif int(i) == 24:
            RT[24] += 1
        elif int(i) == 25:
            RT[25] += 1
        elif int(i) == 26:
            RT[26] += 1
        elif int(i) == 27:
            RT[27] += 1
        elif int(i) == 28:
            RT[28] += 1
        elif int(i) == 29:
            RT[29] += 1
        elif int(i) == 30:
            RT[30] += 1
        elif int(i) == 31:
            RT[31] += 1
        elif int(i) == 32:
            RT[32] += 1
        elif int(i) == 33:
            RT[33] += 1

    for i in BB:
        if int(i) == 1:
            BT[1] += 1
        elif int(i) == 2:
            BT[2] += 1
        elif int(i) == 3:
            BT[3] += 1
        elif int(i) == 4:
            BT[4] += 1
        elif int(i) == 5:
            BT[5] += 1
        elif int(i) == 6:
            BT[6] += 1
        elif int(i) == 7:
            BT[7] += 1
        elif int(i) == 8:
            BT[8] += 1
        elif int(i) == 9:
            BT[9] += 1
        elif int(i) == 10:
            BT[10] += 1
        elif int(i) == 11:
            BT[11] += 1
        elif int(i) == 12:
            BT[12] += 1
        elif int(i) == 13:
            BT[13] += 1
        elif int(i) == 14:
            BT[14] += 1
        elif int(i) == 15:
            BT[15] += 1
        elif int(i) == 16:
            BT[16] += 1

    # 显示红球各号码出现次数
    print("*****各红色球出现的次数：")
    print RT
    i = 1
    while i < 34:
        print ("红球%d共出现:%d次   " % (i, RT[i])),
        if i % 6 == 0:
            print
        i += 1
    print

    # 统计红球出现次数最少的数
    i = 1
    while i < len(RT):
        if RT[i] == min(RT[1:]):
            print ("%d, " % i),
        i += 1
    print("出现次数最少，每个数共计出现%d次！" % min(RT[1:]))

    # 统计红球出现次数最多的数
    i = 1
    while i < len(RT):
        if RT[i] == max(RT):
            print ("%d, " % i),
        i += 1
    print("出现次数最多，每个数共计出现%d次！" % max(RT))

    # 统计篮球各号码出现的次数
    print("*****蓝色球出现的次数：")
    print BT
    i = 1
    while i < 17:
        print ("蓝球各球%d共出现:%d次   " % (i, BT[i])),
        if i % 6 == 0:
            print
        i += 1
    print

    # 统计蓝球出现次数最少的数
    i = 1
    while i < len(BT):
        if BT[i] == min(BT[1:]):
            print ("%d, " % i),
        i += 1
    print("出现次数最少，每个数共计出现%d次！"% min(BT[1:]))

    # 统计蓝球出现次数最多的数
    i = 1
    while i < len(BT):
        if BT[i] == max(BT):
            print ("%d, " % i),
        i += 1
    print("出现次数最多，每个数共计出现%d次！" % max(BT))
    print

    # 利用pyecharts插件生成html格式图表，统计各球号码出现的次数
    bar = Bar("号码出现次数统计", title_pos='center', is_animation=True, width=1200, height=600,\
              background_color="#abc",title_color="#404")
    # bar.use_theme('dark')   # 黑色主题
    bar_x = range(1, 34)
    bar_red_y = RT[1:]
    bar_blue_y = BT[1:]
    times = 17  # 填充蓝球不足的位数
    while times > 0:
        bar_blue_y.append(0)
        times -= 1
    bar.add('红色球', bar_x, bar_red_y, is_more_utils=True, mark_line=['average'], mark_point=['max', 'min'], \
            legend_pos='left', is_label_show=True)
    bar.add('蓝色球', bar_x, bar_blue_y, is_more_utils=True, mark_point=['max', 'min'], xaxis_name='号码', \
            yaxis_name='次数', legend_pos='right', legend_orient='vertical', is_label_show=True)
    bar.render('red_blue_statistics.html')

    # 统计各期号码的和值
    bar = Bar("各期和值统计", title_pos='center', is_animation=True, width=1200, height=600, \
              background_color="#abc", title_color="#404")
    bar_x = []
    bar_y = TT
    f = open('ssq.txt')
    lines = f.readlines()
    for i in lines:
        bar_x.append(i[:5])
    f.close()
    bar.add('', bar_x, bar_y, is_more_utils=True, mark_line=['average'], mark_point=['max', 'min'], is_label_show=True)
    bar.render('stage_sum_statistics.html')

    # 和值区间统计
    attr = ['高区(<110y<=199)', '中区(80<y<110)', '低区(22<=y<=80)']
    v1 = [higher, middle, lower]
    pie = Pie('每期和值区间统计表', width=1000, height=500)
    pie.add("", attr, v1, center=[50, 50], radius=[25, 50], is_legend_show=True, is_label_show=True)
    pie.render('sum_section_statistics.html')


if __name__ == '__main__':
    while True:
        print("*****1) 随机选择 *****")
        print("*****2) 号码录入 *****")
        print("*****3) 号码统计 *****")
        print("*****4) 退出系统 *****")
        yn = raw_input("请选择功能编号(1-3）：")
        if yn == '1':
            ssq_select()
        elif yn == '2':
            input_num()
        elif yn == '3':
            count_num()
        elif yn == '4':
            exit()
        else:
            print("请输入正确的编号！！！")
