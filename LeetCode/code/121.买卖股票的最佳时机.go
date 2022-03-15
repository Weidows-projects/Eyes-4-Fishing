/*
 * @?: *********************************************************************
 * @Author: Weidows
 * @Date: 2022-03-15 16:56:39
 * @LastEditors: Weidows
 * @LastEditTime: 2022-03-15 23:43:48
 * @FilePath: \Blog-private\source\_posts\public-post\LeetCode\code\121.买卖股票的最佳时机.go
 * @Description:
 * @!: *********************************************************************
 */
/*
 * @lc app=leetcode.cn id=121 lang=golang
 *
 * [121] 买卖股票的最佳时机
 *
 * https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/description/
 *
 * algorithms
 * Easy (57.58%)
 * Likes:    2202
 * Dislikes: 0
 * Total Accepted:    708.3K
 * Total Submissions: 1.2M
 * Testcase Example:  '[7,1,5,3,6,4]'
 *
 * 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
 *
 * 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。
 *
 * 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：[7,1,5,3,6,4]
 * 输出：5
 * 解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
 * ⁠    注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
 *
 *
 * 示例 2：
 *
 *
 * 输入：prices = [7,6,4,3,1]
 * 输出：0
 * 解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1
 * 0
 *
 *
 */

package main

import "math"

// @lc code=start
func maxProfit(prices []int) int {
	min, max := math.MaxInt32, 0

	for _, v := range prices {
		if v < min {
			min = v
		} else if v-min > max {
			max = v - min
		}
	}
	return max
}

// @lc code=end
