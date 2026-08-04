class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack= [] #0
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                x = stack.pop() # 0
                res[x] = i-x # no.of days we waited
            
            stack.append(i)
        return res

        