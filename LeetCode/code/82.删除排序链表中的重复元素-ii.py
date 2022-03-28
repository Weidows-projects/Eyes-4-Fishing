#
# @lc app=leetcode.cn id=82 lang=python
#
# [82] 删除排序链表中的重复元素 II
#
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/description/
#
# algorithms
# Medium (53.28%)
# Likes:    848
# Dislikes: 0
# Total Accepted:    235.7K
# Total Submissions: 442.3K
# Testcase Example:  '[1,2,3,3,4,4,5]'
#
# 给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。
#
#
#
# 示例 1：
#
#
# 输入：head = [1,2,3,3,4,4,5]
# 输出：[1,2,5]
#
#
# 示例 2：
#
#
# 输入：head = [1,1,1,2,3]
# 输出：[2,3]
#
#
#
#
# 提示：
#
#
# 链表中节点数目在范围 [0, 300] 内
# -100 <= Node.val <= 100
# 题目数据保证链表已经按升序 排列
#
#
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head, prev=None):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return head

        if (prev is not None
                and head.val == prev) or (head.next
                                          and head.val == head.next.val):
            head = self.deleteDuplicates(head.next, head.val)
            return head
        else:
            head.next = self.deleteDuplicates(head.next, head.val)
            return head


# @lc code=end
