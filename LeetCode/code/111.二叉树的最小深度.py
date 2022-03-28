#
# @lc app=leetcode.cn id=111 lang=python
#
# [111] 二叉树的最小深度
#
# https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (49.74%)
# Likes:    703
# Dislikes: 0
# Total Accepted:    356.7K
# Total Submissions: 714.6K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明：叶子节点是指没有子节点的节点。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
#
#
# 示例 2：
#
#
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
#
#
#
#
# 提示：
#
#
# 树中节点数的范围在 [0, 10^5] 内
# -1000
#
#
#


# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 当前节点为空返回0
        if not root:
            return 0
        # 叶子节点
        if not root.left and not root.right:
            return 1
        # 左空,返回右+1
        elif not root.left:
            return 1 + self.minDepth(root.right)
        # 右空,返回左+1
        elif not root.right:
            return 1 + self.minDepth(root.left)
        # 都非空,返回左右最小+1
        else:
            return 1 + min(self.minDepth(root.right), self.minDepth(root.left))


# @lc code=end
