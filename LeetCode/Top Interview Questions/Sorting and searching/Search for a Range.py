#Search for a Range
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/802/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def findNum(fl: bool) -> int:
            res = -1
            l = 0
            r = len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                else:
                    res = mid
                    if fl:
                        r = mid - 1
                    else:
                        l = mid + 1
            return res
        
        return [findNum(True), findNum(False)]
