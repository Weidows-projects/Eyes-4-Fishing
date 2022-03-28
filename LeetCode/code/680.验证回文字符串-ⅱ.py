#
# @lc app=leetcode.cn id=680 lang=python
#
# [680] 验证回文字符串 Ⅱ
#
# https://leetcode-cn.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (40.09%)
# Likes:    470
# Dislikes: 0
# Total Accepted:    103.4K
# Total Submissions: 258K
# Testcase Example:  '"aba"'
#
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
#
#
#
# 示例 1:
#
#
# 输入: s = "aba"
# 输出: true
#
#
# 示例 2:
#
#
# 输入: s = "abca"
# 输出: true
# 解释: 你可以删除c字符。
#
#
# 示例 3:
#
#
# 输入: s = "abc"
# 输出: false
#
#
#
# 提示:
#
#
# 1
# s 由小写英文字母组成
#
#
#


# @lc code=start
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isPalindrome(s):
            return s == s[::-1]

        index = 0
        while s[index] == s[-index - 1]:
            if index < len(s) / 2:
                index += 1
            else:
                return True

        is1 = isPalindrome(
            s[index + 1:-index]) if index != 0 else isPalindrome(s[index + 1:])
        is2 = isPalindrome(s[index:-index - 1])
        return is1 or is2


# @lc code=end
