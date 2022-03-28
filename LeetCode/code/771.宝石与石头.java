import java.util.HashSet;

/*
 * @lc app=leetcode.cn id=771 lang=java
 *
 * [771] 宝石与石头
 *
 * https://leetcode-cn.com/problems/jewels-and-stones/description/
 *
 * algorithms
 * Easy (85.17%)
 * Likes:    692
 * Dislikes: 0
 * Total Accepted:    162.2K
 * Total Submissions: 190.5K
 * Testcase Example:  '"aA"\n"aAAbbbb"'
 *
 *  给你一个字符串 jewels 代表石头中宝石的类型，另有一个字符串 stones 代表你拥有的石头。 stones
 * 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。
 *
 * 字母区分大小写，因此 "a" 和 "A" 是不同类型的石头。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：jewels = "aA", stones = "aAAbbbb"
 * 输出：3
 *
 *
 * 示例 2：
 *
 *
 * 输入：jewels = "z", stones = "ZZ"
 * 输出：0
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= jewels.length, stones.length <= 50
 * jewels 和 stones 仅由英文字母组成
 * jewels 中的所有字符都是 唯一的
 *
 *
 */

// @lc code=start
class Solution {
  public int numJewelsInStones(String jewels, String stones) {
    // return numJewelsInStones1(jewels, stones);
    return numjewelsInStones2(jewels, stones);
  }

  // String.contains()
  // Accepted 255/255
  // cases passed (1 ms)
  // Your runtime beats 69.56 % of java submissions
  // Your memory usage beats 49.79 % of java submissions (39.6 MB)
  int numJewelsInStones1(String jewels, String stones) {
    int num = 0;

    for (int i = 0; i < stones.length(); i++) {
      if (jewels.contains(stones.charAt(i) + "")) {
        num++;
      }
    }

    return num;
  }

  // Accepted 255/255
  // cases passed (1 ms)
  // Your runtime beats 69.56 % of java submissions
  // Your memory usage beats 23.41 % of java submissions (39.9 MB)
  int numjewelsInStones2(String jewels, String stones) {
    int num = 0;
    HashSet<Character> jewelSet = new HashSet<Character>();

    for (int i = 0; i < jewels.length(); i++) {
      jewelSet.add(jewels.charAt(i));
    }

    for (int i = 0; i < stones.length(); i++) {
      if (jewelSet.contains(stones.charAt(i))) {
        num++;
      }
    }

    return num;
  }
}
// @lc code=end
