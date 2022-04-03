import java.util.ArrayList;
import java.util.List;

/*
 * @lc app=leetcode.cn id=78 lang=java
 *
 * [78] 子集
 *
 * https://leetcode-cn.com/problems/subsets/description/
 *
 * algorithms
 * Medium (80.37%)
 * Likes:    1558
 * Dislikes: 0
 * Total Accepted:    410.9K
 * Total Submissions: 511.2K
 * Testcase Example:  '[1,2,3]'
 *
 * 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
 *
 * 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [0]
 * 输出：[[],[0]]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * -10
 * nums 中的所有元素 互不相同
 *
 *
 */

// @lc code=start
class Solution {
  int[] nums;
  List<List<Integer>> ans = new ArrayList<List<Integer>>();
  List<Integer> t = new ArrayList<Integer>();

  public List<List<Integer>> subsets(int[] nums) {
    this.nums = nums;
    dfs(0);
    return ans;
  }

  public void dfs(int cur) {
    if (cur == nums.length) {
      ans.add(new ArrayList<Integer>(t));
      return;
    }
    t.add(nums[cur]);
    dfs(cur + 1);
    t.remove(t.size() - 1);
    dfs(cur + 1);
  }
}

// @lc code=end
