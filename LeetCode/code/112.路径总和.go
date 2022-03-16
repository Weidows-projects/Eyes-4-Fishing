/*
 * @?: *********************************************************************
 * @Author: Weidows
 * @Date: 2022-03-16 18:16:35
 * @LastEditors: Weidows
 * @LastEditTime: 2022-03-16 18:48:14
 * @FilePath: \Blog-private\source\_posts\public-post\LeetCode\code\112.路径总和.go
 * @Description:
 * @!: *********************************************************************
 */
/*
 * @lc app=leetcode.cn id=112 lang=golang
 *
 * [112] 路径总和
 *
 * https://leetcode-cn.com/problems/path-sum/description/
 *
 * algorithms
 * Easy (53.04%)
 * Likes:    817
 * Dislikes: 0
 * Total Accepted:    344.7K
 * Total Submissions: 649.8K
 * Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,null,1]\n22'
 *
 * 给你二叉树的根节点 root 和一个表示目标和的整数 targetSum 。判断该树中是否存在 根节点到叶子节点
 * 的路径，这条路径上所有节点值相加等于目标和 targetSum 。如果存在，返回 true ；否则，返回 false 。
 *
 * 叶子节点 是指没有子节点的节点。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
 * 输出：true
 * 解释：等于目标和的根节点到叶节点路径如上图所示。
 *
 *
 * 示例 2：
 *
 *
 * 输入：root = [1,2,3], targetSum = 5
 * 输出：false
 * 解释：树中存在两条根节点到叶子节点的路径：
 * (1 --> 2): 和为 3
 * (1 --> 3): 和为 4
 * 不存在 sum = 5 的根节点到叶子节点的路径。
 *
 * 示例 3：
 *
 *
 * 输入：root = [], targetSum = 0
 * 输出：false
 * 解释：由于树是空的，所以不存在根节点到叶子节点的路径。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 树中节点的数目在范围 [0, 5000] 内
 * -1000 <= Node.val <= 1000
 * -1000 <= targetSum <= 1000
 *
 *
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

package main

func hasPathSum(root *TreeNode, targetSum int) bool {
	return isEqual(root, targetSum, 0)
}

func isEqual(root *TreeNode, targetSum int, prevSum int) bool {
	ret := false

	if root == nil {
		// init-> false

		// 非叶子节点
	} else if !(root.Left == nil && root.Right == nil) {
		left := isEqual(root.Left, targetSum, root.Val+prevSum)
		right := isEqual(root.Right, targetSum, root.Val+prevSum)
		ret = left || right

		// 叶子节点
	} else if root.Val+prevSum == targetSum {
		ret = true
	}
	return ret
}

// @lc code=end
