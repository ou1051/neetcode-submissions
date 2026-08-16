class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)] #[[]*len(num)+1個分,+1 to manage num in list are all the same]
        
        for i in nums:
            count[i] = 1 + count.get(i,0)
        for i,c in count.items():#i for num, c for how many
            freq[c].append(i)
        
        res = []
        for n in range(len(freq)-1,0,-1):
            for i in freq[n]:
                res.append(i)
                if len(res) == k:
                    return res




