#Search in Rotated Sorted Array
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/804

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        #find the smallest number location
        l = 0
        r = len(nums) - 1
        while (l < r):
            print(l,r)
            mid = (l + r)//2
            if nums[r] < nums[mid]:
                l = mid + 1
            else:
                r = mid
                
        piv = l
        print(piv)
        if piv == 0:
            l = 0
            r = len(nums) - 1
        elif target >= nums[0]:
            l = 0
            r = piv - 1
        else:
            l = piv
            r = len(nums) - 1
            
        res = -1
        while (l <= r):
            print(l,r)
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
            
        return res
