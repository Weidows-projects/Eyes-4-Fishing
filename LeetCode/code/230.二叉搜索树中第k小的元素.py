#
# @lc app=leetcode.cn id=230 lang=python
#
# [230] 二叉搜索树中第K小的元素
#
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/description/
#
# algorithms
# Medium (75.29%)
# Likes:    597
# Dislikes: 0
# Total Accepted:    198.3K
# Total Submissions: 263.4K
# Testcase Example:  '[3,1,4,null,2]\n1'
#
# 给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
#
#
#
# 示例 1：
#
#
# 输入：root = [3,1,4,null,2], k = 1
# 输出：1
#
#
# 示例 2：
#
#
# 输入：root = [5,3,6,2,4,null,null,1], k = 3
# 输出：3
#
#
#
#
#
#
# 提示：
#
#
# 树中的节点数为 n 。
# 1
# 0
#
#
#
#
# 进阶：如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 k 小的值，你将如何优化算法？
#
#


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# @lc code=start
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # return self.stack_search(root, k)

        self.k = k
        self.recursion_search(root)
        return self.res

    # Accepted
    # 93/93 cases passed (20 ms)
    # Your runtime beats 99.81 % of python submissions
    # Your memory usage beats 89.57 % of python submissions (20.4 MB)
    def stack_search(self, root, k):
        stack = [root]
        while stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right

    # Accepted
    # 93/93 cases passed (32 ms)
    # Your runtime beats 88.8 % of python submissions
    # Your memory usage beats 76.64 % of python submissions (20.5 MB)
    def recursion_search(self, root):
        if not root: return

        self.recursion_search(root.left)
        self.k -= 1
        if self.k == 0:
            self.res = root.val
            return
        self.recursion_search(root.right)


# @lc code=end
