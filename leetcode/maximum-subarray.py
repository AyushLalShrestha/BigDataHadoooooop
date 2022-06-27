from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        highest_sum = nums[0]
        sum_of_current_contiguous_list = 0

        for num in nums:
            if sum_of_current_contiguous_list + num < num:
                sum_of_current_contiguous_list = num
            else:
                sum_of_current_contiguous_list += num

            if sum_of_current_contiguous_list > highest_sum:
                highest_sum = sum_of_current_contiguous_list

        return highest_sum


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [5, 4, -1, 7, 8]
    nums = [-1]
    nums = [1, 2]
    nums = [-1, -2]
    nums = [-2, -1]
    nums = [8, -19, 5, -4, 20]
    res = Solution().maxSubArray(nums)
    print(res)
