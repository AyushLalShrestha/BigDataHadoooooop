
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_k_elements = []
        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1
            if num in top_k_elements:
                continue
            if len(top_k_elements) < k:
                top_k_elements.append(num)
            else:
                for top in top_k_elements:
                    if count_map[top] < count_map[num]:
                        top_k_elements.remove(top)
                        top_k_elements.append(num)
                        break

        return top_k_elements
