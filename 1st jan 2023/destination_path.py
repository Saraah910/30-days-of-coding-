# You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. 
# The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.
# You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui 
# and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

# Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

# Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
# Output: 4
  
  
from collections import defaultdict
import math
from heapq import heappop,heappush

def countPaths(n, roads):
    graph = defaultdict(list)
    for u, v, time in roads:
        graph[u].append([v, time])
        graph[v].append([u, time])
    
    def dijkstra(src):
        dist = [math.inf] * n
        ways = [0] * n
        minHeap = [(0, src)]  
        dist[src] = 0
        ways[src] = 1
        while minHeap:
            d, u = heappop(minHeap)
            if dist[u] < d: continue  
            for v, time in graph[u]:
                if dist[v] > d + time:
                    dist[v] = d + time
                    ways[v] = ways[u]
                    heappush(minHeap, (dist[v], v))
                elif dist[v] == d + time:
                    ways[v] = (ways[v] + ways[u]) % 1_000_000_007
        return ways[n - 1]

    return dijkstra(0)
    
n = 7
roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
# Output: 4
result = countPaths(n, roads)
print(result)


# -By Sakshi Aherkar
