#Top K Frequent Elements
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/799/


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        candidates = list(count.keys())
        candidates.sort(key = lambda n : -count[n])
        return candidates[:k]
