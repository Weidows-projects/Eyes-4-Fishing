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
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        # return self.sub_node(root.left, root.right)
        return self.sub_node_2(root.left, root.right)

    # 队列
    # Accepted
    # 198/198 cases passed (20 ms)
    # Your runtime beats 71.59 % of python submissions
    # Your memory usage beats 26.02 % of python submissions (13.3 MB)
    def sub_node_2(self, p, q):
        queue = [p, q]
        while queue:
            p = queue.pop(0)
            q = queue.pop(0)
            if p is None and q is None:
                continue
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            queue.append(p.left)
            queue.append(q.right)
            queue.append(p.right)
            queue.append(q.left)
        return True

    # 递归
    # Accepted
    # 198/198 cases passed (20 ms)
    # Your runtime beats 71.59 % of python submissions
    # Your memory usage beats 93.31 % of python submissions (13 MB)
    def sub_node(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        return p.val == q.val and self.sub_node(
            p.left, q.right) and self.sub_node(p.right, q.left)

    # wrong: [1]
    def isSymmetric_2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        arr = []
        self.midOrder(root, arr)
        # print(arr)

        l, r = 0, len(arr) - 1
        while l != r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True

    def midOrder(self, root, arr):
        if root is None:
            arr.append(None)
        else:
            self.midOrder(root.left, arr)
            arr.append(root.val)
            self.midOrder(root.right, arr)


# @lc code=end


# [None, 3, None, 2, None, 4, None, 1, None, 4, None, 2, None, 3, None]
# True
def sample_1():
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    print(s.isSymmetric(root))


def sample_2():
    s = Solution()
    root = TreeNode(1)
    print(s.isSymmetric(root))


if __name__ == '__main__':
    # sample_1()
    sample_2()
