'''
?: *********************************************************************
Author: Weidows
Date: 2022-04-09 17:13:01
LastEditors: Weidows
LastEditTime: 2022-04-09 17:25:25
FilePath: \Blog-private\source\_posts\public-post\4.py
Description:
!: *********************************************************************
'''
import sys

n = int(sys.stdin.readline().strip(' '))

if n == 1:
    print(0)
    sys.exit()

res = 0

# i j
# k l
for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if i != j\
                   and i != k\
                   and j != l \
                   and k != l:
                    res += 1

print(res % 1000000007)
