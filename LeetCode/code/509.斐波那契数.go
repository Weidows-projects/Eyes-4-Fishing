/*
 * @lc app=leetcode.cn id=509 lang=golang
 *
 * [509] 斐波那契数
 *
 * https://leetcode-cn.com/problems/fibonacci-number/description/
 *
 * algorithms
 * Easy (66.81%)
 * Likes:    438
 * Dislikes: 0
 * Total Accepted:    364.8K
 * Total Submissions: 547.4K
 * Testcase Example:  '2'
 *
 * 斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：
 *
 *
 * F(0) = 0，F(1) = 1
 * F(n) = F(n - 1) + F(n - 2)，其中 n > 1
 *
 *
 * 给定 n ，请计算 F(n) 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：n = 2
 * 输出：1
 * 解释：F(2) = F(1) + F(0) = 1 + 0 = 1
 *
 *
 * 示例 2：
 *
 *
 * 输入：n = 3
 * 输出：2
 * 解释：F(3) = F(2) + F(1) = 1 + 1 = 2
 *
 *
 * 示例 3：
 *
 *
 * 输入：n = 4
 * 输出：3
 * 解释：F(4) = F(3) + F(2) = 2 + 1 = 3
 *
 *
 *
 *
 * 提示：
 *
 *
 * 0 <= n <= 30
 *
 *
 */
package main

// @lc code=start
func fib(n int) int {
	return iteration_fib(n)
	// return recursion_fib(n)
}

// Accepted
// 31/31 cases passed (0 ms)
// Your runtime beats 100 % of golang submissions
// Your memory usage beats 65.97 % of golang submissions (1.8 MB)
func iteration_fib(n int) int {
	if n < 2 {
		return n
	}
	a, b := 0, 1
	for i := 2; i <= n; i++ {
		c := a + b
		a = b
		b = c
	}
	return b
}

// Accepted
// 31/31 cases passed (8 ms)
// Your runtime beats 24.75 % of golang submissions
// Your memory usage beats 55.61 % of golang submissions (1.8 MB)
func recursion_fib(n int) int {
	if n < 2 {
		return n
	}
	return recursion_fib(n-1) + recursion_fib(n-2)
}

// 还有通项公式和矩阵解法, 数学范畴的...要打草稿
// @lc code=end
