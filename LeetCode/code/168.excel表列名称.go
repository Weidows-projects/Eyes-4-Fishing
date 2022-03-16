/*
 * @?: *********************************************************************
 * @Author: Weidows
 * @Date: 2022-03-16 23:23:09
 * @LastEditors: Weidows
 * @LastEditTime: 2022-03-17 01:37:30
 * @FilePath: \Blog-private\source\_posts\public-post\LeetCode\code\168.excel表列名称.go
 * @Description:
 * @!: *********************************************************************
 */
/*
 * @lc app=leetcode.cn id=168 lang=golang
 *
 * [168] Excel表列名称
 *
 * https://leetcode-cn.com/problems/excel-sheet-column-title/description/
 *
 * algorithms
 * Easy (43.43%)
 * Likes:    510
 * Dislikes: 0
 * Total Accepted:    99.3K
 * Total Submissions: 228.5K
 * Testcase Example:  '1'
 *
 * 给你一个整数 columnNumber ，返回它在 Excel 表中相对应的列名称。
 *
 * 例如：
 *
 *
 * A -> 1
 * B -> 2
 * C -> 3
 * ...
 * Z -> 26
 * AA -> 27
 * AB -> 28
 * ...
 *
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：columnNumber = 1
 * 输出："A"
 *
 *
 * 示例 2：
 *
 *
 * 输入：columnNumber = 28
 * 输出："AB"
 *
 *
 * 示例 3：
 *
 *
 * 输入：columnNumber = 701
 * 输出："ZY"
 *
 *
 * 示例 4：
 *
 *
 * 输入：columnNumber = 2147483647
 * 输出："FXSHRXW"
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 *
 *
 */
package main

import (
	"fmt"
)

func main() {
	runeArr := make([]rune, 0)
	runeArr = append(runeArr, rune(65), rune(65+25))
	s := string(runeArr)
	fmt.Printf(s)
}

// @lc code=start
func convertToTitle(columnNumber int) string {
	runeArr := make([]rune, 0)
	for columnNumber != 0 {
		columnNumber--
		runeArr = append(runeArr, rune(65+columnNumber%26))
		columnNumber /= 26
	}
	for i, j := 0, len(runeArr)-1; i < j; i, j = i+1, j-1 {
		runeArr[i], runeArr[j] = runeArr[j], runeArr[i]
	}

	return string(runeArr)
}

// @lc code=end
/*
Accepted
18/18 cases passed (0 ms)
Your runtime beats 100 % of golang submissions
Your memory usage beats 64.02 % of golang submissions (1.8 MB)
*/
