# Given an array rectangles where rectangles[i] = [xi, yi, ai, bi] represents an axis-aligned rectangle. The bottom-left point of the rectangle is (xi, yi) and the top-right point of it is (ai, bi).

# Return true if all the rectangles together form an exact cover of a rectangular region.
def isRectangleCover(rectangles) -> bool:
    
    area = 0
    corners = set()
    a = lambda: (Y-y) * (X-x)
    
    for x, y, X, Y in rectangles:
        area += a()
        corners ^= {(x,y), (x,Y), (X,y), (X,Y)}

    if len(corners) != 4: return False
    x, y = min(corners, key=lambda x: x[0] + x[1])
    X, Y = max(corners, key=lambda x: x[0] + x[1])
    return a() == area
    
rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
res = isRectangleCover(rectangles)
print(res)

