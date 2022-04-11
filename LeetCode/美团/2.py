'''
?: *********************************************************************
Author: Weidows
Date: 2022-04-09 16:20:48
LastEditors: Weidows
LastEditTime: 2022-04-09 22:58:31
FilePath: \Blog-private\source\_posts\public-post\LeetCode\美团\2.py
Description:
!: *********************************************************************
'''

import sys

from sortedcollections import SortedList

n = int(sys.stdin.readline().strip(' '))
height = [int(i) for i in sys.stdin.readline().strip(' ').split(' ')]
name = [i for i in sys.stdin.readline().strip(' ').strip('\n').split(' ')]

if n == 1:
    print(name[0])
    sys.exit()

list = []
for i in range(n):
    list.append((height[i], name[i]))

# [(176, 'beta'), (170, 'tom'), (176, 'alpha'), (176, 'bamma')]
# print(list)

# [(170, 'tom'), (176, 'beta'), (176, 'alpha'), (176, 'bamma')]
list.sort(key=lambda x: x[0])

fin_res = []

# 170 176
for i in range(list[0][0], list[-1][0] + 1):
    buff_list = []
    while i == list[0][0]:
        buff_list.append(list[0])
        list.pop(0)

    buff_list = SortedList(buff_list, key=lambda x: x[1])

    for j in buff_list:
        fin_res.append(j[1])

print(' '.join(fin_res))
