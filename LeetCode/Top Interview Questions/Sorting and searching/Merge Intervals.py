#Merge Intervals
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/803/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals) == 0:
            return []
        res = []
        first = intervals[0][0]
        last = intervals[0][1]
        for i in range(1, len(intervals)):
            if last < intervals[i][0]:
                res.append([first, last])
                first = intervals[i][0]

            last = max(last, intervals[i][1])
        res.append([first, last])
        return res
