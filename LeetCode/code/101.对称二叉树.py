#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#
# https://leetcode-cn.com/problems/symmetric-tree/description/
#
# algorithms
# Easy (57.24%)
# Likes:    1797
# Dislikes: 0
# Total Accepted:    521.4K
# Total Submissions: 910.9K
# Testcase Example:  '[1,2,2,3,4,4,3]'
#
# 给你一个二叉树的根节点 root ， 检查它是否轴对称。
#
#
#
# 示例 1：
#
#
# 输入：root = [1,2,2,3,4,4,3]
# 输出：true
#
#
# 示例 2：
#
#
# 输入：root = [1,2,2,null,3,null,3]
# 输出：false
#
#
#
#
# 提示：
#
#
# 树中节点数目在范围 [1, 1000] 内
# -100 <= Node.val <= 100
#
#
#
#
# 进阶：你可以运用递归和迭代两种方法解决这个问题吗？
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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isPalindrome(s):
            index = 0
            while index < len(s) / 2:
                # 任何一方为 None
                if not s[index] or not s[-index - 1]:
                    if not s[index] == s[-index - 1] == None:
                        return False
                # 都不是 None
                elif s[index].val != s[-index - 1].val:
                    return False
                index += 1

        list = []
        list.append([root])
        dep = 0
        while len(list[dep]) != 0:
            list.append([])
            for i in list[dep]:
                # 本身非空
                if not i: continue
                # 添加左右子树,即使是None也加
                list[dep + 1].append(i.left)
                list[dep + 1].append(i.right)
            dep += 1

        for i in range(0, dep):
            if not isPalindrome(list[i]):
                return False

        return True
# @lc code=end
