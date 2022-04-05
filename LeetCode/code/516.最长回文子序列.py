#
# @lc app=leetcode.cn id=516 lang=python
#
# [516] 最长回文子序列
#
# https://leetcode-cn.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (66.12%)
# Likes:    767
# Dislikes: 0
# Total Accepted:    112.7K
# Total Submissions: 170.2K
# Testcase Example:  '"bbbab"'
#
# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
#
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
#
#
#
# 示例 1：
#
#
# 输入：s = "bbbab"
# 输出：4
# 解释：一个可能的最长回文子序列为 "bbbb" 。
#
#
# 示例 2：
#
#
# 输入：s = "cbbd"
# 输出：2
# 解释：一个可能的最长回文子序列为 "bb" 。
#
#
#
#
# 提示：
#
#
# 1
# s 仅由小写英文字母组成
#
#
#


# @lc code=start
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)

        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][n - 1]


# @lc code=end
# Accepted
# 86/86 cases passed (988 ms)
# Your runtime beats 52.33 % of python submissions
# Your memory usage beats 94.35 % of python submissions (27.3 MB)
