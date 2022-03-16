/*
 * @?: *********************************************************************
 * @Author: Weidows
 * @Date: 2022-03-15 23:48:39
 * @LastEditors: Weidows
 * @LastEditTime: 2022-03-16 15:12:03
 * @FilePath: \Blog-private\source\_posts\public-post\LeetCode\code\219.存在重复元素-ii.go
 * @Description:
 * @!: *********************************************************************
 */
/*
 * @lc app=leetcode.cn id=219 lang=golang
 *
 * [219] 存在重复元素 II
 *
 * https://leetcode-cn.com/problems/contains-duplicate-ii/description/
 *
 * algorithms
 * Easy (44.45%)
 * Likes:    456
 * Dislikes: 0
 * Total Accepted:    167.4K
 * Total Submissions: 376.7K
 * Testcase Example:  '[1,2,3,1]\n3'
 *
 * 给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且
 * abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。
 *
 *
 *
 * 示例 1：
 *
 *
 * 输入：nums = [1,2,3,1], k = 3
 * 输出：true
 *
 * 示例 2：
 *
 *
 * 输入：nums = [1,0,1,1], k = 1
 * 输出：true
 *
 * 示例 3：
 *
 *
 * 输入：nums = [1,2,3,1,2,3], k = 2
 * 输出：false
 *
 *
 *
 *
 *
 * 提示：
 *
 *
 * 1 <= nums.length <= 10^5
 * -10^9 <= nums[i] <= 10^9
 * 0 <= k <= 10^5
 *
 *
 */

package main

// @lc code=start
func containsNearbyDuplicate(nums []int, k int) bool {
	return solu2(nums, k)
}

func solu1(nums []int, k int) bool {
	// int -> []int
	maps := make(map[int][]int)

	for i, v := range nums {
		// 判空
		if _, ok := maps[v]; ok {
			maps[v] = append(maps[v], i)
		} else {
			maps[v] = []int{i}
		}
	}

	for _, arr := range maps {
		if len(arr) > 1 {
			for i := 0; i < len(arr)-1; i++ {
				if arr[i+1]-arr[i] <= k {
					return true
				}
			}
		}
	}
	return false
}

func solu2(nums []int, k int) bool {
	queue := make([]int, 0)

	for _, v := range nums {
		for _, j := range queue {
			if v == j {
				return true
			}
		}
		queue = append(queue, v)
		if len(queue) > k {
			queue = queue[1:]
		}
	}
	return false
}

// @lc code=end
