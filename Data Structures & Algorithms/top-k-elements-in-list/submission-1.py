from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        result = []
        for i in range(k):
            result.append(max(num_count, key=num_count.get))
            num_count.pop(max(num_count, key=num_count.get))
        return result