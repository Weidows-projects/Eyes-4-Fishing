import java.util.HashMap;
import java.util.Stack;

/*
 * @?: *********************************************************************
 * @Author: Weidows
 * @Date: 2022-03-17 21:47:16
 * @LastEditors: Weidows
 * @LastEditTime: 2022-03-18 12:42:28
 * @FilePath: \Blog-private\source\_posts\public-post\LeetCode\code\394.字符串解码.java
 * @Description:
 * @!: *********************************************************************
 */
/*
 * @lc app=leetcode.cn id=394 lang=java
 *
 * [394] 字符串解码
 *
 * https://leetcode-cn.com/problems/decode-string/description/
 *
 * algorithms
 * Medium (55.80%)
 * Likes:    1067
 * Dislikes: 0
 * Total Accepted:    150.4K
 * Total Submissions: 269.4K
 * Testcase Example:  '"3[a]2[bc]"'
 *
 * 给定一个经过编码的字符串，返回它解码后的字符串。
 *
 * 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
 *
 * 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
 *
 * 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：s = "3[a]2[bc]"
 * 输出："aaabcbc"
 *
 *
 * 示例 2：
 *
 *
 * 输入：s = "3[a2[c]]"
 * 输出："accaccacc"
 *
 *
 * 示例 3：
 *
 *
 * 输入：s = "2[abc]3[cd]ef"
 * 输出："abcabccdcdcdef"
 *
 *
 * 示例 4：
 *
 *
 * 输入：s = "abc3[cd]xyz"
 * 输出："abccdcdcdxyz"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= s.length <= 30
 * s 由小写英文字母、数字和方括号 '[]' 组成
 * s 保证是一个 有效 的输入。
 * s 中所有整数的取值范围为 [1, 300] 
 *
 *
 */

class Test {
  public static void main(String[] args) {
    for (int i = 0; i < 5; i++) {
      if (i == 2) {
        System.out.println(i);
        continue;
      }
    }
  }

  // 不符合题意
  private static void v1() {
    char[] arr = "3[a]2[bc]".toCharArray();
    StringBuilder ret = new StringBuilder();

    int times = 0;
    String buff = "";

    for (int i = 0; i < arr.length; i++) {

      if (Character.isDigit(arr[i])) {
        while (Character.isDigit(arr[i])) {
          times = 10 * times + (arr[i] - 48);
          i++;
        }

        // 跳过 '['
        i++;

        while (i < arr.length && arr[i] != ']') {
          buff += arr[i];
          i++;
        }

        for (int j = 0; j < times; j++) {
          ret.append(buff);
        }
        times = 0;
        buff = "";
      } else {
        ret.append(arr[i]);
      }
    }
    System.out.println(ret.toString());
  }

  // 错误输出
  private static String v2(String s) {
    {
      char[] arr = s.toCharArray();

      int times;
      String buff = "";

      Stack<String> charsStack = new Stack<String>();
      Stack<Integer> timesStack = new Stack<Integer>();

      for (int i = 0; i < arr.length; i++) {

        for (times = 0; i < arr.length && Character.isDigit(arr[i]); i++) {
          times = 10 * times + (arr[i] - 48);
        }
        timesStack.push(times);

        if (arr[i] == '[') {
          for (buff = "", i++; i < arr.length && (Character.isDigit(arr[i]) && arr[i] == ']'); i++) {
            buff += arr[i];
          }
          charsStack.push(buff);
        }

        if (arr[i] == ']') {
          if (i < arr.length)
            i++;
          String pop = charsStack.pop();
          for (times = 0, buff = ""; times < timesStack.pop(); times++) {
            buff += pop;
          }

          if (charsStack.empty())
            charsStack.push(buff);
          else
            charsStack.push(charsStack.pop() + buff);
        }
      }
      return charsStack.pop();
    }

  }
}

// @lc code=start
class Solution {
  public String decodeString(String s) {
    char[] charArr = s.toCharArray();
    Stack<String[]> stack = new Stack<String[]>();
    int times = 0;
    String outerBuff = "";

    for (int i = 0; i < charArr.length; i++) {
      if (Character.isDigit(charArr[i])) {
        times = 10 * times + (charArr[i] - '0');
      } else if (charArr[i] == '[') {
        stack.push(new String[] { outerBuff, String.valueOf(times) });
        times = 0;
        outerBuff = "";
      } else if (charArr[i] == ']') {
        String[] pop = stack.pop();
        StringBuilder innerBuff = new StringBuilder();
        for (int j = 0; j < Integer.parseInt(pop[1]); j++) {
          innerBuff.append(outerBuff);
        }
        outerBuff = pop[0] + innerBuff.toString();
      } else {
        outerBuff += charArr[i];
      }
    }

    return outerBuff;
  }
}
// @lc code=end
