import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

/*
 * @lc app=leetcode.cn id=1122 lang=java
 *
 * [1122] 数组的相对排序
 *
 * https://leetcode-cn.com/problems/relative-sort-array/description/
 *
 * algorithms
 * Easy (70.71%)
 * Likes:    207
 * Dislikes: 0
 * Total Accepted:    71.5K
 * Total Submissions: 101.1K
 * Testcase Example:  '[2,3,1,3,2,4,6,7,9,2,19]\n[2,1,4,3,9,6]'
 *
 * 给你两个数组，arr1 和 arr2，arr2 中的元素各不相同，arr2 中的每个元素都出现在 arr1 中。
 *
 * 对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1
 * 的末尾。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
 * 输出：[2,2,2,1,4,3,3,9,6,7,19]
 *
 *
 * 示例  2:
 *
 *
 * 输入：arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
 * 输出：[22,28,8,6,17,44]
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= arr1.length, arr2.length <= 1000
 * 0 <= arr1[i], arr2[i] <= 1000
 * arr2 中的元素 arr2[i]  各不相同 
 * arr2 中的每个元素 arr2[i] 都出现在 arr1 中
 *
 *
 */

// @lc code=start
class Solution {
  // Accepted
  // 16/16 cases passed (3 ms)
  // Your runtime beats 27.42 % of java submissions
  // Your memory usage beats 21.15 % of java submissions (41.1 MB)
  public int[] relativeSortArray(int[] arr1, int[] arr2) {
    ArrayList<Integer> retList = new ArrayList<Integer>();
    HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
    ArrayList<Integer> sortList = new ArrayList<Integer>();

    // arr2 填入 map
    for (int i : arr2) {
      map.put(i, 0);
    }

    // 遍历 arr1
    for (int i : arr1) {
      if (map.containsKey(i)) {
        map.put(i, map.get(i) + 1);
      } else {
        sortList.add(i);
      }
    }
    Collections.sort(sortList);

    for (int i : arr2) {
      for (int j = 0, times = map.get(i); j < times; j++) {
        retList.add(i);
      }
    }

    retList.addAll(sortList);
    return retList.stream().mapToInt(Integer::intValue).toArray();
  }
}
// @lc code=end
