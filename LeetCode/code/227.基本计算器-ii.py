#
# @lc app=leetcode.cn id=227 lang=python
#
# [227] 基本计算器 II
#
# https://leetcode-cn.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (43.80%)
# Likes:    547
# Dislikes: 0
# Total Accepted:    105K
# Total Submissions: 239.9K
# Testcase Example:  '"3+2*2"'
#
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
#
# 整数除法仅保留整数部分。
#
# 你可以假设给定的表达式总是有效的。所有中间结果将在 [-2^31, 2^31 - 1] 的范围内。
#
# 注意：不允许使用任何将字符串作为数学表达式计算的内置函数，比如 eval() 。
#
#
#
# 示例 1：
#
#
# 输入：s = "3+2*2"
# 输出：7
#
#
# 示例 2：
#
#
# 输入：s = " 3/2 "
# 输出：1
#
#
# 示例 3：
#
#
# 输入：s = " 3+5 / 2 "
# 输出：5
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 3 * 10^5
# s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
# s 表示一个 有效表达式
# 表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
# 题目数据保证答案是一个 32-bit 整数
#
#
#


# @lc code=start
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        op, index = '+', 0
        while index < len(s):
            if s[index] == ' ':
                index += 1
                continue
            elif s[index].isdigit():
                num = int(s[index])
                while index + 1 < len(s) and s[index + 1].isdigit():
                    index += 1
                    num = num * 10 + int(s[index])
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    pop = stack.pop()
                    if pop < 0:
                        stack.append(-(-pop // num))
                    else:
                        stack.append(pop // num)
            elif s[index] in '+-*/':
                op = s[index]
            index += 1
        return sum(stack)

    # wrong
    def calculate_1(self, s):
        """
        :type s: str
        :rtype: int
        """
        numStack = []
        num = 0
        preSign = '+'
        for i in range(len(s)):
            if s[i] == ' ': continue
            elif s[i].isdigit():
                num = num * 10 + int(s[i])
            elif not s[i].isdigit() or i == len(s) - 1:
                if preSign == '+':
                    numStack.append(num)
                elif preSign == '-':
                    numStack.append(-num)
                elif preSign == '*':
                    numStack.append(numStack.pop() * num)
                elif preSign == '/':
                    numStack.append(numStack.pop() // num)
                preSign = s[i]
                num = 0
        return sum(numStack)


# @lc code=end
# Accepted
# 109/109 cases passed (92 ms)
# Your runtime beats 51.6 % of python submissions
# Your memory usage beats 89.5 % of python submissions (14.8 MB)
