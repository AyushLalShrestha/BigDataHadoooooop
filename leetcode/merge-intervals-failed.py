
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        hm = {}
        merged_intervals = []
        for start, end in intervals:
            range_start = start
            range_end = end
            nums = []
            for num in range(start, end + 1):
                nums.append(num)
                if num in hm:
                    num_range = hm[num]
                    range_start = min(range_start, num_range[0])
                    range_end = max(range_end, num_range[1])
                    for n in range(num_range[0], num_range[1] + 1):
                        nums.append(n)
            for num in nums:
                if num in hm and hm[num] in merged_intervals:
                    merged_intervals.remove(hm[num])
                hm[num] = [range_start, range_end]
            merged_intervals.append([range_start, range_end])

        return merged_intervals


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = [[1, 3], [2, 6], [5, 10], [15, 18]]
    # intervals = [[1, 4], [4, 5]]
    # intervals = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    res = Solution().merge(intervals)
    print(res)
