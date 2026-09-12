from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count = Counter(nums)
        result = []
        for i in range(k):
            max_key = max(num_count, key=num_count.get)
            result.append(max_key)
            num_count.pop(max_key)
        return result