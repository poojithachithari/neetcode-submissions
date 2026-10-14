class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {}
        for frm , to in tickets:
            if frm not in graph:
                graph[frm] =[]
            graph[frm].append(to)
        
        for key in graph:
            graph[key].sort(reverse=True)
        
        path = []

        def dfs(loc):
            while loc in graph and graph[loc]:
                next_loc = graph[loc].pop()
                dfs(next_loc)
            path.append(loc)
        
        dfs("JFK")
        return path[::-1]
        