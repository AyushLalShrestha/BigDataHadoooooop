
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = [[]]
        next_subsets = list()
        for n in nums:
            all_subsets.append([n])
            next_subsets.append([n])
        if len(nums) == 1:
            return all_subsets
        stop = False
        while not stop:
            new_next_subsets = list()
            for i, l in enumerate(next_subsets):
                for to_add in next_subsets[i + 1:]:
                    entry = sorted(list(set(l + to_add)))
                    if entry not in all_subsets:
                        new_next_subsets.append(entry)
                        all_subsets.append(entry)
                    if len(entry) == len(nums):
                        stop = True
            next_subsets = new_next_subsets
        return all_subsets


if __name__ == "__main__":
    # print(Solution().subsets([1,9,8,3,-1,0]))
    print(Solution().subsets([1, 2, 3, 4, 5, 6, 7, 8, 9]))
