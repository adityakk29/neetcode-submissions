from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = Counter(nums)
        return [k for k, v in sorted(results.items(), key=lambda x: x[1], reverse=True)[:k]]