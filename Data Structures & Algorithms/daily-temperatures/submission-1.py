class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack= [] #0
        res = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0] : #temperatures[stack[-1]] < temperatures[i]
                stackt,stackInd = stack.pop() # 0
                res[stackInd] = i-stackInd # no.of days we waited
            
            stack.append([t,i])
        return res

        