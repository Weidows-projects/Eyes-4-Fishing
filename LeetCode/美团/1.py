'''
?: *********************************************************************
Author: Weidows
Date: 2022-04-09 16:05:23
LastEditors: Weidows
LastEditTime: 2022-04-09 16:18:20
FilePath: \Blog-private\source\_posts\public-post\LeetCode\test.py
Description:
!: *********************************************************************
'''

import sys

n = int(sys.stdin.readline().strip(' '))
res = 0

if n == 0:
    print(1)
else:
    while n != 0:
        a = n % 10
        n = n // 10
        if a in [1, 2, 3, 4, 5, 7]: continue
        elif a in [0, 6, 9]: res += 1
        elif a == 8: res += 2

    print(res)
