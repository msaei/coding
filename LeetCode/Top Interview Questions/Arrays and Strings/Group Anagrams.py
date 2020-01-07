#Group Anagrams
#https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/778/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key in anagrams.keys():
                anagrams[key].append(word)
            else:
                anagrams[key] = [word]
        return anagrams.values()
