#
# @lc app=leetcode.cn id=231 lang=python
#
# [231] 2 的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (50.49%)
# Likes:    478
# Dislikes: 0
# Total Accepted:    211.5K
# Total Submissions: 419K
# Testcase Example:  '1'
#
# 给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。
#
# 如果存在一个整数 x 使得 n == 2^x ，则认为 n 是 2 的幂次方。
#
#
#
# 示例 1：
#
#
# 输入：n = 1
# 输出：true
# 解释：2^0 = 1
#
#
# 示例 2：
#
#
# 输入：n = 16
# 输出：true
# 解释：2^4 = 16
#
#
# 示例 3：
#
#
# 输入：n = 3
# 输出：false
#
#
# 示例 4：
#
#
# 输入：n = 4
# 输出：true
#
#
# 示例 5：
#
#
# 输入：n = 5
# 输出：false
#
#
#
#
# 提示：
#
#
# -2^31
#
#
#
#
# 进阶：你能够不使用循环/递归解决此问题吗？
#
#


# @lc code=start
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        a = 1
        while a < n:
            a = a << 1
        return a == n


# @lc code=end
