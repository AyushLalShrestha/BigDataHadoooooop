from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        if len(nums) == 1:
            return [
                nums,
            ]
        for i, num in enumerate(nums):
            remaining_nums = [n for n in nums if n != num]
            for remaining_perms in self.permute(remaining_nums):
                permutations.append([num] + remaining_perms)
        return permutations


if __name__ == "__main__":
    nums = [1, 2, 3]
    nums = [0, 1]
    nums = [
        1,
    ]
    nums = [1, 2, 3, 4]
    res = Solution().permute(nums)
    print(len(res))
