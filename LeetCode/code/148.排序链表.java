/*
 * @lc app=leetcode.cn id=148 lang=java
 *
 * [148] 排序链表
 *
 * https://leetcode-cn.com/problems/sort-list/description/
 *
 * algorithms
 * Medium (66.52%)
 * Likes:    1544
 * Dislikes: 0
 * Total Accepted:    272.3K
 * Total Submissions: 409.3K
 * Testcase Example:  '[4,2,1,3]'
 *
 * 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
 *
 *
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：head = [4,2,1,3]
 * 输出：[1,2,3,4]
 *
 *
 * 示例 2：
 *
 *
 * 输入：head = [-1,5,3,4,0]
 * 输出：[-1,0,3,4,5]
 *
 *
 * 示例 3：
 *
 *
 * 输入：head = []
 * 输出：[]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 链表中节点的数目在范围 [0, 5 * 10^4] 内
 * -10^5 <= Node.val <= 10^5
 *
 *
 *
 *
 * 进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？
 *
 */

class ListNode {
  int val;
  ListNode next;

  ListNode() {
  }

  ListNode(int val) {
    this.val = val;
  }

  ListNode(int val, ListNode next) {
    this.val = val;
    this.next = next;
  }
}

// @lc code=start
class Solution {
  public ListNode sortList(ListNode head) {
    return sortList(head, null);
  }

  // 分
  public ListNode sortList(ListNode head, ListNode tail) {
    if (head == null) {
      return head;
    }
    if (head.next == tail) {
      head.next = null;
      return head;
    }
    ListNode slow = head, fast = head;
    while (fast != tail) {
      slow = slow.next;
      fast = (fast.next != tail) ? fast.next.next : fast.next;
    }
    return merge(sortList(head, slow), sortList(slow, tail));
  }

  // 合
  public ListNode merge(ListNode head1, ListNode head2) {
    ListNode dummyHead = new ListNode(0);
    ListNode temp = dummyHead, temp1 = head1, temp2 = head2;
    while (temp1 != null && temp2 != null) {
      if (temp1.val <= temp2.val) {
        temp.next = temp1;
        temp1 = temp1.next;
      } else {
        temp.next = temp2;
        temp2 = temp2.next;
      }
      temp = temp.next;
    }
    if (temp1 != null) {
      temp.next = temp1;
    } else if (temp2 != null) {
      temp.next = temp2;
    }
    return dummyHead.next;
  }
}

// @lc code=end
// Accepted
// 28/28 cases passed (6 ms)
// Your runtime beats 82.14 % of java submissions
// Your memory usage beats 37.97 % of java submissions (49 MB)
