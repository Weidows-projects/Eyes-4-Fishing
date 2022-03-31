import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

/*
 * @lc app=leetcode.cn id=442 lang=java
 *
 * [442] 数组中重复的数据
 *
 * https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/description/
 *
 * algorithms
 * Medium (70.19%)
 * Likes:    483
 * Dislikes: 0
 * Total Accepted:    52.2K
 * Total Submissions: 74.4K
 * Testcase Example:  '[4,3,2,7,8,2,3,1]'
 *
 * 给你一个长度为 n 的整数数组 nums ，其中 nums 的所有整数都在范围 [1, n] 内，且每个整数出现 一次 或 两次 。请你找出所有出现
 * 两次 的整数，并以数组形式返回。
 *
 * 你必须设计并实现一个时间复杂度为 O(n) 且仅使用常量额外空间的算法解决此问题。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [4,3,2,7,8,2,3,1]
 * 输出：[2,3]
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,1,2]
 * 输出：[1]
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1]
 * 输出：[]
 *
 *
 *
 *
 * 提示：
 *
 *
 * n == nums.length
 * 1 <= n <= 10^5
 * 1 <= nums[i] <= n
 * nums 中的每个元素出现 一次 或 两次
 *
 *
 */

// @lc code=start
class Solution {
  public List<Integer> findDuplicates(int[] nums) {
    return findDuplicates2(nums);
  }

  // 原地 hash
  // 作者：changyj
  // 链接：https://leetcode-cn.com/problems/find-all-duplicates-in-an-array/solution/c-9545-yuan-di-ha-xi-ke-can-kao-448-by-p-r323/
  //
  // Accepted
  // 28/28 cases passed (3 ms)
  // Your runtime beats 100 % of java submissions
  // Your memory usage beats 48.83 % of java submissions (49.1 MB)
  List<Integer> findDuplicates2(int[] nums) {
    ArrayList<Integer> retList = new ArrayList<Integer>();
    int n = nums.length;
    for (int i : nums) {
      int index = (i - 1) % n;
      nums[index] += n;
    }

    for (int i = 0; i < nums.length; i++) {
      if (nums[i] > 2 * n) {
        retList.add(i + 1);
      }
    }

    return retList;
  }

  // HashSet
  // Accepted
  // 28/28 cases passed (15 ms)
  // Your runtime beats 19.56 % of java submissions
  // Your memory usage beats 5.86 % of java submissions (49.7 MB)
  List<Integer> findDuplicates1(int[] nums) {
    ArrayList<Integer> retList = new ArrayList<Integer>();
    HashSet<Integer> numSet = new HashSet<Integer>();

    for (Integer i : nums) {
      if (numSet.contains(i)) {
        retList.add(i);
      } else {
        numSet.add(i);
      }
    }

    return retList;
  }
}
// @lc code=end
