# coding:utf-8

of = open('ssq.txt', 'r')
wf = open('ssq2.txt', 'a')
lines = of.readlines()
line_num = 19079
for line in lines:
    temp = line.split(',')
    temp_new = []
    line_num += 1
    i = 0
    for i in temp:
        if '\n' in i:
            i = i[:-1]
            if len(i) < 2:
                temp_new.append('0' + i)
            else:
                temp_new.append(i)
        else:
            if len(i) < 2:
                temp_new.append('0' + i)
            else:
                temp_new.append(i)
    print("第%d期:"%line_num ),
    print temp_new
    wf.write(str(line_num) + ":" + str(temp_new) + '\n')

of.close()
wf.close()