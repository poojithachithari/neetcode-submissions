class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        newMap = defaultdict(list)
        for i in strs:
            count = [0]*26
            for ch in i:
                count[ord(ch)-ord('a')] +=1
            newMap[tuple(count)].append(i)
        return list(newMap.values())
            
        