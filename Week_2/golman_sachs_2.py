# Que: Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if the four points construct a square.

# The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

# A valid square has four equal sides with positive length and four equal angles (90-degree angles).

 

# Example 1:

# Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
# Output: true


def validSquare(p1,p2,p3,p4) -> bool:
        if p1==p2==p3==p4:return False
        def dist(x,y):
            return (x[0]-y[0])**2+(x[1]-y[1])**2
        ls=[dist(p1,p2),dist(p1,p3),dist(p1,p4),dist(p2,p3),dist(p2,p4),dist(p3,p4)]
        ls.sort()
        if ls[0]==ls[1]==ls[2]==ls[3]:
            if ls[4]==ls[5]:
                return True
        return False
        
p1 = [0,0]
p2 = [1,1]
p3 = [1,0]
p4 = [0,1]

res = validSquare(p1,p2,p3,p4)
print(res)

# -By Sakshi Aherkar
