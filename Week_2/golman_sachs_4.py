# Que: You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. 
# A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

# Return the number of boomerangs.

 

# Example 1:

# Input: points = [[0,0],[1,0],[2,0]]
# Output: 2

def numberOfBoomerangs(points) -> int:
    res = 0
    for p in points:
        cmap = {}
        for q in points:
            f = p[0]-q[0]
            s = p[1]-q[1]
            cmap[f*f + s*s] = 1 + cmap.get(f*f + s*s, 0)
        for k in cmap:
            res += cmap[k] * (cmap[k] -1)
    return res
    
points = [[0,0],[1,0],[2,0]]
res = numberOfBoomerangs(points)

print(res)

# -By Sakshi AHerkar
