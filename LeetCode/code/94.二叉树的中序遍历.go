/*
 * @lc app=leetcode.cn id=94 lang=golang
 *
 * [94] 二叉树的中序遍历
 *
 * https://leetcode-cn.com/problems/binary-tree-inorder-traversal/description/
 *
 * algorithms
 * Easy (75.70%)
 * Likes:    1357
 * Dislikes: 0
 * Total Accepted:    762.4K
 * Total Submissions: 1M
 * Testcase Example:  '[1,null,2,3]'
 *
 * 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [1,null,2,3]
 * 输出：[1,3,2]
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = []
 * 输出：[]
 *
 *
 * 示例 3：
 *
 *
 * 输入：root = [1]
 * 输出：[1]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点数目在范围 [0, 100] 内
 * -100 <= Node.val <= 100
 *
 *
 *
 *
 * 进阶: 递归算法很简单，你可以通过迭代算法完成吗？
 *
 */
package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

// @lc code=start

func inorderTraversal(root *TreeNode) []int {
	// return midOrder1(root, []int{})
	return midOrder2(root)
}

// 迭代
// Accepted
// 70/70 cases passed (0 ms)
// Your runtime beats 100 % of golang submissions
// Your memory usage beats 76.82 % of golang submissions (1.9 MB)
func midOrder2(root *TreeNode) (res []int) {
	stack := []*TreeNode{}
	for root != nil || len(stack) > 0 {
		// 填入左斜线
		for root != nil {
			stack = append(stack, root)
			root = root.Left
		}
		// pop
		root = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		// add
		res = append(res, root.Val)

		root = root.Right
	}
	return
}

// 递归
// Accepted
// 70/70 cases passed (0 ms)
// Your runtime beats 100 % of golang submissions
// Your memory usage beats 76.82 % of golang submissions (1.9 MB)
func midOrder1(root *TreeNode, result []int) []int {
	if root == nil {
		return result
	}
	result = midOrder1(root.Left, result)
	result = append(result, root.Val)
	result = midOrder1(root.Right, result)
	return result
}

// @lc code=end
