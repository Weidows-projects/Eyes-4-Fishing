/*
 * @?: *********************************************************************
 * @Author: Weidows
 * @Date: 2022-03-16 19:22:34
 * @LastEditors: Weidows
 * @LastEditTime: 2022-03-16 23:03:44
 * @FilePath: \Blog-private\source\_posts\public-post\LeetCode\code\83.删除排序链表中的重复元素.go
 * @Description:
 * @!: *********************************************************************
 */
/*
 * @lc app=leetcode.cn id=83 lang=golang
 *
 * [83] 删除排序链表中的重复元素
 *
 * https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/description/
 *
 * algorithms
 * Easy (53.69%)
 * Likes:    744
 * Dislikes: 0
 * Total Accepted:    390.1K
 * Total Submissions: 726.6K
 * Testcase Example:  '[1,1,2]'
 *
 * 给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [1,1,2]
 * 输出：[1,2]
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = [1,1,2,3,3]
 * 输出：[1,2,3]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中节点数目在范围 [0, 300] 内
 * -100 <= Node.val <= 100
 * 题目数据保证链表已经按升序 排列
 *
 *
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

package main

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	for slow, fast := head, head; fast != nil; {
		fast = fast.Next
		if fast == nil || slow.Val != fast.Val {
			slow.Next = fast
			slow = slow.Next
		}
	}

	return head
}

// @lc code=end
