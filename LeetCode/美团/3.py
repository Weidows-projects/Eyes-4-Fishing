'''
?: *********************************************************************
Author: Weidows
Date: 2022-04-09 16:31:54
LastEditors: Weidows
LastEditTime: 2022-04-09 17:10:14
FilePath: \Blog-private\source\_posts\public-post\LeetCode\3.py
Description:
!: *********************************************************************
'''

import sys

line1 = sys.stdin.readline().strip(' ').split(' ')
node_num = int(line1[0])
edge_num = int(line1[1])

line2 = sys.stdin.readline().strip(' ').split(' ')
line3 = sys.stdin.readline().strip(' ').split(' ')

# [[2, 3, 4], [1], [2], []]
edge_map = [[] for i in range(node_num)]
for i in range(edge_num):
    line2[i] = int(line2[i])
    line3[i] = int(line3[i])
    edge_map[line2[i] - 1].append(line3[i])

ask_num = int(sys.stdin.readline().strip(' '))
# print(ask_num)
for i in range(ask_num):
    ask = sys.stdin.readline().strip(' ').split(' ')
    src = int(ask[0])
    dst = int(ask[1])
    if dst in edge_map[src - 1] or src in edge_map[dst - 1]:
        print('Yes')
    else:
        print('No')
