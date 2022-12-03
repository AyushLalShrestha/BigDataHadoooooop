from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda e: e[0])
        merged = []

        for interval in intervals:
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
                continue

            merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


if __name__ == "__main__":
    intervals = [[2, 6], [5, 6], [4, 10], [2, 4]]
    res = Solution().merge(intervals)
    print(res)
