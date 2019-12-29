#First Bad Version
#https://leetcode.com/explore/featured/card/top-interview-questions-easy/96/sorting-and-searching/774/

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        good = 0
        bad = n
        while good < (bad -1):
            prob = (good + bad)//2
            if isBadVersion(prob):
                bad = prob
            else:
                good = prob
        return bad
