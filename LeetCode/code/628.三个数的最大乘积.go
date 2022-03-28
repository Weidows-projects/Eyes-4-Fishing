/*
 * @lc app=leetcode.cn id=628 lang=golang
 *
 * [628] 三个数的最大乘积
 *
 * https://leetcode-cn.com/problems/maximum-product-of-three-numbers/description/
 *
 * algorithms
 * Easy (52.44%)
 * Likes:    369
 * Dislikes: 0
 * Total Accepted:    90.1K
 * Total Submissions: 171.8K
 * Testcase Example:  '[1,2,3]'
 *
 * 给你一个整型数组 nums ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3]
 * 输出：6
 *
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,2,3,4]
 * 输出：24
 *
 *
 * 示例 3：
 *
 *
 * 输入：nums = [-1,-2,-3]
 * 输出：-6
 *
 *
 *
 *
 * 提示：
 *
 *
 * 3
 * -1000
 *
 *
 */

package main

import "math"

func test() {
	search := [5]int{0}
	for _, v := range search {
		println(search[v])
	}
	// 0
	// 0
	// 0
	// 0
	// 0
}

// @lc code=start
// 线性扫描法
func maximumProduct(nums []int) int {
	if len(nums) == 3 {
		return nums[0] * nums[1] * nums[2]
	}

	search := [5]int{math.MaxInt64, math.MaxInt64, math.MinInt64, math.MinInt64, math.MinInt64}
	for _, v := range nums {
		if v <= search[0] {
			search[1] = search[0]
			search[0] = v
		} else if v < search[1] {
			search[1] = v
		}

		if v >= search[4] {
			search[2] = search[3]
			search[3] = search[4]
			search[4] = v
		} else if v >= search[3] {
			search[2] = search[3]
			search[3] = v
		} else if v > search[2] {
			search[2] = v
		}
	}

	v1 := search[0] * search[1] * search[4]
	v2 := search[2] * search[3] * search[4]

	if v1 >= v2 {
		return v1
	} else {
		return v2
	}
}

// @lc code=end
// Accepted
// 92/92 cases passed (28 ms)
// Your runtime beats 97.19 % of golang submissions
// Your memory usage beats 76.97 % of golang submissions (6.4 MB)
