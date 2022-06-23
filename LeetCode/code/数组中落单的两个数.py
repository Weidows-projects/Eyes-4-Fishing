'''
?: *********************************************************************
Author: Weidows
Date: 2022-06-23 02:11:16
LastEditors: Weidows
LastEditTime: 2022-06-23 02:11:24
FilePath: \Blog-private\source\_posts\public-post\LeetCode\code\数组中落单的两个数.py
Description:
!: *********************************************************************
'''
def findTwoSingleNum(array):
    # 两个独立数的异或
    buff = 0
    for i in array:
        buff ^= i

    bias = 0
    # 从末尾轮着找为'1'的位 (也就是两独立数不同的位)
    while (buff & 1 != 1):
        buff >> 1
        bias += 1

    res_0, res_1 = 0, 0
    # 通过第bias位的0和1分为两个child-array, 分别all-XOR后就是两个结果
    for i in array:
        if (i >> bias & 1 == 1): res_1 ^= i
        else: res_0 ^= i

    return [res_0, res_1]


# 4:    100
# 5:    101
# 4^5:  001
# xxx1&1: 1
arr = [1, 1, 2, 2, 3, 3, 4, 5]
print(findTwoSingleNum(arr))
