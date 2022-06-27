from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        if len(nums) == 1:
            return [
                nums,
            ]
        for i, num in enumerate(nums):
            remaining_nums = [n for j, n in enumerate(nums) if i != j]
            for remaining_perms in self.permuteUnique(remaining_nums):
                temp = [num] + remaining_perms
                if temp not in permutations:
                    permutations.append([num] + remaining_perms)
        return permutations


if __name__ == "__main__":
    nums = [1, 1, 2]
    nums = [1, 2, 3]
    res = Solution().permute(nums)
    print((res))
