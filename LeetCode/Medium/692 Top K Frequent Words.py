#692 Top K Frequent Words
#https://leetcode.com/problems/top-k-frequent-words/

#Using collections
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]
    
#Using heapq
class Solution(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in xrange(k)]

# my solution    
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # calcuate frequency of words
        frequenty = {}
        for word in words:
            if word in frequenty.keys():
                frequenty[word] += 1
            else:
                frequenty[word] = 1
        # put the words in frequency buckets
        buckets = {}
        for key in frequenty.keys():
            count = frequenty[key]
            if count in buckets.keys():
                buckets[count].append(key)
            else:
                buckets[count] = [key]
        # sort buckets keys
        bucket_keys = sorted(buckets.keys())
        # fill out the first k
        res = []
        cur_count = bucket_keys.pop()
        cur_bucket = sorted(buckets[cur_count])[::-1]
        while k > 0:
            if len(cur_bucket) == 0:
                cur_count = bucket_keys.pop()
                cur_bucket = sorted(buckets[cur_count])[::-1]
            res.append(cur_bucket.pop())
            k -= 1
        return res
            
