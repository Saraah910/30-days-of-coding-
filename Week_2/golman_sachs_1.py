# Que : Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
  
  
from collections import defaultdict
def maxPoints(points) -> int:
    if len(points)<=2: return len(points)

    def slope(p1,p2):

        if p2[0]-p1[0] == 0:
            return inf
        return (p2[1]-p1[1]) / (p2[0]-p1[0])                

    res = 0
    for i in range(len(points)):
        count = defaultdict(int)
        for j in range(i+1,len(points)):
            count[slope(points[i],points[j])] += 1
        # print(count)
        if count:
            res = max(res,max(count.values()))
    
    return res + 1
    
points = [[1,1],[2,2],[3,3]]
res = maxPoints(points)

print(res)
    
# -By Sakshi Aherkar

    
