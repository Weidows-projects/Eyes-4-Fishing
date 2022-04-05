#
# @lc app=leetcode.cn id=147 lang=python
#
# [147] 对链表进行插入排序
#
# https://leetcode-cn.com/problems/insertion-sort-list/description/
#
# algorithms
# Medium (68.64%)
# Likes:    500
# Dislikes: 0
# Total Accepted:    117K
# Total Submissions: 170.3K
# Testcase Example:  '[4,2,1,3]'
#
# 给定单个链表的头 head ，使用 插入排序 对链表进行排序，并返回 排序后链表的头 。
#
# 插入排序 算法的步骤:
#
#
# 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
# 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
# 重复直到所有输入数据插入完为止。
#
#
#
# 下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。
#
# 对链表进行插入排序。
#
#
#
#
#
# 示例 1：
#
#
#
#
# 输入: head = [4,2,1,3]
# 输出: [1,2,3,4]
#
# 示例 2：
#
#
#
#
# 输入: head = [-1,5,3,4,0]
# 输出: [-1,0,3,4,5]
#
#
#
# 提示：
#
#
#
#
# 列表中的节点数在 [1, 5000]范围内
# -5000 <= Node.val <= 5000
#
#
#


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# @lc code=start
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        dummy = ListNode(0, head)
        lastSorted = head
        curr = head.next

        while curr:
            # 比排序后的最后 node 还大, 不用管接着走
            if lastSorted.val <= curr.val:
                lastSorted = lastSorted.next
            else:
                prev = dummy
                while prev.next.val <= curr.val:
                    prev = prev.next
                # 抽出 cur
                lastSorted.next = curr.next
                # prev -> cur -> prev.next
                curr.next = prev.next
                prev.next = curr
            # cur 换为排序链表末尾的下一个
            curr = lastSorted.next
        return dummy.next


# @lc code=end
# Accepted
# 19/19 cases passed (128 ms)
# Your runtime beats 56.71 % of python submissions
# Your memory usage beats 71 % of python submissions (16.2 MB)
