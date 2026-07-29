class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # numbers are not unique so no hashset
        # Need to use hashMap becoz o(n) is required time complexity 
        '''
        hashmap = {key:value}
        key => element => nums[i]
        value => frequency of element => count(nums[i])

        result : K Most frequent 
        need to return k keys which has high values 

        one more loop with range(K):
        find the max value return the keys of it 

        Butttt
        we can also group the elements which have same frequency in the hashmap
        like Group Anagrams 
        then return the values 
        '''
        count= {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1+ count.get(n,0)
        for n,c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) -1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res












