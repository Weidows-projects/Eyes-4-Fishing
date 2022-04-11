import java.util.Deque;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;

/*
 * @lc app=leetcode.cn id=105 lang=java
 *
 * [105] 从前序与中序遍历序列构造二叉树
 *
 * https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
 *
 * algorithms
 * Medium (70.85%)
 * Likes:    1522
 * Dislikes: 0
 * Total Accepted:    333K
 * Total Submissions: 469.2K
 * Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
 *
 * 给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder
 * 是同一棵树的中序遍历，请构造二叉树并返回其根节点。
 *
 *
 *
 * 示例 1:
 *
 *
 * 输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
 * 输出: [3,9,20,null,null,15,7]
 *
 *
 * 示例 2:
 *
 *
 * 输入: preorder = [-1], inorder = [-1]
 * 输出: [-1]
 *
 *
 *
 *
 * 提示:
 *
 *
 * 1 <= preorder.length <= 3000
 * inorder.length == preorder.length
 * -3000 <= preorder[i], inorder[i] <= 3000
 * preorder 和 inorder 均 无重复 元素
 * inorder 均出现在 preorder
 * preorder 保证 为二叉树的前序遍历序列
 * inorder 保证 为二叉树的中序遍历序列
 *
 *
 */

/**
 * Definition for a binary tree node.
 */
class TreeNode {
  int val;
  TreeNode left;
  TreeNode right;

  TreeNode() {
  }

  TreeNode(int val) {
    this.val = val;
  }

  TreeNode(int val, TreeNode left, TreeNode right) {
    this.val = val;
    this.left = left;
    this.right = right;
  }
}

// @lc code=start
class Solution {
  private Map<Integer, Integer> indexMap;

  public TreeNode buildTree(int[] preorder, int[] inorder) {
    // return buildTree_recursion(preorder, inorder);
    return buildTree_stack(preorder, inorder);
  }

  // Accepted
  // 203/203 cases passed (1 ms)
  // Your runtime beats 99.31 % of java submissions
  // Your memory usage beats 53.44 % of java submissions (41 MB)
  public TreeNode buildTree_recursion(int[] preorder, int[] inorder) {
    int n = preorder.length;
    // 构造哈希映射，帮助我们快速定位根节点
    indexMap = new HashMap<Integer, Integer>();
    for (int i = 0; i < n; i++) {
      indexMap.put(inorder[i], i);
    }
    return myBuildTree(preorder, inorder, 0, n - 1, 0, n - 1);
  }

  public TreeNode myBuildTree(int[] preorder, int[] inorder, int pre_l, int pre_r, int in_l,
      int in_r) {
    if (pre_l > pre_r) {
      return null;
    }

    // 前序遍历中的第一个节点就是根节点
    // 先把根节点建立出来
    TreeNode root = new TreeNode(preorder[pre_l]);
    // 在中序遍历中定位根节点位置
    int inorder_root = indexMap.get(preorder[pre_l]);

    // 得到左子树中的节点数目 in_l -> inorder_root -> in_r
    int size_left_subtree = inorder_root - in_l;

    // 递归地构造左子树，并连接到根节点
    // 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
    root.left = myBuildTree(preorder, inorder, pre_l + 1, pre_l + size_left_subtree, in_l,
        inorder_root - 1);
    // 递归地构造右子树，并连接到根节点
    // 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
    root.right = myBuildTree(preorder, inorder, pre_l + size_left_subtree + 1, pre_r, inorder_root + 1,
        in_r);
    return root;
  }

  // Accepted
  // 203/203 cases passed (1 ms)
  // Your runtime beats 99.31 % of java submissions
  // Your memory usage beats 65.72 % of java submissions (40.9 MB)
  public TreeNode buildTree_stack(int[] preorder, int[] inorder) {
    if (preorder == null || preorder.length == 0) {
      return null;
    }
    TreeNode root = new TreeNode(preorder[0]);
    Deque<TreeNode> stack = new LinkedList<TreeNode>();
    stack.push(root);
    int inorderIndex = 0;
    for (int i = 1; i < preorder.length; i++) {
      int preorderVal = preorder[i];
      TreeNode node = stack.peek();
      if (node.val != inorder[inorderIndex]) {
        node.left = new TreeNode(preorderVal);
        stack.push(node.left);
      } else {
        while (!stack.isEmpty() && stack.peek().val == inorder[inorderIndex]) {
          node = stack.pop();
          inorderIndex++;
        }
        node.right = new TreeNode(preorderVal);
        stack.push(node.right);
      }
    }
    return root;
  }
}
// @lc code=end
