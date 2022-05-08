#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (41.64%)
# Likes:    7989
# Dislikes: 0
# Total Accepted:    1.3M
# Total Submissions: 3.2M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
#
# 你可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
#
#
# 示例 1：
#
#
# 输入：l1 = [2,4,3], l2 = [5,6,4]
# 输出：[7,0,8]
# 解释：342 + 465 = 807.
#
#
# 示例 2：
#
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
#
#
# 示例 3：
#
#
# 输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# 输出：[8,9,9,9,0,0,0,1]
#
#
#
#
# 提示：
#
#
# 每个链表中的节点数在范围 [1, 100] 内
# 0
# 题目数据保证列表表示的数字不含前导零
#
#
#

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution:
    # Accepted
    # 1568/1568 cases passed (56 ms)
    # Your runtime beats 88.11 % of python3 submissions
    # Your memory usage beats 12.46 % of python3 submissions (15.1 MB)
    def addTwoNumbers(self,
                      l1: ListNode,
                      l2: ListNode,
                      carry_flag=0) -> Optional[ListNode]:
        val1, val2 = l1.val if l1 else 0, l2.val if l2 else 0
        s = val1 + val2 + carry_flag
        val, carry_flag = s % 10, 1 if s >= 10 else 0

        # 由于题目给的是逆序链表,也就是说即使位数不一致也是末端对齐的,可以直接每位加起来
        # 遍历下一位
        next1, next2 = l1.next if l1 else None, l2.next if l2 else None

        # next1 或 next2 任一非None, 或者 carry 为 1
        if next1 or next2 or carry_flag:
            return ListNode(val, self.addTwoNumbers(next1, next2, carry_flag))
        return ListNode(val)


# @lc code=end
