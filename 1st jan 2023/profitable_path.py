

from collections import defaultdict
import math
def mostProfitablePath(edges, bob, amount) -> int:
    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)
    visited = set()
    lvl = 0
    _sum = 0
    _max = -math.inf
    def remove_bob_income(src, bob, lvl):
        if src == bob:
            lvl = lvl
            amount[bob] = 0
            return True
        visited.add(src)
        for child in graph[src]:
            if child not in visited:
                ans = remove_bob_income(child, bob, lvl + 1)
                if ans:
                    if lvl & 1 and lvl == (lvl + 1)//2:
                        amount[src] //= 2
                    elif lvl > (lvl // 2):
                        amount[src] = 0
                    else:
                        _sum += amount[src]   
                    return True
        return False
    
        visited.remove(src)
    
    def dfs(src, income, visited):
        if len(graph[src]) == 1 and src != 0:
            _max = max(_max, income)
            return
        visited.add(src)
        for child in graph[src]:
            if child not in visited:
                dfs(child, income + amount[child], visited)
        visited.remove(src)
            
    remove_bob_income(0, bob, 1)
    dfs(0, amount[0], set())
    return _max
    
edges = [[0,1],[1,2],[1,3],[3,4]]
bob = 3
amount = [-2,4,2,-4,6]
res = mostProfitablePath(edges,bob,amount)
print(res)
