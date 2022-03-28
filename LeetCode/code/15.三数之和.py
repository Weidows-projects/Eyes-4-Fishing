#
# @lc app=leetcode.cn id=15 lang=python
#
# [15] 三数之和
#
# https://leetcode-cn.com/problems/3sum/description/
#
# algorithms
# Medium (34.79%)
# Likes:    4540
# Dislikes: 0
# Total Accepted:    877.5K
# Total Submissions: 2.5M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0
# 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
# 示例 1：
#
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#
#
# 示例 2：
#
#
# 输入：nums = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：nums = [0]
# 输出：[]
#
#
#
#
# 提示：
#
#
# 0
# -10^5
#
#
#

# @lc code=start
class Solution(object):
    # i ->
    #     | m->  <-r |
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] > nums[i - 1]:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    s = nums[i] + nums[l] + nums[r]
                    if s < 0:
                        l += 1
                    elif s > 0:
                        r -= 1
                    else:
                        res.append([nums[i], nums[l], nums[r]])
                        # 去除
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
        return res

    # 下面这第一种方法是行不通的
    # l ->       <-r
    #     | m-> |
    def threeSum_1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        res = []
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] > 0: break

            m = l + 1
            while m < r:
                sum = nums[l] + nums[m] + nums[r]
                if sum == 0:
                    try:
                        res.index([nums[l], nums[m], nums[r]])
                    except:  # 报错就说明没有,为了去重
                        res.append([nums[l], nums[m], nums[r]])
                elif sum > 0 and m == l + 1:
                    r -= 1
                    continue
                m += 1
            l += 1
        return res
# @lc code=end
