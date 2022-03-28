#
# @lc app=leetcode.cn id=69 lang=python
#
# [69] x 的平方根
#
# https://leetcode-cn.com/problems/sqrtx/description/
#
# algorithms
# Easy (38.88%)
# Likes:    946
# Dislikes: 0
# Total Accepted:    492.9K
# Total Submissions: 1.3M
# Testcase Example:  '4'
#
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
#
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
#
#
#
# 示例 1：
#
#
# 输入：x = 4
# 输出：2
#
#
# 示例 2：
#
#
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
#
#
#
#
# 提示：
#
#
# 0 <= x <= 2^31 - 1
#
#
#

print(5 / 2)  # 2.5
print(5 // 2)  # 2


# @lc code=start
class Solution(object):
    def mySqrt(self, x):
        # return self.mySqrt_2(float(x), float(x))
        return self.mySqrt_3(x)

    # 二分
    def mySqrt_1(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 1:
            return 0
        else:
            l, r, ans = 1, x, 1
            while l <= r:
                mid = (l + r) // 2
                if mid * mid <= x:
                    ans = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return ans

    # 牛顿迭代: 递归
    def mySqrt_2(self, x, i):
        if x < 1:
            return 0
        res = (x / i + i) / 2
        # 80% 24%
        # if abs(res - i) < 1e-6:
        # 98% 27%
        if res == i:
            return int(i)
        else:
            return self.mySqrt_2(x, res)

    # 93% 76%
    # 牛顿迭代: 迭代
    def mySqrt_3(self, x):
        if x < 1:
            return 0
        C, x0 = float(x), float(x)
        while True:
            xi = (x0 + C / x0) / 2
            if abs(x0 - xi) < 1e-7:
                break
            x0 = xi

        return int(x0)


# @lc code=end
