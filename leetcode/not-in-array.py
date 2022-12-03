from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        all_nums = set(range(1, len(nums) + 1))
        return list(all_nums.difference(set(nums)))


if __name__ == "__main__":
    solution = Solution()

    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    # nums = [1,1]
    print(solution.findDisappearedNumbers(nums))
