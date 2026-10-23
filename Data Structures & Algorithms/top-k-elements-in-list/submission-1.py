class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        nes = [[] for i in range(len(nums)+1)]
        for i,num in enumerate(nums):
            freq[num] = freq.get(num,0)+1

        for num,count in freq.items():
            nes[count].append(num)
        
        res = []
        for i in range(len(nes)-1,0,-1):
            for n in nes[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        