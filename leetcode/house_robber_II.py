from typing import List


class Solution:
    def rob_partial(self, nums):
        total_houses = len(nums)
        if total_houses <= 2:
            return max(nums)

        best_robs = [0] * total_houses
        best_robs[0] = nums[0]
        best_robs[1] = max(nums[:2])
        for i in range(2, total_houses):
            best_robs[i] = max(best_robs[i - 1], nums[i] + best_robs[i - 2])

        return best_robs[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return self.rob_partial(nums)
        rob1 = self.rob_partial(nums[:-1])
        rob2 = self.rob_partial(nums[1:])
        return max([rob1, rob2])


if __name__ == "__main__":
    nums = [1, 2, 3]  # 3
    # nums = [200,3,140,20,10] #340
    # nums = [1,2,3,1]  # 4
    # nums = [2,3,2]  # 3
    # nums = [2,7,9,3,1]  # 11
    # nums = [1,7,9,2]  # 10
    nums = [1, 1, 1, 2]  # 3
    # nums = [0]
    solution = Solution()
    res = solution.rob(nums)
    print(res)
