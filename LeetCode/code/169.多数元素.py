'''
?: *********************************************************************
Author: Weidows
Date: 2022-03-15 01:07:18
LastEditors: Weidows
LastEditTime: 2022-03-15 01:26:51
FilePath: \Blog-private\source\_posts\public-post\LeetCode\code\169.多数元素.py
Description:
!: *********************************************************************
'''

#
# @lc app=leetcode.cn id=169 lang=python
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (66.56%)
# Likes:    1354
# Dislikes: 0
# Total Accepted:    474.8K
# Total Submissions: 713.3K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
# 示例 1：
#
#
# 输入：[3,2,3]
# 输出：3
#
# 示例 2：
#
#
# 输入：[2,2,1,1,1,2,2]
# 输出：2
#
#
#
#
# 进阶：
#
#
# 尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
#
#
#


# @lc code=start
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in list(set(nums)):
            if nums.count(i) > len(nums) / 2:
                return i


# @lc code=end
